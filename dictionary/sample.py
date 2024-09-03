#dict={key:value}
student={"name":"sukumar","course":"fullstack"}
#<class dict>:collection of a elements as a key:value pair
#print(student["name"])
#print(student.keys())           #key should be aunique
#student["name"]="hari" 
#student['place'] ="chennai"  #overwrites the value if the key is present else add  as a new pair
#new=student.items()
#print(new)

for i in student:
  print(student)


# update the course as fullstack in students in itteration
student={"course":"fullstack"}
for i in student:
     if i=="course":
         student[i]
print(student)

#delete a key "place" if it person in the dict using iteration

for i in (student):
    print(i)
    if i=="place":
       new=student.pop(i)
print(new)



