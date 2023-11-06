def swapVariables():
    var1 = int(input('Enter Your First Variable Value: '))
    var2 = int(input('Enter Your Second Variable Value: '))

    print('\n')
    print('Your Variabl 1:', var1)
    print('Your Variable 2:', var2)
    print('\n')

    temp = var1
    var1 = var2
    var2 = temp

    print('**************After Swapping***************')
    print('Variable 1:', var1)
    print('Variable 2:', var2)
    
swapVariables()
