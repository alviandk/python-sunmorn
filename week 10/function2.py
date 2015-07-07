#buat contoh
def say_name(name):
    print name
say_name("alvian")

#excercise
def say_name(name):
    print "hallo {}".format(name)

say_name("jon")

#buat contoh
def say_name_age(name,age):
    print "my name is {}, i am {} years old".format(name,age)

say_name_age("Alvian",17)

#excercise
def say_name_age_haha(name,age):
    print "my name is {}, i am {} years old".format(name,age)
    if age>10:
        print "haha too old"
    else:
        print "you still a boy"
say_name_age_haha("De",9)

#excercise
def max(first,second):
    if first==second:
        print "{} and {} are same number".format(first,second)
    elif first>second:
        print "{} is the max number".format(first)
    elif second>first:
        print "{} is the max number".format(second)

max(9,9)
max(10,9)
max(9,10)

#exercise
        # make min function (reverse logic)




