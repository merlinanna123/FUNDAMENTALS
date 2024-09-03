# write a program to check yr is leap year or not


yr=int(input("enter year"))

if (yr%100==0 and yr%400==0) or (yr%100!=0 and yr%4==0):
    print(f"{yr} is leap year")

else:
    print(f"{yr}is not leap year")
    
    