text="ABCCDDBB"

word_count={}#A:1,B:1,C:1

for char in text:#char=A,B,C

     if char in word_count:

         print(char,"first recursive character")

         break

     else:

         word_count[char]=1


