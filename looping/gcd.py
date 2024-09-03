#gcd of (12,24,)#1,2,3,4,6,12,(12)

#1,,,,,,,12

number1=int(input("enter number 1"))#4

number2=int(input("enter number 2"))#8

gcd=1

for i in range(1,number1+1):#1,2,3,4

    if number1%i==0 and number2%i==0:#4%1==0 and 8%2==0

        gcd=i#2

print(gcd)
