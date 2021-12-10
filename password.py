import random
n = int(input('Enter the size of the password you need: '))

def PasswordGenerator(n):

    #define strings 
    lower='abcdefghijklmnopqrstuvwxyz'
    upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number='0123456789'
    special='!@$%&*'
    password=''

    for i in range(n):
        l= [random.choice(lower),random.choice(upper),random.choice(special),random.choice(number)]

        password= password + random.choice(l)

    return password

print('Your password random is : ',PasswordGenerator(n))