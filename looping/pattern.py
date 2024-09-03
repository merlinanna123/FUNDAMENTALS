#1 2 3 4 
#1 2 3 4
#1 2 3 4
for  row  in range(1,4):
     for col in range(1,5):
          print(col,end=" ")
     print()

#1 1 1 1
#2 2 2 2
#3 3 3 3 
for row in range(1,4):
     for col in range(1,5):
        print(col,end="")
     print()

#@ @ @ @ @
#@ @ @ @ @
#@ @ @ @ @
#@ @ @ @ @
for row in range(1,5):
     for col in range(1,6):
          print("@",end=" ")
     print()

# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *
for row in range(1,6):
     for col in range(1,7):
          print("*",end=" ")
     print()

#@
#@ @
#@ @ @
#@ @ @ @
for row in range(1,5):
     for col in range(1,row+1):
          print("@",end=" ")
     print()

#@ @ @ @
#@ @ @
#@ @
#@
for row in range(1,5):
     for col in range(1,6-row):
         print("@",end=" ")
     print()

#@ @ @ @ @ @
#@ @ @ @ @
#@ @ @ @
#@ @ @
#@ @
#@
for row in range(1,7):
     for col in range(1,8-row):
          print("@", end="\t ")
     print()