
def cube(num):
    result=num*3
    return result
print(cube(3))
def max_two(n1,n2):
    result=n1 if n1>n2 else n2
    return result
print(max_two(10,20))
def mini_two(n1,n2):
    result=n1 if n1<n2 else n2
    return result


#is_odd
def is_odd(num):
    result=True if  num%2!=0 else False 
    return result
def max_two(n1,n2):
    result=n1 if n1>n2 else n2
    return result
def mini_two(n1,n2):
    result=n1 if n1<n2 else n2
    return result

def is_leap_year(year):

    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:

        return True
    
    else:

        return False
    

print(is_leap_year(2002))



