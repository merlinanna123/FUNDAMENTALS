#numbers=[1,2,[3,(100,200,300)4]5,6]>>[1,2[3,4,(100,200,300)]5,6]
#numbers=[1,2,[3,(100,200,300),4,],5,6]
#num=numbers[2][1]
#new_num=list(num)
#new_num.insert(1,150)
#numbers[2][1]=tuple(new_num)
#num3=numbers[2]
#poped=num3.pop(2)
#newest=num3.insert(1,poped)
#print(numbers)



number=[3,5,7,1,9,2,0,10,4]          #sorted order= 1,2,3,4,5,7,9,10

smallest_num=number[0]          
secon_smallest=number[-1]        
for i in number:
    if i < secon_smallest and i<smallest_num:  
        secon_smallest=smallest_num
        smallest_num=i
    elif i<secon_smallest and i>smallest_num:   
        secon_smallest=i  
print(secon_smallest)





        