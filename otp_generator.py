import random
import string
import math
def otp(sample,len):
    pass1=""
    getotp=random.sample(sample,len)
    password=(pass1.join(getotp))
    return password
         
     
    
    
    
numbers = "0123456789"    
symbols = "!@#$%^&*"
letters = string.ascii_letters
sample = numbers + symbols + letters
print(len(sample))
n=int(input('enter the length: '))
print(otp(sample,n))
