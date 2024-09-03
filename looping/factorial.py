num=4
#1*2*3*4

num=5
#1*2*3*4*5

num=int(input("enter number"))#
fact=1

for i in range(1,num+1):
    fact=fact*i
    print(f"{num}!={fact}")