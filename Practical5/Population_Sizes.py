# 2 Population	Sizes	

#the population data list
uk_countries = [57.11, 3.13, 1.91, 5.45]
cn_provinces = [65.77, 41.88, 45.28, 61.27, 85.15]

#sort but not mutate
sort_uk_countries = sorted(uk_countries)
sort_cn_provinces = sorted(cn_provinces)

#print
print("countries in UK: ", sort_uk_countries)
print("Zhejiang neighbouring provinces in China: ", sort_cn_provinces)

#import matplotlib
import matplotlib.pyplot as plt

#the name list
uk_countries_name = ["England", "Wales", "Northern Ireland", "Scotland"]
cn_provinces_name = ["Zhejiang", "Fujian", "Jiangxi", "Anhui", "Jiangsu"]

#explode the center
explode = (0.1, 0, 0 ,0)
explode1 = (0.1, 0, 0, 0, 0)

#create pie chart
plt.pie(uk_countries, explode = explode, labels = uk_countries_name, autopct = "%1.1f%%", shadow = False, startangle = 90)
plt.axis('equal')
plt.title('Population Distribution in UK Countries')
plt.show()


plt.pie(cn_provinces, explode = explode1, labels = cn_provinces_name, autopct = "%1.1f%%", shadow = False, startangle = 90)
plt.axis('equal')
plt.title('Population Distribution in Zhejiang neighbouring provinces in China')
plt.show()
