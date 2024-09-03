arr=[6,7,3,4,8,9,10]

#[return iteration condition]

#map..if num>5=> num+1 if num<5=> num-1

#7,8,2,3,9,10,11

mapped_list=[num+1 if num>5 else num-1 for num in arr]

print(mapped_list)


