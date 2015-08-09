#declare class
class Animal:
    def __init__(self,name):
        self.name=name    
    def move(self):
        print "i am moving"
    def breathe(self):
        print "i am breathing"
    def my_name(self):
        print "my name is {}".format(self.name)

class Reptile(Animal):
    def cold_blooded(self):
        print "i am cold blooded"

class Amphibian(Animal):
    def living_in_two_world(self):
        print "i am living in water and on land"

class Fish(Animal):
    def fins(self):
        print "i have fins"

class Bird(Animal):
    def wings(self):
        print "i have wings"



    
