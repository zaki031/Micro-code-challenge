#roman numbers dictionary
roman_map = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1
}

def num_to_roman(num):
    #Convert an integer to Roman numbers
    roman_numeral = ''
    for roman, value in roman_map.items():
        while num >= value:
            roman_numeral += roman
            num -= value
    return roman_numeral

def roman_to_num(roman_numeral):
    #Convert Roman numbers to an integer
    num = 0
    prev_value = 0
    for roman in reversed(roman_numeral):
        value = roman_map[roman]
        if value < prev_value:
            num -= value
        else:
            num += value
        prev_value = value
    return num


j = input().split(" since ")
num = int(j[0])
roman = num_to_roman(num)




date = ''
for i in j[1].split('/'):
    date+=str(roman_to_num(i))+'/'





print(roman, 'since', date[:-1])
