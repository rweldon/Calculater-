
operation = input("Please type in the math operation you would like to complete")


number_1 = int(input("Please enter the first number: "))


number_2 = int(input("Please enter the second number: "))


if operation == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

elif operation == '-':
    print('{}-{}='.format(number_1,number_2))
    print(number_1-number_2)

elif operation == '*':
    print('{}*{}='.format(number_1,number_2))
    print(number_1*number_2)

elif operation == '/':
    print('{}/{}='.format(number_1,number_2))
    print(number_1/number_2)

else:
    print('You have not types a valid operator, goodbye')
