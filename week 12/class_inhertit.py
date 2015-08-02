#declare class
class Living_Things:
    def __init__(self,name):
        self.name=name    
    def move(self):
        print "i am moving"
    def breathe(self):
        print "i am breathing"
    def my_name(self):
        print "my name is {}".format(self.name)

class Human(Living_Things):
    def thinking(self):
        print "i am thinking"

class Cat(Living_Things):
    def climbing_a_roof(self):
        print "i am climbing roof"

#create instance of Human class   
jo=Human("jo")
catro=Cat("catro")
          
jo.move()
catro.move()

jo.thinking()
catro.climbing_a_roof()


