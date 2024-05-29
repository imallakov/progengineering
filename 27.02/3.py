def roman(one, two):
    three = one + two

    roman_numerals = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
        90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
    }

    def to_roman(num):
        result = ''
        for value, numeral in sorted(roman_numerals.items(), reverse=True):
            while num >= value:
                result += numeral
                num -= value
        return result

    roman_one = to_roman(one)
    roman_two = to_roman(two)
    roman_three = to_roman(three)

    print(f"{roman_one} + {roman_two} = {roman_three}")


# Пример использования функции
one = 5
two = 4
roman(one, two)
