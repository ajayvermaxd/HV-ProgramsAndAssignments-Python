# students = ["s1","s2","s3"]

# for details in students:
#     print(details)

    ##
# marks = [67, 78, 89]
# name = input("Enter your name")
# sum = marks[0] + marks[1] + marks[2]
# #print("The name is :- ", name, "and the total marks is :-", (marks[0]+marks[1]+marks[2]))
# print("The name is :- ", name, "and the total marks is :-", sum)

## without doing sum

# marks = [67, 78, 89]
# name = input("Enter your name")
# #sum = marks[0] + marks[1] + marks[2]
# #print("The name is :- ", name, "and the total marks is :-", (marks[0]+marks[1]+marks[2]))
# # print("The name is :- ", name, "and the total marks is :-", sum)
# print("The name is :- ", name, "and the total marks is :-", sum(marks))

##

# #dictionary - key-value pair
# subject_marks = {"maths": 78, "physics": 89, "chemistry": 99}
# # print(subject_marks.keys())
# # print(subject_marks.values())
# # print(subject_marks)

# tm = 0

# for marks in subject_marks.values():
#     tm+=marks

# print("The total marks is :- ", tm)


##

my_dict = {"name": [], "age": []}
# my_dict["name"].append("Anik")
# print(my_dict)

user_input1 = input("Enter the name ")
my_dict["name"].append(user_input1)
# print(my_dict)

user_input2 = int(input("Enter the age "))
my_dict["age"].append(user_input2)
print(my_dict)