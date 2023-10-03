# Ters taksim (backslah)(\)
print('İstanbul\'un 5 günlük hava durumu tahmini')
print("""İstanbul'un 5 günlük hava durumu tahmini""")
print("Python programlama dilinin adı \"piton\" yılanından gelmez")

#Python bir karakter dizisi tanımladığımızda, karakter dizisini soldan sağa doğru okumaya
# başlar. Mesela yukarıdaki örnekte ilk olarak karakter dizisini tanımlamaya tek tırnakla
# başladığımızı görür ve taramaya devam ederken ilk tırnakta durur ve işlemi bitirir .
#biz burda \ işareti kullanarak senin aradığın tek tırnak bu değil okumaya devam et demiş oluyoruz 
#Böylece çıkacak olark invalid syntax hatsını önüne geçeriz

#başka bir avanatjı
print("Python 1990 yılında Guido Van Rossum \
tarafından geliştirilmeye başlanmış, oldukça \
güçlü ve yetenekli bir programlama dilidir.")

#New line (\n)
title="Python Programlama Dili"
print(title,"\n","-"*len(title),sep="")

#  open("C:\nisan\masraflar.txt")
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# OSError: [Errno 22] Invalid argument: 'C:\nisan\\masraflar.txt'  bu hata \n işaretinden kaynaklı

# iki çözüm vardır .
# 1) ters taksimi çiftlersin--->open("C:\\nisan\\masraflar.txt")--->sorun çıkaran yeri çiflemek yerine tümünü yap
# 2) ters taksim yerine düz taksim kullan-->open("C:/nisan/masraflar.txt") 


# tab(sekme)
print("abc\tdef")
print(*"123456789",sep="\t")


#zil sesi
print("\a"*10)

#aynı satır başı(\r)
print("Merhaba,\rpython") 
# \r fonksiyonu ondan sonra yazan kısmı ,ondan önceki kısmın üstüne yazar.
#python altı harfli ve merhaba yedi harfli a harfinin üstüne yazabilceği bişey kalmadığı için pythona şeklinde çıktı verdi.


#Düşey Sekme(\v)
print("Düşey\v Sekme")

#imleç kaydırma(\b) ---> bu imlecin görevi imleci o an ki konumundan sola kaydrmaktır
print("python","\b","\b.com")
print("istihza\b\b\bsna")

#küçük unicode(\u) unicode:karakterlerin, harflerin, sayıların ve bilgisayar ekranında gördüğümüz
#öteki bütün işaretlerin her biri için tek ve benzersiz bir numaranın tanımlandığı bir sistemdir


print(r"Dosya konumu: C:\users\zeynep\gizli\dosya.txt")
# File "<stdin>", line 1
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in
# position 16-18: truncated \uXXXX escape  --> çözmek için \ yazan yerde çifter halde (\\) kullanmak ya da düz taksim(/) kullan
 # ya da 56.satırda sonradasn denemek için koyduğum r ile de çözebilirsin


