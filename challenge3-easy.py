#!/usr/bin/python
"""
Caesar cipher
I want to dig into codecs and see if I can add some complexity (multiple layers)
"""

import codecs
import os



def shift_value():
	moar_input = raw_input('Please input the string you wish to encrypt: ')
	moar_input = moar_input.encode('rot13')
	print moar_input
	raw_input("Press Enter to continue...")

def unshift_value(moar_input):
	moar_input = raw_input('Please input the string you wish to encrypt: ')
	moar_input = moar_input.decode('rot13')
	print moar_input
	raw_input("Press Enter to continue...")

def main():
	os.system('cls')
	moar_input = raw_input('Do you wish to (e)ncrypt, (d)ecrypt, or (q)uit: ')
	if moar_input == 'e':
		a = shift_value()
		print a
	elif moar_input == 'd':
		a = shift_value()
		print a
	elif moar_input == 'q':
		quit()
	else:
		raw_input('Input must be a string.  Press <enter> to continue...')
	main()

if __name__ == '__main__':
	main()