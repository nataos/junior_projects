
def check_number():
    try:
        number = int(input('What number do You think? Beetwen 1 - 1000 '))
        if (number< 1000 and number >0):
            if(number % 2 == 0):
                return('Odd number')
            else:
                return('Even number')
        else:
            return('Out of range')
    except ValueError:
        return('It\'s not a number')


d = check_number()
print(d)
