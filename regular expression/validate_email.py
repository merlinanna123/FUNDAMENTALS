#validate gmaild
# starting with alphanumberic number
from re import fullmatch
pattern="\\w[\\w\\._]*@gmai.com"
gmail_id=input("enter the gmail id: ")
matcher=fullmatch(pattern,gmail_id)
print("invalid" if matcher==None else "valid")

#+ match one or more
#? optional
#*zero or more 