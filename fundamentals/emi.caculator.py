#EMI CACULATOR program 
# EMI=p*r*(1+r)**n/(1+r)**n-1
#p=> loan ammount 
#r=>intreset_rate(P.a)=>p.m
#t=>tenure(years)=>months

#SET loan_amount
loan_amount=2000000
#SET interest_rate
intreset_rate=9
#SET tenure
tenure=10

# convert yearly interest rate to monthly intreset rate
r=intreset_rate/12/100

print(r)

n=tenure*12

##EMI=p*r*(1+r)**n/(1+r)**n-1

one_plus_r=(1+r)**n

EMI=(loan_amount*r*one_plus_r)/(one_plus_r-1)

#Totalintersetpayable
 
total_payable_amount=EMI*n

print(f"MONTHLY EMI={EMI}")

print(f"Total payable amount ={total_payable_amount}")

total_interest_payable=total_payable_amount-loan_amount

print(f"Total intreset payable amount ={total_interest_payable}")









