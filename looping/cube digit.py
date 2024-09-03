#sum of cube of each digit

#input=543

num=int(input("enter the number"))

total=0

while(num!=0):

    digit=num%10

    exponent=digit**3

    total=total+exponent

    num=num//10

print(total)