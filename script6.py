password = ''
while password != 'python123':
    password = input("Enter password: ")
    if password == 'python123':
        print('u r logged in')
    else:
        print('wrong, try again')