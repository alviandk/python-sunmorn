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

#create instance of Living _Things class   
cathy=Living_Things("cathy")
#access my_name function in Living_Thing class
cathy.my_name()

jon=Living_Things("jon")
jon.my_name()


