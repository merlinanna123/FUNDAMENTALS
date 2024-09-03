from json import load
f=open("C:\\Users\\HELEN VIJU\\OneDrive\\Documents\\OneDrive\\Documents\\PYTHON\\FUNDAMENTALS\\jsonworks\\countries.json",encoding="UTF-8")
country_data=load(f)
# print(len(country_data))

def fetch_country_by_name(name):
    return [c for c in country_data if c .get("name")==name][0]
data=fetch_country_by_name("India")
#print(data)
    
# 1>>>> find the largest populated country?
def get_population(c):
    return c.get("population")
largest_populated_country=max(country_data,key=get_population)
# print(f"{largest_populated_country.get("name")}:{largest_populated_country.get("population")}")

# 2>>> how many countries are independent?
count=0
for c in country_data:
    if c.get("independent"):
        count+=1
# print(count)

# 3>>> list out the countries in the subregion western asia?
countries_western=[c.get("name")for c in country_data if c.get("subregion")=="Western Asia"]
# print(countries_western)

#4>>> find all countries where the currency  is euro(EUR)and not in the region europe?
def is_euro(c):
    if c.get("currencies")!=None:
        for curr in c.get("currencies"):
            return curr.get("code")=="EUR"
country_currency_filter=[c.get("name") for c in country_data if is_euro(c)and c.get("region")!="Europe"]
# print(country_currency_filter)

#5>>> which countries have more than one official language?
country_language_filter=[c.get("name")for c in country_data if len(c.get("languages"))>1]
#print(country_language_filter)

#6>>> list all countries that share a broder with more than five other countries?
def get_broder_count(c):
    if c.get("borders")!=None:
        return len(c.get("borders"))
    else:
        return 0
country_broder_filter=[c.get("name") for c in country_data if get_broder_count(c)>5]
#print(country_broder_filter)

#7>>> find the country with smallest area?
def get_area(c):
    return c.get("area")if c.get("area")is not None else float("inf")
smallest_country=min(country_data,key=get_area)
# print(smallest_country.get("name"))

#8>>> which countries have a gini index above 40?
countries_gini_filter=[c.get("name")for c in country_data if c.get("gini")!=None and c.get("gini")>40]
#print(countries_gini_filter)

#9>>> biggest country by area?
def get_area(dic):
    if "area" in dic:
     return dic.get("area")
    else:
biggest_country_by_area=max(data,key=get_area)
#print(biggest_country_by_area)


#10>>> largest region by area?
all_regions={c.get("region")for c in data}
print(all_regions)

#11>>>region_summary?
region_summary={}
for c in data:
    region_names=c.get("region")
if region_names in region_summary:
    region_summary[region_names]=+c.get("area",0)
else:
    region_summary[region_names]=c.get("area",0)
print(region_summary)

#12>> maximum  value of region summary?
value_key=[(v,k) for k,v in region_summary.items()]
print(max(value_key))

    