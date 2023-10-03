# kullanıcıdan alacağınız sınırsız ürün bilgisini ürün listesine ekleyin
    #ürün sayısını kullamıcıdan alın
    #dictionary listesinin yapısı(name,price) şeklinde olsun
    #ürün işleme işlemi bittiğinde while ile ekrana yazdır

ürün_sayisi = int(input("Ürünleriniz kaç tanedir:"))
dictionary =[]
i = 0
while i<ürün_sayisi:
        adi = input("Ürün adını giriniz:")
        fiyat =int(input("Ürün fiyatını giriniz :"))
        dictionary.append({
                'Adı':adi,
                'Fiyat':fiyat
        })
        i+=1

print(dictionary)