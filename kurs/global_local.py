#global scope
x = "global x" 

def function():
    #local scope
    x = "local x"
    print(x)

print(x)
function() # x i fonksiyon içinde tanımladın ve
           #sorgulandığında ilk o fonks. kapsamında arar ve bulursa o x'i yazdırır
           #eğer bulamzsa global alana çıkar ve ordan bulunca yazdırır


#####################
#global
name = "Çınar"

def changeName(new_name):
    #local
    name = new_name # name fonks.içinde globalden başka değişken
    print(name)

changeName('SILA')
print(name)


################################
name = "global string"

def greeting ():
    #name = "Çınar"

    def hello():
        #name = "Ada"
        print("Hello " +name)

    hello()

greeting()


########################

x =50

def test(x):
    print(f"x : {x}")

    x = 100
    print(f'changed x to {x}')

test(x)
print(x)


############################################

x =50

def test():
    global x
    print(f"x : {x}")

    x = 100
    print(f'changed x to {x}')

test()
print(x) #100 fonk. içinde global x e yaptığımız her işlem dışarıda da etkiler