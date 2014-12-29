#!/usr/bin/python

import os
import time

def arithmetic_func():
    print'''Welcome to the simple_ass_arithmetic_calculator!

    Currently supported operations:
    1) Addition == +
    2) Subtraction == -
    3) Multiplication == *
    4) Division == /

    Also, unsupported input will exit program... So think very hard before you hit enter.'''
    user_input = raw_input('For adding, type (+), for subtraction, type (-), etc.: ')
    if user_input == '+':
        a = int(raw_input('State your first addend: '))
        b = int(raw_input('State your second addend: '))
        print '%d + %d is %d \n' % (a, b, a + b)
        time.sleep(5)
        del a, b
        os.system('cls')
        main()
    elif user_input == '-':
        a = int(raw_input('State your first minuend: '))
        b = int(raw_input('State your second minuend: '))
        print '%d - %d is %d \n' % (a, b, a - b)
        time.sleep(5)
        del a, b
        os.system('cls')
        main()
    elif user_input == '*':
        a = int(raw_input('State your first factor: '))
        b = int(raw_input('State your second factor: '))
        print '%d * %d is %d \n' % (a, b, a * b)
        time.sleep(5)
        del a, b
        os.system('cls')
        main()
    elif user_input == '/':
        a = int(raw_input('State your divisor: '))
        b = int(raw_input('State your dividend: '))
        print '%d * %d is %d \n' % (a, b, a / b)
        time.sleep(5)
        del a, b
        os.system('cls')
        main()
    else:
        quit()

def main():
    user_input = raw_input('What sort of calculation do you wish to make? (1)Arithmetic ')
    if user_input == "1":
        arithmetic_func()
    else:
        quit()

if __name__ == '__main__':
    main()
