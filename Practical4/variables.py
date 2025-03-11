#  4.1  Some simple math
a = 15              #walk to the bus stop
b = 1 * 60 + 15     #take the bus directly to their office
c = a + b           #total length of bus-based commute

d = 1 * 60 + 30     #dive to the nearby car park
e = 5               #walk the final stage
f = d + e           #total length of car-based commute
if c > f:
    print("the bus-based is longer, the car-based is quicker.") 
else:
    print("the car-based is longer, the bus-based is quicker.")       
                    #so the car-based is longer, the bus-based is quicker.

#  4.2  Booleans
X = True
Y = False
W = X and Y
print(W)            #the answer is "False"
                    #W is False, because Y is False.