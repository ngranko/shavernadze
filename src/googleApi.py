import json
import settings
import urllib.request
from urllib.parse import quote
from exceptions import GoogleError

STATUS_OK = 'OK'

def _parseJson(string):
    return json.loads(string)

def _doRequest(url):
    url = urllib.request.urlopen(url)
    contents = url.read()
    url.close()
    return _parseJson(contents)

def _validate(result):
    status = result.get('status', '')
    if status != STATUS_OK:
        raise GoogleError(status, result)

def _request(url):
    rawData = _doRequest(url)
    _validate(rawData)
    return rawData

def getList(lat, lng, searchString):
    return _request('https://maps.googleapis.com/maps/api/place/textsearch/json?key=%s&location=%f,%f&query=%s&language=ru&region=ru' % (settings.GOOGLE_API_KEY, lat, lng, quote(searchString)))

def getNextPage(pageToken):
    return _request('https://maps.googleapis.com/maps/api/place/textsearch/json?key=%s&pagetoken=%s' % (settings.GOOGLE_API_KEY, quote(pageToken)))

def getDetails(placeId):
    return _request('https://maps.googleapis.com/maps/api/place/details/json?key=%s&placeid=%s&fields=price_level&language=ru&region=ru' % (settings.GOOGLE_API_KEY, placeId)).get('result', {})
