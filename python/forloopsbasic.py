#Basic - Print all integers from 0 to 150.

for x in range(0,151,1):
    print(x)

#Multiples of Five - Print all the multiples of 5 from 5 to 1,000

for mult in range(5,1001,5):
    print(mult)

#Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for counting in range(1,101):    
    if counting % 5 == 0:
        print("Coding")
    if counting % 10 ==0:
        print("Coding Dojo")


#Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
for odd in range(0,500001):
    sum=0
    if odd % 2 != 0:
        sum= sum + odd
print(sum)
        

#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for positive in range(2018,0,-4): 
    print(positive)


#Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
for flexible in range(2,200):
    if flexible % 3 == 0:
        print(flexible)