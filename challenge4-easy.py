#!/usr/bin/python

""" 
You're challenge for today is to create a random password generator!
For extra credit, allow the user to specify the amount of passwords to generate.
For even more extra credit, allow the user to specify the length of the strings he wants to generate!
"""

import random

c = int(raw_input("Number of characters? "))
for each_item in range(int(raw_input("How many passwords would you like to make?"))):
    print ''.join(random.sample("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"*k,k))