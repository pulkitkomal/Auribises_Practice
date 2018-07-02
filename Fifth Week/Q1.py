import re


def email():
    a = input('Enter Email Address(Only Gmail): ')
    at = re.search(r"@", a)
    com = re.search(r"gmail.com", a)

    try:
        if at.group() == '@' and com.group() == 'gmail.com':
            print('Email entered successfully')

    except:
        print('Email Address not valid')


def passwrd():
    password = input('Enter Password(with @ and numbers): ')

    at = re.search(r"@", password)
    num = re.search(r"\d", password)

    try:
        if at.group() == '@' and num.group() == '0' or num.group() == '1' or num.group() == '3'\
                or num.group() == '4' or num.group() == '5' or num.group() == '6' or num.group() == '7' \
                or num.group() == '8' or num.group() == '9':
            print('Valid Password')

    except:
        print('Invalid Password')


def phne():
    phone = input('Enter Mobile number with country code(+91): ')
    if len(phone) == 13:
        ind = re.search(r"91", phone)

        try:
            if ind.group() == '91':
                print('Valid Number')

        except:
            print('Number not valid.')

    else:
        print('Number not valid(Out of index) ')


email()
passwrd()
phne()

