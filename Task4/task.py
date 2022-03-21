def number_to_array(number: int):
    string_number = str(number)

    new_string = ""
    count = 0
    for num in string_number[::-1]:
        if count == 3:
            new_string += " "
            count = 0

        new_string += num
        count += 1

    result_array = []
    sub_array = []
    for num in new_string[::-1]:
        if num == " ":
            result_array.append(sub_array)
            sub_array = []
        else:
            sub_array.append(int(num))
    result_array.append(sub_array)

    return result_array


units = (
    'ноль',

    ('один', 'одна'),
    ('два', 'две'),

    'три', 'четыре', 'пять',
    'шесть', 'семь', 'восемь', 'девять'
)

tens_exclusive = (
    'десять', 'одиннадцать',
    'двенадцать', 'тринадцать',
    'четырнадцать', 'пятнадцать',
    'шестнадцать', 'семнадцать',
    'восемнадцать', 'девятнадцать'
)

tens = (
    '', '',
    'двадцать', 'тридцать',
    'сорок', 'пятьдесят',
    'шестьдесят', 'семьдесят',
    'восемьдесят', 'девяносто'
)

hundreds = (
    '',
    'сто', 'двести',
    'триста', 'четыреста',
    'пятьсот', 'шестьсот',
    'семьсот', 'восемьсот',
    'девятьсот'
)

orders = (
    ('тысяча', 'тысячи', 'тысяч'),
    ('миллион', 'миллиона', 'миллионов'),
    ('миллиард', 'миллиарда', 'миллиардов'),
)

minus = 'минус'


def convert_to_string(number_array: list):
    if len(number_array) == 1 and number_array[0][0] == 0:
        return units[0]

    current_order = len(number_array) - 2

    result_string = ""
    for nums in number_array:
        ten = 0
        unit = 0
        if len(nums) == 1:
            unit = nums[0]

            result_string += process_units(0, unit, current_order)

        if len(nums) == 2:
            ten = nums[0]
            unit = nums[1]

            result_string += process_tens(ten, unit)
            result_string += process_units(ten, unit, current_order)

        if len(nums) == 3:
            hundred = nums[0]
            ten = nums[1]
            unit = nums[2]

            result_string += process_hundreds(hundred, ten, unit)
            result_string += process_tens(ten, unit)
            result_string += process_units(ten, unit, current_order)

        if current_order >= 0:
            result_string += process_order(ten, unit, current_order)
            current_order -= 1

    return result_string


def process_units(ten: int, unit: int, order: int):
    if ten == 0 and unit == 0:
        return ""  # 100 - возвращаем пустую строку
    elif ten == 1:
        return ""  # 10, 11, 12, ... 19 - возвращаем пустую строку
    elif unit == 1 or unit == 2:
        if order == 0:
            return units[unit][1]  # одна, две
        else:
            return units[unit][0]  # один, два
    else:
        return units[unit]  # всё остальное


def process_tens(ten: int, unit: int):
    if ten == 1:
        return tens_exclusive[unit]  # 10, 11, 12, 13, ... 19
    elif ten != 0:
        return tens[ten] + " "  # 20, 30, 40, ... 90
    else:
        return ""  # 100 - возвращаем пустую строку


def process_hundreds(hundred: int, ten: int, unit: int):
    if ten == 0 and unit == 0:
        return hundreds[hundred]  # 100 - пробелов нет
    else:
        return hundreds[hundred] + " "  # 101 - нужны пробелы


def process_order(ten: int, unit: int, order: int):
    if unit == 1 and ten != 1:
        return " " + orders[order][0] + " "  # тысяча, миллион
    if unit in range(2, 5) and ten != 1:
        return " " + orders[order][1] + " "  # тысячи, миллиона
    else:
        return " " + orders[order][2] + " "  # тысяч, миллионов


if __name__ == '__main__':
    number = 10582394624
    number_array = number_to_array(number)
    res_string = convert_to_string(number_array)
    print(res_string)
    print(number_array)
