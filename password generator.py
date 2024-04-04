# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 20:43:37 2024

@author: aisha
"""

import random
import string 

def password_generator(length: int = 15): 
    alphabet = string.ascii_letters + string.digits + string.punctuation #concatenates letters, numbers, and symbols to create the new password
    password = ''.join(random.choice(alphabet) for i in range(length)) #chooses randomly from the ascii library to create password using set length
    return password

password = password_generator()
print(f"Your generated password is: {password}") #prints generated password