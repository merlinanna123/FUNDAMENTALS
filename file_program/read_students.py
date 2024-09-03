f=open("C:\\Users\\HELEN VIJU\\OneDrive\\Documents\\OneDrive\\Documents\\PYTHON\\FUNDAMENTALS\\file_program\\students.txt","r")
students=[]
for stud in f:
    students.append(stud. rstrip("\n"))
print(students)#["sam\n","ravi\n","ahan\n","bejoy\n"]
