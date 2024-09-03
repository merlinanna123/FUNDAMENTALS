#power range

number=int(input("enter number"))

pattern=0

for i in range(1,number+1):
    
    pattern=pattern*10+number

    print(pattern)

for i in range(1,number+1):

       pattern=pattern*10+number

       print(pattern)

pattern=0

total=0

for i in  range(1,number+1):
       
       pattern=pattern*10+number

       total=total+pattern
      