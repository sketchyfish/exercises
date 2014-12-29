def main():
    name = raw_input('What is your name? ')
    age = raw_input('What is your age? ')
    f = open('C:\Python27\Myscripts\Dailyprogrammer\exercise1.txt', 'a')
    a = 'Your name is ' + name + ' and you are ' + age + ' years old.'
    f.write(a)
    f.close()

if __name__ == '__main__':
    main()
