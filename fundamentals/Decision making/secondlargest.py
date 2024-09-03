num1=int(input("enter the num1"))
num2=int(input("enter the num2"))
num3=int(input("enter the num3"))
#num3 maximum
if num1>num2 and num1>num3:
    #num1 is largest
    # possibly 4 second largest num2 or num3
    if num2>num3:
       print(f"second largest number is num2={num2}")
       #num1,num2,num3 
    else:
       print(f"second largest number is num 3={num3}")
    #num1,num3,num2

if num2>num1 and num2>num3:
    #maximum number num2 
    #possibly 4 second largest num1 or num3
    if num1>num3:
       print(f"second largest number is  num1={num1}")
        #num2,num1,num3
    else:
        print(f"second largest number is num3={num3}")
        #num2,num3,num1

        
if num3>num1 and num3>num2:
    #maximum number num3
    #possibly 4 second largest num1 or num2
    if num1>num2:
        print(f"second largest number is num1={num1}")
        #num3,num1,num2
    else:
        print(f"second largest number is num2={num2}")
        #num3,num2,num1

if num1==num2==num3:
    print(f"three numbers are equal")