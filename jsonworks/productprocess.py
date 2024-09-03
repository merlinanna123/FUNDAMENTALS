from json import load
f=open("C:\\Users\\HELEN VIJU\\OneDrive\\Documents\\OneDrive\\Documents\\PYTHON\\FUNDAMENTALS\\jsonworks\\products.json",encoding="UTF-8")
items=load(f)
#print(len(items))

items_title=[i.get("title")for i in items]
#print(items_title)

jewelery_products=[i.get("title")for i in items if i.get("category")== "jewelery"]
#print(jewelery_products)

items_price=[ i.get("title")for i in items if i .get("price")>100]
#print(items_price)

items_range=[ i.get("id") for i in items if i.get("price")>=100 and i.get("price")<=150]
#print(items_range)

#product with most  number of ratings
def get_rating_count(dic):
    return dic.get("rating").get("count")
top_selling_product=max(items,key=get_rating_count)
print(top_selling_product)









