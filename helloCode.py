def helloCode():
    name_entered = str.upper(input('Enter Your Name: '))
    gender_entered = str.lower(input('Enter Your Gender: '))

    if gender_entered == 'male':
        print('Hello Mr.',name_entered)

    elif gender_entered== 'female':
        print('Hello Miss.',name_entered)

    else:
        print('Invalid!')


helloCode()
