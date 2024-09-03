num=int(input("enter number"))#153

orginal=num

total=0

digital_count=len(str(num))

while(num !=0):

    digit=num%10

    exponenet=digit**digital_count

    total=total+exponenet 

    num=num//10#0

print(total)

print("armstrong number" if orginal==total else "not armstrong")