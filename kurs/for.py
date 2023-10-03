sayilar = [1,3,4,2,6,7,8,9,15,23,24]

#soru.1  ---> sayılar listesinden hangi sayılar 3'ün katıdır

for a in sayilar :
     if a%3 == 0 :
         print(a)

#soru.2 ---> sayıları for döngüsünü kullanrak topla

toplam =0
for d  in sayilar :
     toplam+=d
     print(toplam)


# soru.3 ---> sayılar listesinde ki tek olan sayıların karesini al

for c in sayilar:
     if c%2 ==1:
          print("karesi:",c**2)


print("----------------------------------------")

sehirler = ["İstanbul","Ankara","İzmir","Rize","Bolu"]

#soru.4 sehirlerden hangileri en fazla beş karakterlidir ekrana yazdır
for b in sehirler:
    if len(b)<=5:
         print(b)