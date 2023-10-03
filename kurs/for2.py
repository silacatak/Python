products= [
 {'name':'samsung a10','price':'3000'},
 {'name':'samsung a11','price':'4000'},
 {'name':'samsung a12','price':'5000'},
 {'name':'samsung a13','price':'6000'}
 ]

#example.1  --> what total is the price of products 
total = 0

for a in products:
   product_price = int(a['price'])
   total +=product_price
   print("TOTAL:",total)


#example.2 --> ürünlerden fiyatı en fazla 5000 olanları sırala
for x in products:
   if int(x['price']) <=5000:
      print(x['name'])