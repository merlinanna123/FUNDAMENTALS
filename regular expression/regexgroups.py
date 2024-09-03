# from re import finditer
# text="abc123 @k#7LMdef"
# #pattern="[abf]"
# #pattern="[a-k]"
# #pattern="[a-z]"
# #pattern="[A-Z]"
# #pattern="[abc]"
# #pattern="[0-9]"
# #pattern="[a-zA-Z0-9]"
# #pattern="[a-zA-Z]"
# #pattern="[^a-zA-Z]"
# #pattern="[^0-9]"
# #pattern="[^a-zA-Z0-9]"
# #pattern="[\s]"
# #pattern="[^a-zA-Z0-9\s]"
# pattern="[\d]"
# matcher=finditer(pattern,text)
# for m in matcher:
#   print(m.start(),"==",m.group())




from re import finditer
text="abc 7klefg@#"
#pattern="\\D" #space, lower case
#pattern="\\w" #alpha numeric
#pattern="\\d" #digit
#pattern="\\W" #special chara ,space
pattern="\\s"  #space 
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),"==",m.group())