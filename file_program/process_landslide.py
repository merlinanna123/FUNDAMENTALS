
f=open("C:\\Users\\HELEN VIJU\\OneDrive\\Documents\\OneDrive\\Documents\\PYTHON\\FUNDAMENTALS\\file_program\\land_slide.txt","r")
data=[]
for line in f:#kerala 2018 14
   lst= line.rstrip("\n").split(" ")#["kerala,2018,14"]
   dic={"state":lst[0],"year":lst[1],"death_count":int(lst[2])}
   data.append(dic)
#print(data)


#death_per state
state_summary={}
for dic in data:
   state=dic.get("state")
   death_count=dic.get("death_count")
   if state in state_summary:
       state_summary[state]+=death_count
   else:
      state_summary[state]=death_count
print(state_summary)


#death per year 
year_summary={}
for dic in data:
   year=dic.get("year")
   death_count=dic.get("death_count")
   if year in year_summary:
      year_summary[year]+=death_count
   else:
      year_summary[year]=death_count
print(year_summary)