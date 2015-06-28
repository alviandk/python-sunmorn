list_menu=['rice','chicken']
def program():
    print "\n"
    print "Program"
    print "1. Show Menu"
    print "2. Input Menu"
    print "3. Delete Menu"
    print "4. Rename Menu"
    print "5. Exit"
    choice=input('what\'s your choice?')    
    if choice==1:
        out()        
    elif choice==2:
        inp()
    elif choice==3:
        delete()
    elif choice==4:
        rename()
    elif choice==5:
        exit()

def out():
    print "\n\n Our Food Menu"
    idx=0
    for menu in list_menu:
        idx=idx+1
        print "{}.{}".format(idx,menu)
    any_key()
    program()

def inp():
    add=raw_input("add a food name: ")
    list_menu.append(add)
    any_key()
    program()

def delete():
    delete=raw_input("delete a food name: ")
    list_menu.remove(delete)
    any_key()
    program()

def any_key():
    key=raw_input("\npress any key...")

def rename():
    rename=raw_input("input a food name to be renamed: ")
    update=list_menu.index(rename)
    list_menu[update]=raw_input("input a new name for {}: ".format(rename))
    any_key()
    program()
program()
