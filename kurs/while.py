sayilar = [1,2,323,21,54,89,00]
#example.1 while döngüsü ile ekrana yazdır sayıları
x = 0
while (x<len(sayilar)):
    print(sayilar[x])
    x+=1

#başlangıç ve bitiş sayıalrını kullnıcıdan al ve arasındaki tüm tek sayıları yazdır
baslangic =int(input("Başlangıç sayısını giriniz:"))
bitis = int(input("Bitiş sayısını giriniz:"))
z = baslangic

while z<bitis:
    if (z%2==1):
      print(z)
    z+=1


#kullancıdan alacağınız 5 rakamı sıralı bir şekilde yazdırınız

number = []
num = 0

while num<=5:
   number.append(int(input("Sayı:")))
   num+=1


number.sort()
print(number)