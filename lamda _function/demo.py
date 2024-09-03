add=lambda  n1,n2:n1+n2
print(add(100,200))

sub=lambda n1,n2:n1-n2
print(sub(100,200))

cube=lambda n:n**3
print(cube(3))

max_two=lambda n1,n2:n1 if n1>n2 else n2
print(max_two(100,200))

min_two=lambda n1,n2:n1 if n1<n2 else n2
print(min_two(100,200))

last_digit_max=lambda n1,n2:n1 if n1%10>n2%10 else n2
print(last_digit_max(127,872))

odd_even=lambda n:"even" if n%2==0 else "odd"
print(odd_even(10))