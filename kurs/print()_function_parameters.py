#sep
print("T","C")  #print kendi özelliği aralrına boşluk atar biz görmesek bile kendi içinde sep fonksiyonunu kullanmıştır
               # yani sep(" ") şeklinde 

print("T","C", sep=".")

print("bir","iki","üç","dört","on dört" ,sep=" "+ "mumdur"+" ")

print("a","b",sep=None) # none boşluk olarak cevap verir
"""
sep fonksiyonunun karşılığı sepatator(ayırıcı,ayraç) parametrelr arasına bi değerinin yerleştirilmesini sağlar.
karakter dizilerin son kısmıyla ilgilenmez
"""

# end
print("birinci satır","ikinci satır","üçüncü satır",sep="\n")
# end fonksiyonu parametrenin sonuna işlem yapar

print("Bugün günlerden Salı",end=".\n") #gördğünüz gibi sonunda işlem yaptı ve nokta koydu

print("bir","iki","üç","dört", end="     mumdur\n",sep=" mumdur ")


"""  end fonksiyonu da sep gibi sadece none ve string bir değer alabiliir yoksam hata alırsın
>>> print(1, 2, 3, 4, 5, end=0)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: end must be None or a string, not int

"""


#file   #file da end ve sep gibi printin arka kısmında bulunur biz çağırmasak bile

dosya = open("deneme.txt","w")
print("Ben Python,Monty Python", file=dosya)
dosya.close() #işin bittiğinde dosyayı kapatmalsın .Eğer close diyerek kapatmazsan bilgiler flush da yani tampon bölgede bekler.
              #sonuç olarak o dosyayı açtığında hiçbir bilgi göremezsin
 #kurs>deneme.txt dosyasına bak

"""
file nin görevi print() fonksiyonuna verilen karakter dizisi veya sayıların nereye yazılacağını belirlemktir.
bu parametrelerin ön tanımlı değeri sys.stdout tur yani standart çıktı konumudur.Bu çıktıların standart olarak verildiği konumdur.
Etkileşimli kabuk veya komut satırı üzrinde çalışıyorsan buraya çıktı verir
"""


# flush
kisisel_bilgiler = open("kisisel_bilgiler.txt","w")
print("Sıla Çatak", file=kisisel_bilgiler , flush=True)
print("05342608836",file=kisisel_bilgiler, flush=True)
print("Manisa Celal Bayar Üniversitesi Kırkağaç Meslek Yüksekokulu",file=kisisel_bilgiler, flush=True)

# flush ın ön tanımlı değeri false dur biz burda true yaptık ve bilgiler tampon bölgede beklemeden dosyaya aktatırıldı.
#Ve burada dosyayı close diyerek kapatma gereği duyulmadı.