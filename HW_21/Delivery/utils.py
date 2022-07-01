
def balance(place):
    strings = []
    for key, item in place.items():
        strings.append("{}: {}".format(key.capitalize(), item))
    result = ", ".join(strings)
    return result

