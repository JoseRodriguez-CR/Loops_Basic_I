# 1.Basic -  Print all integers from 0 to 150.
for num in range(0, 101):
    print( num)

# 2.Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for num in range(0, 1001):
    if num%5 == 0:
        print( num)

# 3.Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for num in range(1, 101):
    if num%10 == 0:
        print( "Coding Dojo" )
        #print( num)
    elif num%5 == 0:
        print( "Coding" )
        #print( num)
    else:
        print( num)

# 4.Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
num = 0
sum = 0
print(type(num))
for num in range(0, 500000):
    if num % 2 != 0:
        sum = sum + num
        #print( sum )
print( sum )

# 5.Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for num in range(2018, 0, -4):
    print( num)

# 6.Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, 
# print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop 
# should print 3, 6, 9 (on successive lines)
lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum, highNum+1 ):
        if i % mult == 0:
            print( i)