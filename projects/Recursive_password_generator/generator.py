import random
import string

def stretch(text,maxlength):
    if len(text) >= maxlength:
        return text
    randomChar = get_random_char()
    return stretch(text+randomChar,maxlength)

def get_random_char():
    chars = string.printable
    return chars[random.randint(0,len(chars)-1)]

while 1:
    maxlen = input(' [?] Enter a length for your password (e for exit): ')
    try:
        maxlength = int(maxlen)
        print("'",stretch('',maxlength),"'\n")
    except:
        if maxlen == 'e':
            break
        print('Please Enter an integer')
