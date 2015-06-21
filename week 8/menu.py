list_menu=['nasi','ayam']
def program():
    print "\n"
    print "Program"
    print "1. Show Menu"
    print "2. Input Menu"
    print "\n"
    choice=input('what\'s your choice?')
    
    if choice==1:
        out()
        any_key()
        program()
    elif choice==2:
        inp()
        any_key()
        program()
    

def out():
    print "\n\n Our Food Menu"
    idx=0
    for menu in list_menu:
        idx=idx+1
        print "{}.{}".format(idx,menu)

def inp():
    add=raw_input("add a food name: ")
    list_menu.append(add)

def any_key():
    key=raw_input("\npress any key...")
    
    

program()

















