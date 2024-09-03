
# from re import finditer
# text="hellopyhtonhellopythonhellopython"
# matchers=finditer("python",text)
# count=0
# for m in matchers:
#     print(m.start(),"===",m.group())
# count+=1
# print("total count",count)

from re import finditer
text="ababbaab"
matcher=finditer("ab",text)
count=0
for m in matcher:
    print(m.start(),"==",m.group())
count+=1
print("total count",count)
