#!/usr/bin/python

import os

'''
1)
'''

database_1 = {
    '06am': '',
    '07am': '',
    '08am': '',
    '09am': '',
    '10am': '',
    '11am': '',
    '12am': '',
    '13am': '',
    '14am': '',
    '15am': '',
    '16am': '',
    '17am': '',
    '18am': '',
}

def edit_func():
    edit_key = raw_input("Which time do you wish to edit?:  (format == '17am' or '06am', etc.)")
    edit_key = edit_key.lower()
    edit_value = raw_input('Type in new value: ')
    edit_value = edit_value.lower()
    database_1[edit_key] = edit_value
    print 'Invalid input.  Please try again.\n'
    edit_func()

def add_func():
    user_input = raw_input('Do you want to add a key/value (p)air or just a (v)alue?: ')
    if user_input == 'p' or user_input == 'P':
        add_key = raw_input('Name your key: ')
        add_key = add_key.lower()
        add_value = raw_input('Name your value: ')
        add_value = add_value.lower()
        database_1[add_key] = add_value
    elif user_input == 'v' or user_input == 'V':
        add_key = raw_input('To which key do you wish to append value?: ')
        add_key = add_key.lower()
        add_value = raw_input('Name your value: ')
        add_value = add_value.lower()
        database_1[add_key] = add_value
    else:
        print 'Invalid input.  Please try again.\n'
        add_func()

def remove_func():
    user_input = raw_input('Remove a (k)ey or remove a (v)alue? ')
    if user_input == 'k' or user_input == 'K':
        key_input = raw_input('Which key do you want to remove? ')
        database_1.pop(key_input)
        main()
    elif user_input == 'v' or user_input == 'V':
        key_input = raw_input('Which key? ')
        value_input = raw_input('Which value? ')
        database_1.pop(key_input[value_input])
        main()
    else:
        print 'Invalid input. Please try again.\n'
        remove_func()

def main():
    print '''

    Welcome to your calendar/itinerary thing!

    Your options include the following:

    'l' == list current itinerary
    'e' == edit current itinerary
    'a' == add to itinerary
    'r' == remove an item from the itinerary

    '''
    user_input = raw_input('Type the hot-key and press enter: ')
    while user_input != 'q':
        if user_input == 'l' or user_input == 'L':
            print database_1
            main()
        elif user_input == 'e' or user_input == 'E':
            os.system('cls')
            edit_func()
        elif user_input == 'a' or user_input == 'A':
            os.system('cls')
            add_func()
        elif user_input == 'r' or user_input == 'R':
            os.system('cls')
            remove_func()
        else:
            print 'Exiting program.'
            user_input = 'q'
    else:
        quit()

if __name__ == '__main__':
    main()