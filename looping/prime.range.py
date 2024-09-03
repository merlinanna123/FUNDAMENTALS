#n (1,n)=>2,,,,,,,,n-1

number=int(input("enter number"))

isprime=True

for i in range(2,number):

   if number%i==0:

     isprime=False

     break
   
print ("is prime" if isprime==True else  "not prime")
