from mongoconnection import *

client = localmongoconnection()

productdata = mongodatarequest(client, "huwebshopsmall", "products")
firstproduct = firstentry(productdata, "_id", "name")
print(firstproduct)

productdata = mongodatarequest(client, "huwebshopsmall", "products")
firstentry = firstentrywithletter(productdata, "name", "r")
print(firstentry)

productdata = mongodatarequest(client, "huwebshopsmall", "products")
average = averageindoublejson(productdata, "price", "selling_price")
print(average)

