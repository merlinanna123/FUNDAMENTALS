class student:
    name:str
    id:int
    gender:str
    age:int
    course:str
    contact:str
    addres:str
    def set_student(self,id,name,gender,age,course,contact,addres):
        self.id=id
        self.name=name
        self.gender=gender
        self.age=age
        self.course=course
        self.contact=contact
        self.addres=addres
    def display_student(self):


        print(self.id,self.name,self.gender,self.age,self.course,self.contact,self.addres)
        student_instance=student()
        student_instance.set_student(100,"hari","male",24,"django",)
        student_instance.display_student()