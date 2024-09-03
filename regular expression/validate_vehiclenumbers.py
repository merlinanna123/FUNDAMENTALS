#starting with KL
#two digits
#alphabets(one or two)
#4digits


from re import fullmatch
vehicle_num="KL-08-BN-4970"
pattern="(KL)(-)?[0-9]{2}(-)?[A-Z]{1,2}(-)?[0-9]{4}"   #?atmost
matcher=fullmatch(pattern,vehicle_num)
print("invalid" if matcher==None else "valid")
