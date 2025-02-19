# ....creating list []
list1=[10,20,30,40,50]
list2=['parth','yesh','shivam','saumya']

# ....access list
print(list1[2])
print(list2[0])
print(list2[1:4])

# ....update list
# ***1.change element
list1[2]=100
print(list1)
list2[1]=100
print(list2)

# ***2.add elements at end
list1.append(60)
print(list1)
list2.extend(['spiderman','thor']) 
print(list2)

# ***3.combine 2 lists using +
list3 = list1 + list2
print(list3)

# ***4.repeat list using *
list3 = list2*2
print(list3)

# ***5.insert at position
list1.insert(2,'hulk')
print(list1)

# ***6.delete by postion
del list1[2]
print(list1)

# ***7.delete by element
list2.remove('saumya')
print(list2)

# ....count 
print(list3.count(100))

# ....sort
print(list1.sort())

# ....reverse
print(list3.reverse())