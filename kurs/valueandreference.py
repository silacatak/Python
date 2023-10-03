# value type--> string ,int ----> differet addresses

x = 5 
y = 25

x = y
y = 10
print(x ,y)

#references type -->list  --> after assigning to each other, they use the same address.synchronizing the address information

x =["banana","apple"]
y=["banana","apple"]

x = y 

y[0]= "grape"

print(x ,y)