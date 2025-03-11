#  7    BMI Calculator

#input weight and height
#calculate BMI
#output BMI
#output health level

weight = float(input("your weight(in kg) is: "))        #input weight
height = float(input("your height(in m) is: "))         #input height
BMI = weight / (height ** 2)                            #calculate BMI

#judge health level
if BMI > 30:
    health_level = 'obese'
elif BMI < 18.5:
    health_level = 'underweight'
else:
    health_level = 'normal'

print("your BMI is "+str(BMI) + ", you are " + str(health_level))    #print BMI and health level
