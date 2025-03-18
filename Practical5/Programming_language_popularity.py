# 1 Programming	language popularity

#the language dictionary
language_percentage = {
    'JavaScript': 62.3, 
    'HTML': 52.9, 
    'Python': 51, 
    'SQL': 51, 
    'TypeScript': 38.5
    }
print(language_percentage)  #print

#import numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt

#create two individual list to do the bar chart
languages =list(language_percentage.keys())
percentages = list(language_percentage.values())

#create bar chart
N = 5                                   #5 element
p1 = plt.bar(languages, percentages)    #create bar
plt.xlabel("Languages")                 #x-label
plt.ylabel("Percentages")               #y-label
plt.title("Percentage of developers who use the top 5 programming languages globally as of February 2024")  #title
plt.show()                              #show the bar chart

#The percentage of developers who use one language taken from the input	list
requested_language = 'Python'           
if requested_language in language_percentage:
    print("The percentage of developers who use " + str(requested_language) + " is " + str(language_percentage[requested_language]))
else:
    print(str(requested_language) + " not found")