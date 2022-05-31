def validate_int(string :str):
    try:
        return int(string)
    except:
        return -1


def validate_float(string : str):
    try:
        return float(string)
    except:
        return -1