height_in_cm=int(input("enter height in cm"))

weight_in_kg=int(input("enter height in kg"))

height_in_meter=height_in_cm/100

bmi=weight_in_kg/height_in_meter**2

print(f"bmi={bmi}")

#under weight<19
#normal weight19-25
#over weight25-30
#obese>30

if bmi<=19:#0-19
    print("under weight")
elif bmi <=25:#20-25
    print("normal weight")
elif bmi<=30:#26-30
    print("over weight")
else:
    print("obese")
