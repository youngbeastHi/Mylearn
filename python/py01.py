Anndy = ['Anndy',['age',24]]

Anndy01 = Anndy

Tom = Anndy[:]

Cindy = list(Anndy)

print(id(Anndy))
print(id(Anndy01))
print(id(Tom))
print(id(Cindy))



a = [0,[1,2],3]
b = a[:]
a[0] = 8
a[1][1] = 9
print(a)
print(id(a))
print(b)
print(id(b))


str = 'Cakemaker'

print(str)
print(str[0:9])
print(str[2:5])