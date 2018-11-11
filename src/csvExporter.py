import csv
import os
import time
from params.dataMappings import dataMappings, HEADER_NAME, KEY_NAME

class CsvExporter:
    exportPath = '%s/export' % os.getcwd()
    filename = '%s.csv' % time.strftime('%Y%m%d%H%M%S')
    sortingOrder = [item[KEY_NAME] for item in dataMappings]

    def _checkCreateExportPath(self):
        if not os.path.exists(self.exportPath):
            os.makedirs(self.exportPath)

    def _writeRow(self, data):
        self.writer.writerow(data)

    def _writeHeader(self):
        self._writeRow([item[HEADER_NAME] for item in dataMappings])

    def _prepareWriter(self):
        self.file = open('%s/%s' % (self.exportPath, self.filename), mode='w+')
        self.writer = csv.writer(self.file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        self._writeHeader()

    def __init__(self):
        self._checkCreateExportPath()
        self._prepareWriter()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

    def write(self, data):
        for row in data:
            self._writeRow([row[key] for key in self.sortingOrder])
