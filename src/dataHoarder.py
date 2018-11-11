import googleApi
import placesIndex
from utils import getNestedValue
from exceptions import GoogleError
from params.dataMappings import dataMappings, KEY_NAME, RESPONSE_PATH

class DataHoarder:
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng
        self.list = []
        self.pageToken = None
        self.requested = False

    def _hasMoreResults(self):
        return self.pageToken is not None

    def _getPlaceId(self, rawItem):
        return rawItem.get('place_id', '')

    def _makeItem(self, rawItem):
        preparedItem = {}
        for mapping in dataMappings:
            preparedItem[mapping[KEY_NAME]] = getNestedValue(rawItem, mapping[RESPONSE_PATH])

        try:
            preparedItem.update(googleApi.getDetails(self._getPlaceId(rawItem)))
        except GoogleError as error:
            print('Requesting item %s details failed (%s)' % (self._getPlaceId(rawItem), error.responseStatus))
        
        return preparedItem

    def _makeList(self, rawList):
        result = []

        for rawItem in rawList:
            if not placesIndex.has(self._getPlaceId(rawItem)):
                placesIndex.add(self._getPlaceId(rawItem))
                result.append(self._makeItem(rawItem))
            
        return result

    def _handleRawData(self, rawData):
        self.pageToken = rawData.get('next_page_token')
        self.list.extend(self._makeList(rawData.get('results', [])))

    def getNextChunk(self):
        rawData = googleApi.getNextPage(self.pageToken)
        self._handleRawData(rawData)

    def loadData(self, searchString):
        if not self.requested:
            try:
                self.requested = True
                rawData = googleApi.getList(self.lat, self.lng, searchString)
                self._handleRawData(rawData)

                while self._hasMoreResults():
                    self.getNextChunk()
            except GoogleError as error:
                print('Requesting item list failed (%s): %s' % (error.responseStatus, error.rawResponse))

        return self.list
