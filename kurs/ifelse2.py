#bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not ağırlığına 
#karşılık gelen not bilgisini yazdırınız
# 0-24 => 0
# 25-44 => 1
# 45-54 =>2 
# 55-69 =>3
# 70-84 => 4
# 85-100 => 5


exam_one = int(input("Your first exam grade:"))
exam_two =int(input("Your second exam grade:"))
exam_three = int(input("Yours third exam grade:"))
average = (exam_one+exam_two+exam_three)/3
print(average)

if (average>=0) and (average<=24):
    print("Grade average:0")
elif (average>=25) and (average<=44):
       print("Grade average:1")
elif (average>=45) and (average<=54):
       print("Grade average:2")
elif (average>=55) and (average<=69):
       print("Grade average:3")
elif (average>=70) and (average<=84):
       print("Grade average:4")     
else :
   print("Grade average:5")                