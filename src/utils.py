def getNestedValue(inputDict, keyPath):
    currentValue = inputDict

    for key in keyPath:
        currentValue = currentValue.get(key)

        if currentValue is None:
            return ''

    return currentValue
