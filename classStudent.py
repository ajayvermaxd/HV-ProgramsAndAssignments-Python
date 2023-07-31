class Student:
    name=""
    marks= ""
    rollNo = ""

    def __init__(self,name,marks,rollNo):
        self.name= name
        self.marks= marks
        self.rollNo=rollNo
        
Studentdetails = Student("Ajay",20,1)
    
print( Studentdetails.name,Studentdetails.marks,Studentdetails.rollNo)