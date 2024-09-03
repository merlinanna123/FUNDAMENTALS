number=int(input("enter the number"))
previous=0
current=1
is_fibo=False
if number==0 or number==1:
  is_fibo=True
else:
  next=previous+current
while(next<=number):
  next=previous+current
  if next==number:
    isfibo=True
    break
previous=current
current=next
print(is_fibo)


