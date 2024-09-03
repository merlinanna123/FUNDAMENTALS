#variable name 
#first char must be an alphabet=> k to m 
#second letter must be number that is \ by 3
#followed by any number of alphabets and numbers @


from re import fullmatch
variable_name=input("enter variable name :")
pattern="[k-m][369][a-zA-Z@]*"
matcher=fullmatch(pattern,variable_name)
print("invalid" if matcher == None else "valid")