#  5  Triangle sequence

#create a empty varible
#create a loop from 1 to 10 to accumulate the number of dots in the varible.
#print the number of dots every time in the loop.

sum_of_dots = 0                 #create a new empty variable to accumulate the number of dots
for i in range(1, 11):          #i means the thenumber of dots required	to form	the (i)th triangle from (i - 1)th.
    sum_of_dots += i            #accumulate
    print(sum_of_dots)          #output
