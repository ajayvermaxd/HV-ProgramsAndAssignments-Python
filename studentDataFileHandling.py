import csv

def getStudentData():
    name = input("Enter student's name: ")
    age = input("Enter student's age: ")
    physics = input("Enter marks for Physics: ")
    science = input("Enter marks for Science: ")
    english = input("Enter marks for English: ")

    return name, age, physics, science, english


def writeStudentData(name, age, physics, science, english):
    file = open('students.csv', 'a')
    if file.tell() == 0:
            file.write("Name, Age, Physics, Science, English\n")
    file.write(f"{name},{age},{physics},{science},{english}\n")
    print("Student data saved successfully!")

def getStudentDataFromCSV(student_name):
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip the header row
        for row in reader:
            name, age, physics, science, english = row
            if name == student_name:
                return name, age, physics, science, english
        return None  # If student not found


flag = "y"
while flag == "y":
    name, age, physics, science, english = getStudentData()
    writeStudentData(name, age, physics, science, english)

    flag = input("Do you want to enter data for another student? (y/n): ")

print("Program completed. Please check student.csv")

student_name = input("Do you wish to check data of specific user? write his name: ")
if student_name:
    data = getStudentDataFromCSV(student_name)
    if data:
        name, age, physics, science, english = data
        print("Student Found:")
        print("Name:", name)
        print("Age:", age)
        print("Physics:", physics)
        print("Science:", science)
        print("English:", english)
    else:
        print("Student not found.")