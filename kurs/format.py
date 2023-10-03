# format: karakter dizisi birleştirme işlemi yapar

#example.1
url = input("Please Enter the name of site you want to reach:")
print("Error!! Google Chrome couldnt find the {} site".format(url))


#example.2
print("{} and {} are a good duo".format("Python","Django"))

#example.3
sentence = "{} and {} are a good duo"
sentence.format("Python","Django")
loveyou = "{} is love {}"
print(loveyou.format(input("Name:"),input("Name2:")))


#example.3
petition = """
Date:{}

Consulate General of Italy
 
I am {}.I am planning a trip to Italy between {}.I will make this trip with a tour.
During my trip ,I will visit {}.All expenses during the the trip be covered by myself.
You can find it attached all my travel documents.I guaranteeto return to my country on the departure 
date mentioned above and I request that you provide the necesssary visa 
King Regards

ADDRESS:{}
PHONE:{}

"""

Date = input("Date(02.09.2023):")
name_surname = input("Name-Surname:")
Between_date =input("Which between date will You be:")
Location = input("Which city will You trip:")
Address =input("Home address:")
Phone =input("Your phone number:")

print("--------")

print(petition.format(Date,name_surname,Between_date,
                      Location,Address,Phone))