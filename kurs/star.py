# yıldız bir karekter dizisini öğelerine ayırıp he birini ayrı karakter olarak görür.
#yıldız işaretini birden fazla parametre alan fonksiyonlar için kullanabilirsin.
#Mesela len() fonksioynu tek bir parametreyi ele alıp kaç elemanlı olduğunu verir.type() ve open() da aynı şekilde
print(*"GALATASARAY")

#len("sıla","çatak") #TypeError: len() takes exactly one argument (2 given)  hatası verir.

#len(*"GALATASARAY") #TypeError: len() takes exactly one argument (11 given) 
#burda yıldız karakter dizisini ayırıp her birini ayrı bir karakter diizisi yaptı .len de sadece bir karakter dizisini ele alır


print(*"GALATASARAY", sep=".")
print(*"GALATASARAY",sep=" ")
print(*"abcçdefgğh",sep="/")

# print(* 12345) #TypeError: print() argument after * must be an iterable, not int
