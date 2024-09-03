mobiles=[

    {"id":100,"title":"s23 ultra","brand":"samsung","price":125000,"network":"5g"},
    {"id":101,"title":"s23","brand":"samsung","price":54000,"network":"4g"},
    {"id":102,"title":"edge14pro","brand":"moto","price":25000,"network":"5g"},
    {"id":103,"title":"edgeneo","brand":"moto","price":22000,"network":"4g"},
    {"id":104,"title":"redminote13pro","brand":"mi","price":25000,"network":"5g"},
    {"id":105,"title":"redmi13","brand":"mi","price":12000,"network":"4g"},
]
 
#print all mobile_names
all_mobile_names=[mob.get("title")for mob in mobiles]
print(all_mobile_names)

#print all brands 
all_brands={mob.get("brand") for mob in mobiles}
print(all_brands)

#print samssung mobile names
samsaung_mobile_names=[mob.get("title") for mob in mobiles if mob.get("brand")=="samsung"]
print(samsaung_mobile_names)

#print all mobiles available in range of 23k to 40k
price_filter=[mob.get ("title")for mob in mobiles if mob.get("price") in range(23000,40001)]
print(price_filter)

costly_mobile=[mob.get("title") for mob in mobiles if mob]

def get_price(mob):
    return mob.get("price")
costly_mobile=max(mobiles,key=get_price)
print(costly_mobile)

cheapest_mobile=min(mobiles,key=get_price)
print(cheapest_mobile)

sorted_mobiles=sorted(mobiles,key=get_price,reverse=True)
print(sorted_mobiles)

total_cost=sum([mob.get("price") for mob in mobiles])
print(total_cost)