# excercise
#create game guessing random number use function with return value

from random import randint

def guess_number():
    rand=randint(1,3)
    answer=input("guess a number between 1-3: ")
    while rand!=answer:
        print("wrong try again")
        answer=input("guess a number between 1-3: ")
    print  "correct"
        
guess_number()
