word="ihave 2 bike and 1 car"

#print alphabets

for ch in word:

    if ch.isalpha():

        print(ch,end=',')



#print digits
print("\n printing digits")
for ch in word:

    if ch.isdigit():

        print(ch,end=',')