#program to check number is palindrome
 
number=int(input("enter number"))

result=0

orginal=number

while(number!=0):

    digit=number%10

    result=result*10+digit
    
    number=number//10

print("palindrome"if result==orginal else"not palindrome")

