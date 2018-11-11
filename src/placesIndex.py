placesIndex = {}

def add(placeId):
    placesIndex[placeId] = 1

def has(placeId):
    return placesIndex.get(placeId, 0)
