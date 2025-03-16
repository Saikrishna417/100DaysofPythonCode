#Math matical Operation is +,-,*,/
print(123+456)
print(7-3)
print(3*2)
print(6/3) #default conversion is float 
print(6//3) #integer divison 
print(2**3) #power of 

#BMI Exercise
#The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight. This is the formula used to calculate it:

#bmi is equal to the person's weight divided by the person's height squared.

height = 1.65
weight = 84
BMI = weight / (height **2)
print(BMI)

#Number manipulation and F string
#int to remove the decimal 
print(int(BMI))
#round 
print(round(BMI))
print(round(BMI,2))
#Assignment operation
#-=,+=,*=,/=

#f string is inserting variable or an expression into a string.
print("BMI is "+str(BMI))

print(f"BMI is {BMI}") # --> f string without converting variable to string for adding

# Project TIP calculator
print("Welcome TIP convertor ")

bill = float(input("Enter the total BILL:? $"))
tip=int(input("What percentage of tip would you like to give ? 10 12 15"))

people = int (input("How mant people to split the bill?"))

bill_with_tip = tip/100 * bill + bill

print(bill_with_tip/people)



