def createfile():
 fileObject=open("students.csv", "x")
 data = "name,age,phy,eng"
 fileObject.write(data)


###

def userInput():
 name= input ("Enter name ")
 age= int (input("enter age "))
 phy= int (input("enter phy "))
 eng= int (input("enter eng "))
 data= name,",",age,",",phy,",",eng
 return data


def WriteFile(data):

 fileObject=open("students.csv", "a")
 data="\n"
 fileObject.write(data)

#  fileObject.close()
# createfile()
data = userInput()
WriteFile(data)

def ReadFile():

 fileObject=open("students.csv","r")
#  data=fileObject.readline()
 data=fileObject.read()
 print(data)
