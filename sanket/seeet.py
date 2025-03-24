a={2,5,3.5,True,6,7}
print("a==",a)

print(type(a))

a.add(65876)
print("a==",a)

a.discard(6)
print("a==",a)

maxi= max(a)
mini= min(a)
print("max",maxi)
print("min",mini)

length=len(a)
print("length",length)

b={4,5,87,2,True,False}
c=a.union(b)
print("c==",c)
d=a.intersection(b)
print("d==",d)
e=a.difference(b)
print("e==",e)
f=a.symmetric_difference(b)
print("f==",f)
