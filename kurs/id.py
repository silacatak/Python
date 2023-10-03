#id
a = "Sıla Çatak"
print(id(a)) # different id for each command run

b=100
print(id(b))

id(1000)

#is --> "is" looks that, object id . not the same  "is it equal" and "is "

a = 100
print(a is 100) # "== " looking at the content, the "is " looks at the identity
print(a== 100)

b = 1000
print(b is 1000)


for k in range(-1000, 1000):
    for v in range(-1000, 1000):
     if k is v:
       print(k) 