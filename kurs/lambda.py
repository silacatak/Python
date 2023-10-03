# def diyerek oluşturduğumuz fonksiyon yerine bir fonksiyon

#def square(num): return num**2

from asyncore import readwrite


square2 = lambda num: num**2

numbers =[1,4,2,6,5]

#result = list(map(square,numbers))
#result = list(map(lambda num: num**2,numbers))
#result = list(map(square2,numbers))
result2 = square2(6)

print(result2)
#print(result)
#print(result)
#for item in map(square,numbers):
 #   print(item)


 # FİLTER
numbers2 = [3,5,1,6,4,2,8,10]

def check_even(number): return number % 2==0

check_even = lambda num: num %2== 0

#result3 = list(filter(check_even,numbers2))
#result3 = list(filter(lambda num: num % 2== 0,numbers2))
#result3 = list(filter(check_even,numbers2))
#result3 = check_even(7)  # false
result3 = check_even(numbers2[2]) # false, 2. index sorgulanır
print(result3) 