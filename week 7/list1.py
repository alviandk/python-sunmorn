#create list of "my hobby"
my_hobby=['coding','reading']
print ""
#['coding','reading']
print my_hobby
print ""

# get first element of list 
# use name_of_list followed by[0]
#example:
print my_hobby[0]
print "my first hobby is {}".format(my_hobby[0])
print""

# get how many elements on a list
# use len(name_of_list)
#example:
print len(my_hobby)
print "i have {} hobbies".format(len(my_hobby))
print""

#print all off items on a list
for name_of_variable in my_hobby:
    print name_of_variable
print ""

#adding an item to a list
# use name_of_list.append(item)
hobby=raw_input("input a hobby to be added: ")
my_hobby.append(hobby)
print my_hobby


