import sys
from getopt import getopt, GetoptError
from exceptions import ParamError

def _getRawParams():
    return sys.argv[1:]

def getParamValue(name):
    try:
        opts, args = getopt(_getRawParams(), '', ['%s=' % name])
    except GetoptError as err:
        print(err)
        raise ParamError()

    if len(opts) == 0:
        raise ParamError()
    
    for opt, value in opts:
        if opt == '--%s' % name:
            return value
        else:
            raise ParamError()
