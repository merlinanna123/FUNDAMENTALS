#validate_month
#01
#02
#09
#10
#12
from re import fullmatch
month="9"
pattern="(0?[1-9]|[0-2])"
matcher=fullmatch(pattern,month)
print("invalid" if matcher==None else "valid")