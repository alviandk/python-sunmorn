from random import randint

#create a random suit for computer answer
def enemy(): 
    rand=randint(1,3)
    if rand==1:
        return "rock"
    elif rand==2:
        return "scissor"
    elif rand==3:
        return "paper"

#function result of suite with 2 parameters "player" and "enemy" and give a return value
def suit(player,enemy):
    if player==enemy:
        return "draw"
    if player=="scissor":
        if enemy=="paper":
            return "you win"
        elif enemy=="rock":
            return "you lose"
    elif player=="rock":
        if enemy=="scissor":
            return "you win"
        elif enemy=="paper":
            return "you lose"
    elif player=="paper":
        if enemy=="rock":
            return "you win"
        elif enemy=="scissor":
            return "you lose"

def main_program():
    result_list=[]
    for repeat in range (0,5):
        player=raw_input("what's your choice (paper/rock/scissor): ")
        result=suit(player,enemy())
        result_list.append(result)
        print result
    print "The result of suit are {}".format(result_list)


    
main_program()
