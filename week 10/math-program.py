def program():
    print "\n"
    print "Math Program"
    print "1. Addition"
    print "2. Substraction"
    print "3. Multilication"
    print "4. Divsion"
    print "5. Exit"
    choice=input('what\'s your choice?')    
    if choice==1:
        print "Addition"
        a=first()
        b=second()
        add(a, b)
        program()
    elif choice==2:
        print "Substraction"
        a=first()
        b=second()
        subtract(a, b)
        program()
    elif choice==3:
        print "Multilication"
        a=first()
        b=second()
        multiply(a, b)
        program()
    elif choice==4:
        print "Divsion"
        a=first()
        b=second()
        divide(a, b)
        program()
    elif choice==5:
        exit()

def add(a, b):
    print "ADDING {} + {} = {}".format(a, b,a + b)
    

def subtract(a, b):
    print "SUBTRACTING {} - {} = {}".format(a, b,a - b)
    

def multiply(a, b):
    print "MULTIPLYING {} * {} = {}" .format(a, b, a * b)
    

def divide(a, b):
    print "DIVIDING {} / {} = {}".format(a, b,a/b)
    

def first():
    inp=input("input first number: ")
    return inp

def second():
    inp=input("input second number: ")
    return inp


program()
