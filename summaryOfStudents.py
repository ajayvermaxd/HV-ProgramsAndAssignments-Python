#create a dictionary name student
# name and mark
#create a list of student
#we need to store the day in a student list from the user and print summery of student
#lists of dictionary

students=[] #list

#taking student number
numStudent = int (input ("enter the number of students"))

#for loop for collecting the data of the student
for i in range(numStudent):
    print("enter the details of the student", (i+1, ":"))

    student={} #directory

    student['name']= input("enter the name of student : ")
    student['marks']= int( input("Enter the marks of student: "))

    students.append(student)

print("Summary of all the student")

#for loop for printing data of the student
for i in range(numStudent):
    student=students[i]
    print("student", (i+1))
    print("Name is ", (student['name']))
    print("Marks is ", (student['marks']))




