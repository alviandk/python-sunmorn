# for 1-user input lalu tambahkan kondisi FizzBuzz
number_input=input('input ending number: ')
for number in range (1,number_input+1):
    if (number%3 == 0) and (number%5 == 0):
        print 'FizzBuzz'
    elif number%3==0: # "%" means  modulus
        print 'Fizz'
    elif number%5==0:
        print 'Buzz'
    else:
        print number
