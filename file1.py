def createFile():
    fileObject = open("Student10.csv", "x")
    data = "name,age,physics,chemistry,english"
    fileObject.write(data)

#################


def userInput():
    name = input("please enter the student name")
    age = input("please enter the age")
    physics = input("Please enter the marks for physics")
    chemistry = input("Please enter the marks for chemistry")
    english = input("Please enter the marks for english")
    data = name+","+age+","+chemistry+","+english
    return data

######


def writeFile(data):
    fileObject = open("Student10.csv", "a")
    data = "\n"+data
    fileObject.write(data)


def readFile():
    fileObject = open("Student10.csv", "r")
    data = fileObject.read()
    print(data)
def userData(username):
    fileobject = open("student10.csv", 'r')
    for line in fileobject:
        stringArray = line.split(",")
        if (stringArray[0] == username):
            print(line)


# if the file do not exist then
# createFile()
data = userInput()
writeFile(data)


ReadFlag = input("Do you want to read the file")
if (ReadFlag == "y"):
    readFile()
    username = input("tell me the name of the user you want to know baout")
    userData(username)