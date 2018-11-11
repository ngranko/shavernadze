class Error(Exception):
    pass

class ParamError(Error):
    def __init__(self, message = ''):
        self.message = message

class GoogleError(Error):
    def __init__(self, responseStatus, rawResponse):
        self.responseStatus = responseStatus
        self.rawResponse = rawResponse
