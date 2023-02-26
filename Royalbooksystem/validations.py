#Validation Module

from datetime import date

def str_len_validation(str_):
    while True:
        try:
            if len(str_) > 20:
                raise ValueError
        except ValueError:
            print('Error: 20-character limitation')
            str_ = input('Enter again: ')
        else:
            break
    return str_

def digit_validation(digit, f):
    while True:
        try:
            res = int(digit)
        except (ValueError, TypeError):  
            print(f + ' must be a number, No character.\n')
            digit = input('Enter again: ')
        else:
            break
    return res

def date_validation(d):
    while True:
        try:
            res = date.fromisoformat(d)
        except ValueError:
            print('Invalid format(YYYY-MM-DD, 1999-01-01)')
            d = input("Enter again: format(YYYY-MM-DD)")
            continue
        else:
            break
    return res