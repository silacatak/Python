#Girilen sayı 0-100 arasında olup olmadığını kontrol ediniz

number = int(input("Enter A number:"))
result = (number <= 100) and (number >= 0)

if result:
    print ("Truee")
else :
   print("Enter between 0-100 a number")


# User name and password check

Password = int(input("your enters' password have to be number:"))
userName=input("User name:")

enter_username = (input("Enter the User Name repeat:"))
enter_password = int(input("Enter the password repeat:"))

if userName == enter_username :
    if Password == enter_password:
        print("Welcome to the my site")
    else :
        print("Password error,please try again")
else:
    print("please try again")