#validate_pan_card_number
#first 3 characters are alphabets 
#4th place PCAFHT
#5th place alphabet
#4 digit
#1 alphabet
#AFZPK7190K
from re import fullmatch
pattern="[a-z]{3}[PCAFHT][A-Z][0-9]{4}[A-Z]"
pan_number=input("enter the pan number :")
matcher=fullmatch(pattern,pan_number)
print("invalid" if matcher==None else"valid")




