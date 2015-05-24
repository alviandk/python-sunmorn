close="no"
while close != "yes":
    print ("Welcome to my program")
    print ("Menu:") 
    print("1. Calculate area of triangle")
    print("2. Calculate area of square")
    print("3. Calculate area of rectangle")
    choice=input("your choice: ")
    if choice == 1:
        print ("Program to calculate area of triangle")
        base=input("base of triangle: ")
        height=input("height of triangle: ")
        print ("Area of triangle = {}\n".format(base*height/2))
    elif choice == 2:
        print ("Program to calculate area of square")
        side=input("side of square: ")
        print ("Area of square = {}\n".format(side*side))
    elif choice==3:
        print ("Program to calculate area of rectangle")
        width=input("width of rectangle: ")
        height=input("height of rectangle: ")
        print ("Area of rectangle = {}\n".format(width*height))
        
    close=raw_input("close? (yes/no): ")
