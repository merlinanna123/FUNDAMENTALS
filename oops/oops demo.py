class employe:
    eid:int
    name:str
    age:int
    gender:str
    department:str
    def set_employee(self,id,name,age,gender,dept):
        self.id=id
        self.name=name
        self.age=age
        self.gender=gender
        self.dept=dept

    def display_employee(self):
        print(self.name,self.id,self.department)