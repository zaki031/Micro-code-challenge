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
    roman_num = ''
    #looping through the roman_numbers dictionary items
    for roman, value in roman_map.items():
        while num >= value:
            roman_num += roman
            num -= value
    return roman_num

def roman_to_num(roman_numeral):
    #Convert Roman numbers to an integer
    num = 0
    previous_value = 0
    #looping through the reversed roman_numbers dictionary
    for roman in reversed(roman_numeral):
        
        # If the value of the current Roman numeral is less than the previous value,
        # subtract it from the total sum to account for cases like IV (4) or IX (9)
        value = roman_map[roman]
        if value < previous_value:
            num -= value
        # In other cases add it to the total sum
        else:
            num += value
        #update the prev value for next iteration
        previous_value = value
    return num

#spliting the input into a num part and a roman_num part

original_value = input().split(" since ")

#num part
num = int(original_value[0])
#coverting the number to it's roman value
roman = num_to_roman(num)




#roman_num part, splitting it into a DD/MM/YYYY format
rom = original_value[1].split('/')






#Transfering the roman typed date into a normal date
date = ''
for i in rom:
    date+=str(roman_to_num(i))+'/'




#printing the num_to_roman value + the roman_to_num value
print(roman, 'since', date[:-1])
