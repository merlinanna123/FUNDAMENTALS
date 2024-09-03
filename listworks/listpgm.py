# numbers=[1,2,[3,[100,200,300,]4]5,6]

# print(numbers[2]) #[3[100, 200,300],4]

# print(numbers[2[1]])#[100,200,300]

# numbers[2][1].append(500)#[100,200,300,500]

# print(numbers)#[1,2,[3,[100,200,300,500]4]5,6]

#wap to swap first and last elments in a list

# num=[1,2,3,4,5,6,7]

# num[-1],num[0]=num[0],num[-1]

# print(num)

#wap to return the odd numbers in a list 
# num=[1,2,3,4,5,6,7,8]
# odd_num=[]
# for i in num :
#     if i%2!=0:
#         odd_num.append(i)
# print(odd_num)

# wap to remove the even numbers from the list 
# num=[1,2,3,4,5,6,7,8]
# for i in num:
#     if i%2==0:
#         num.remove(i)
# print(num)

num=[1,2,2,3,4,5,3,6,4,7]
for i in num:
    if num.count(i)==1:
        print(i)
