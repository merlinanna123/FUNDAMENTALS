#write a program to read student name and 3 marks mark1,mark2,mark3
#and print total mark and average mark

#SET student_name
student_name=input("enter student name")

#SET mark1
hindi_mark=input("enter marks for hindi")

#SET mark2
science_mark=input("enter marks for science")

#SET mark3
malayalam_mark=input("enter marks for malayalam")

#caculate total
total=int(hindi_mark)+int(science_mark)+int(malayalam_mark)

#caculate avg
avg=total/3

print(f"student name {student_name}")

print(f"marks for hindi -{hindi_mark}")

print(f"marks for science -{science_mark}")

print(f" marks for malayalam -{malayalam_mark} ")

print(f"total marks -{total}")

print(f" average  marks {avg}") 
 