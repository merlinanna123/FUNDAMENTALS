num1=int(input("enter num1"))
num2=int(input("enter num2"))
num3=int(input("enter num3"))

if num2>num1>num3 or num3>num1>num2:
    print(f"second largest is num1={num1}")

if num1>num2>num3 or num3>num2>num1:
    print(f"second largest is num2={num2}")

if num1>num3>num2 or num2>num3>num1:
    print(f"second largest is num3={num3}")


