# for 1-user input lalu tambahkan kondisi FizzBuzz
number_input=input('masukkan angka sampai berapa: ')
for number in range (1,number_input+1):
    if (number%3 == 0) and (number%5 == 0):
        print 'FizzBuzz'
    elif number%3==0:
        print 'Fizz'
    elif number%5==0:
        print 'Buzz'
    else:
        print number
