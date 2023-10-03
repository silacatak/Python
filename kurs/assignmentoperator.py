x,y,z = 5,10,15
print(x,y,z)
"""
x *=5
x /=5
x //=5
x %=5
""" 
x **=y

print(x)

values = 1, 2, 3,4,5  # a b c ye birer değer atanır ama sen burda 5 değer vermişsin hata verir(too many values to unpack) bu yüzden a b c den birini dizi haline getirceksin
print(type(values))

a ,b ,*c = values

print(a,b, c)  #1 2 [3,4,5]
print(a,b,c[2]) 
