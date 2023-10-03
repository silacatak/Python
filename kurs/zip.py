#zip: eşleştirme yapar

list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
list3 =[10,20,30,40,50]

print(list(zip(list1,list2,list3 )))
    
print(*zip(list1,list3))

for item in zip(list1,list3):
    print(item)

for a,b,c in zip(list1,list2,list3):
    print(b)