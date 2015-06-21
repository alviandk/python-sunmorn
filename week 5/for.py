#print 1 2 3 4 5
for loop in range (1,6):
    print loop,
#print "enter"
print "\n"


#print 0 2 4 6 8
for loop in range (0,10,2):
    print loop,
#print "enter"
print "\n"

# print 5 4 3 2 1
for loop in range (5,0,-1):
    print loop,
#print "enter"
print "\n"

# print 20 15 10 5 0

for loop in range (20,-1,-5):
    print loop,
print "\n"

# print word that  user input 5 times use "for"
word=raw_input('word: ')
for loop in range (20,-1,-5):
    print word
print "\n"

# print word that  user input 5 times use "while"
word=raw_input('word: ')
loop=input("how many times? ")
for loop in range (1,loop+1):
    print ("{} {}").format(word,loop)












