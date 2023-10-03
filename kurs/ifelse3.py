# trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere 
#göre hesaplayanız.
#1.Bakım => 1.yıl
#2.Bakım => 2.yıl
#3.Bakım =>3.yıl
   # süre hesabını alınan gün ay yıl bilgisine göre gün bazlı hesaplayanız
   # datetime modülünü kullan
   # simdi-(2018/8/1) => kullanılma süresi


import datetime

tarih = input("Aracınız trafiğe hangi çıktı (20023/08/29):")
tarih = tarih.split('/')
trafigeCikis =datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now()
fark = simdi-trafigeCikis
days= fark.days

if days<=365:
    print("1.servis aralığı")
elif days>365 and days<=365*2:
    print("2.servis aralığı")
elif days > 365*2 and days<=365*3:
    print("3.servis aralığı")
else:
    print("Hata oluştu...")