# range--> "Aralık" anlamına gelir.Python da range() fonksiyonunu belli 
#bir aralıkta ki sayıları göstermek için kullanırız

for i in range(0,20): # 0 dan başla 20. indekse kadar
    print(i)

# #parola belirleme
# while True:
#      parola =(input("Şifre oluşturunuz:"))
#      if not parola:
#          print("Şifre belirlenmeden ilerlenmez!!")
#      elif len(parola) in  range(3,8): #karakter sayısı 3 ile 8 arasında olmalı
#          print("Parolanız oluştu.")
#      else :
#          print("Parola'nız 8 karakten uzun 3 karakterden kısa olmamalı")


#parola giriş
i =0
while i<=2 :
    parola =input("Parola oluşturunuz:")
    if not parola:
        print("Lütfen parola oluşturunuz")
    elif len(parola) in range(3,8):
        print("Parola oluştu.")
        break
    else:
        print("Parola'nız 8 karakten uzun 3 karakterden kısa olmamalı")        
    

parola_gir =parola

    #şifre giriş deneme 
for i in range(3):
    parola_deneme=input("Şifrenizi giriniz:")
    if parola_deneme == True:
      print("Başarıyla giriş yapıldı.")
      break
    if  parola_deneme !=  parola_gir:
          print("Parolayı yanlış girdiniz.")
    elif i ==3: 
     print("Şifreyi 3kez yanlış girdiniz.30 dakika bekleyiniz.")
     break
        



