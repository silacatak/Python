# kullanıcıdan ad soyad eğitim durumunu isteyip ehliyet alıp alamama durumunu kontorl edizniz.ehliyet alma koşulu en az
#18 yaşında ve ehliyet durumu en az lise veya üniversite olmalıdır.

Name = input("Your name: ")
Surname =input("Your surname: ")
Education_Status = input("Your education statu:")
Age = int(input("Your age:"))

if Age >= 18:
     if (Education_Status=="highSchool") or (Education_Status=="University"):
        print("You passed the conditions for driver's license! :)")
     elif (Education_Status !="highSchool") or (Education_Status != "University"):
       print("Your education status is out of place this condition")
else: 
     print("Unfortunaly")
     