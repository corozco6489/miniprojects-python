import random
def PasswordGenerator():

    #define strings 
    lower='abcdefghijklmnopqrstuvwxyz'
    upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number='0123456789'
    special='!@$%&*'
    password=''

    password= random.choice(lower)+random.choice(upper)+random.choice(special)+random.choice(number)
    for i in range(2):
        password= password + random.choice(lower)+random.choice(upper)+random.choice(special)+random.choice(number)
    return password

print(PasswordGenerator())