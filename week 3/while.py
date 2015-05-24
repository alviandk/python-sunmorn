#print 1 2 3 4 5
loop=1
while loop<6:
    print loop
    loop=loop+1
print ''

# print 5 4 3 2 1
loop=5
while loop>0:
    print loop
    loop=loop-1
print ''

# print word word word word word
word=raw_input('word: ')
loop=5
while loop>0:
    print word
    loop=loop-1

print ''
word=raw_input('word: ')
loop=input("how many times? ")
while loop>0:
    print ("{} {}").format(word,loop)
    loop=loop-1



