list_menu=['nasi','ayam']
def menu():
    print "\n\n"
    print "Menu"
    print "1. Show Menu"
    print "2. Input Menu"
    choice=input('what\'s your choice?')
    
    if choice==1:
        out()
        any_key()
        menu()
    elif choice==2:
        inp()
        any_key()
        menu()
    

def out():
    for menu in list_menu:
        print menu

def inp():
    add=raw_input("add a food name: ")
    list_menu.append(add)
    menu()

def any_key():
    key=raw_input("press any key...")

menu()
