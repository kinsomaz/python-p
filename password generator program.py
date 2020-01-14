#This program is a password generator
import random
c = ('abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*+=<>')
passlen = 8
password = ' '.join(random.sample(c,passlen))
print(password)


