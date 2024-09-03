#print(message)

#input(message)=>str

#len(obj)=>return length of object

#type(obj)=>return data type of object

#range(start,end,step)

i=1

while(i<=10):
   print(i)
   i=i+1

sequence=range(1,11,1)#(1,2,3,4,5,6,7,8,9,10)
for num in sequence:
    print(num)

sequence=range(50,101,1)
for num in sequence:
    print(num)

sequence=range(2,11,2)
for num in sequence:
    print(num)

sequence=range(10,0,-1)
for num in sequence:
    print(num)

#print 1 to 50 using for loop
for num in range(1,51):
    print(num)

#print 1 to 100 using for loop
for num in range(1,101):
    print(num)

#print 1800 to 2024 using for loop
for year in range(1800,2025):
    if year%100==0:
     print(year)
