number = []
for x in range(10):
    number.append(x)

print(number)

number = [x for x in range(8)]
print(number)

numbers = [x**2 for x in range(6)]
print(numbers)


numbers = [x*x for x in range(4) if x%3 ==0]
print(numbers)

myString = "hello"
myList = []

for letter in myString:
    myList.append(letter)

print(myList)


my_list =[letter for letter in myString]
print(my_list)


print("**************************")

years =[1999,2003,2000,2007]
ages = [2023-year for year in years ]
print(ages)


result = [x if x%2==0 else 'TEK' for x in range(1,10)] # if eğer for dan sonra yazsaydı o döngüye dahildi
print(result)


print("**************************")

numberone = []

for x in range(3):
    for y in range(3):
       numberone.append((x,y))
print(numberone)

numbertwo = [(x,y) for x in range(3) for y in range(3)]