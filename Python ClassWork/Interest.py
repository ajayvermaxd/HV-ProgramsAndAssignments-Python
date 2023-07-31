# #calculate the simple interest of a principle amount 
# #second- dont run the program if principal amount is less than or equal to zero and time is less than or equal to zero


# PrincipleAmount= int (input("enter the principle amount of your loan-  ")) 
# RateofInterest= 5 #(5% interest)
# LoanDuration= int (input("enter the years of loan you want to take-  "))
# SimpleInterst=(PrincipleAmount*LoanDuration*RateofInterest)/100
# print("Simple interest on the loan is",SimpleInterst) #it will print the simple interest 
# Amount=PrincipleAmount*(1+(LoanDuration*RateofInterest))
# print("Total amount to be paid after completing the loan-  ",Amount) #it will print the total amount to be paid including principle and interest. 



#now the second part with validation that the principal amount and time duration cannot be zero or negative

PrincipleAmount= int (input("enter the principle amount of your loan-  ")) 
RateofInterest= 5 #(5% interest)
LoanDuration= int (input("enter the years for the loan you want to take-  "))
SimpleInterst=(PrincipleAmount*LoanDuration*RateofInterest)/100
Amount=PrincipleAmount*(1+(LoanDuration*RateofInterest))

if(PrincipleAmount<=0):
    print("The principal amount can not be negative or zero")
elif(LoanDuration<=0):
    print("Time duration for the loan cannot be zero or negative")
else:
    print()
    print("Simple interest on the loan is",SimpleInterst)
    print() #it will print single line 
    print("Total amount to be paid after completing the loan-  ",Amount)