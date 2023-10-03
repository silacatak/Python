# progmamda kullanmak istediğmiz modülün değişken ve fonksiyonunu ilk önce programda dahil edilmesi gerekir.
#yani içeri aktarılması gerekir o modünün bunu import komutuyla yaparız

import os
os.getcwd() # getcwd fonksiyonu  ile o an hangi dzin içinde olduğumuzu buluruz

import keyword
keyword.kwlist  # kwlist() fonksiyonu ile pythonda hangi kelimelern değişken adı olmucağını gösterir

import sys
sys.stdout # Pythonun çıktıları hangi konuma vereceğini belirler

f = open("imports.txt","w")
sys.stdout= f
print("deneme meti" ,flush=True) #standart çıktı konumu imports.txt de oldu çıktıları orada görebilirsin

#standart çıktı konumunu programı kapatmadan eski haline döndürmek için;
import sys
f = open("imports.txt","w")
sys.stdout, f= f ,sys.stdout
print("deneme1",flush=True) # deneme1 imports.txt ye yazıldı
f, sys.stdout = sys.stdout, f #f değerini sys.stdout‘a, sys.stdout‘un değerini ise f‘ye vermiş oluyoruz.böylelikle eski haline döner
# burada yapmak istediğimiz örnek olarak böyle;
#  osman = "Araştırma Geliştirme Müdürü"
# mehmet = "Proje Sorumlusu"
# osman, mehmet = mehmet, osman
print("deneme2")
