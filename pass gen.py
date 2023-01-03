import random 


def pass_gen():

    length = int(input("Enter the desired length: "))
    strength = input("How strong? (poor/okay/good/strong/very strong): ")

    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    number = '12344567890'
    symbol = '!@#$%^&*()_'

    if strength == 'very strong':
        characters = upper + lower + number + symbol
    elif strength == 'strong':
        characters = upper + lower + number
    elif strength == 'okay':
        characters = upper + lower
    elif strength == 'good':
        characters = lower + number
    elif strength == 'poor':
        characters = lower
        
    randomizer = random.sample(characters, length)
    password = ''.join(randomizer)


    print(f'Your password is {password} thank you.')
    

def pass_check():

    password = input("Enter password: ")

    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    number = '12344567890'
    symbol = '!@#$%^&*()_'
    counter = 0
    strength = ''

    for elt in password:
        if elt in lower:
            counter += 0
        if elt in upper:
            counter += 1
        if elt in number:
            counter += 1
        if elt in symbol and counter == 2:
            counter += 2
        

    
    if counter == 0:
        strength = 'poor'
    if counter == 1:
        strength = 'okay'
    if counter == 2:
        strength = 'good'
    if counter == 3:
        strength = 'strong'
    if counter == 4:
        strength = 'very strong'

    print(counter)
    print(f'Your password strength is {strength}')

pass_check()
