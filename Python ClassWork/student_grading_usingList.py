StudentNameLists=[] #list to store student name
MathMarksLists=[]  #list to store math name
ScienceMarksLists=[]  #list to store Science name
EngMarksLists=[]      #list to store English name
TotalMarksLists=[]   #list to store total marks of students

flag="y"
while(flag =="y"):
     InputName = input ("enter the name of Student ") 
     StudentNameLists.append(InputName)
     mathMarks = int( input("enter maths number"))
     MathMarksLists.append(mathMarks)
     scienceMarks = int(input ("enter sci number "))
     ScienceMarksLists.append(scienceMarks)
     engMarks = int (input ("enter english number "))
     EngMarksLists.append(engMarks)
     totalMarks=(mathMarks+scienceMarks+engMarks)
     TotalMarksLists.append(totalMarks) 
     print ("total marks",totalMarks) #print total marks 
     percentage=(totalMarks/300)*100  #calculate percentage of the marks 
     print(percentage)
     if (percentage<=30):
      print("Useless")
      print("Same on You!")
      print("You are passed the exam")
      print("Congradulation!")
     elif(31<percentage<50):
      print("Grade C")
      print ("you can do better!")
     elif(51<percentage<70):
      print("Grade B ")
      print("Congradulations you are doing good")
     else:
      print("Grade A")
      print("You are Pro")
     flag= input("input if you have another student y/n")
print(StudentNameLists)
print(MathMarksLists)
print(ScienceMarksLists)
print(EngMarksLists)
print(TotalMarksLists)

## lets find out who is topper
topper=0
topperIndex=0
for index in range(0,len(TotalMarksLists),1):
  if(topper<TotalMarksLists[index]):
    topper= TotalMarksLists[index]
    topperIndex=index
print("the topper of the class", StudentNameLists[index])