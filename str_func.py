def do_upper(data_string):
    """Возвышает(!) все символы в верхний регистр в строке"""
    return data_string.upper()

def do_upper_first_symbol(data_string):
    """Делает первый символ в строке Заглавным"""
    if not isinstance(data_string, str):
        raise TypeError("Аргумент должен быть строкой.")

    if not data_string:
        return ""

    return data_string[0].upper() + data_string[1:]
