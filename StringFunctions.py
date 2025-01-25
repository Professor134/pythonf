#types to create str
str1 ="Hi "
str2 ='I am parth '
str3 ='''Nice to meet you '''

#string function

# 1.str conctination
str4 =str1+str2
print(str4)
print(str1+str2+str3)

# 2.str lenth
l1=len(str1)
print(l1)
print(len(str4))

# 3. slicing
s1="spiderman"
print(s1[0:6]) 
print(s1[6:])
print(s1[-3:])

# 4.endswith
str1 ="I am coder"
str2="I am hero"
print(str1.endswith("der"))
print(str2.endswith("er"))

# 5.capitalize
s1="ironman"
print(s1.capitalize())
print(s1)

#6.replace("old","new")
s1="my fav hero ironman"
print(s1)
print(s1.replace("ironman","spiderman"))

#7.find(str)
s1="moneyhiest"
print(s1.find("money"))
print(s1.find("y"))

#8.count(str)
s1="jay shri ram ,jay shri krishna"
print(s1.count("i"))
print(s1.count("jay"))
