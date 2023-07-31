studentName = ["Ajay","Vaibhav","Vijay","Jay"]
PhysicsMarks= [10,20,30,40]
ScienceMarks=[50,60,70,80]
#print(studentName[0],"has got",PhysicsMarks[0],"in physics")
#print(studentName[1],"has got",PhysicsMarks[1],"in physics")
#to short the upper print statement we can do it in a loop like
#for index in range (0,4,1):
#    print(studentName[index],"has got",PhysicsMarks[index],"in physics")

    #if we want to check the lenth of the list
#print(len(studentName))

#so we can write
for index in range (0,len(studentName),1):
    print(studentName[index],"has got",PhysicsMarks[index],"in physics")

#validation, if the physics marks of the student is less than 30, print fail. 
    if(PhysicsMarks[index]<30):
     print("Student is fail in Physics")

# so if we want to add something in the list we use append

studentName.append("Drupad")
PhysicsMarks.append(20)
ScienceMarks.append(30)

#now if we have to add something in the list we can use loops to add multiple entries

for index in range(0,len(studentName),1):
   studentName.append("ABC")
   print(studentName)