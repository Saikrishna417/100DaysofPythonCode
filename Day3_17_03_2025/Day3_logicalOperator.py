#if condition:
#do this 
#else:
#do this

#Excerise checking the user enter height is more than 120cm then he can ride the rollercoaster else not allowed
'''
height = int(input("Enter your height in cm:"))

if height >= 120:
    print("your allowed to ride")
else:
    print("your not allowed to ride the rollercoaster.")

a= 5
x = a==5
y = a=5

print(x,y)
'''
#Excerise check if user enter number is even or odd using module operator. Module operator will give % returns the reminder of divison
'''
number_to_check = int(input("Enter number want to check:"))

if 0 == number_to_check%2:
    print("Entered number is even number")
else :
    print("Entered number is odd number")
'''

#nested if else condition 
# if condition :
#   if condition :
#      do this
#   else:
#      do this
#else:
# do this
'''
height = int(input("Enter the height in cm?"))

if height >= 120:
    age = int(input("Enter the age:"))
    if age > 18:
        print("Pay 12$ and you can ride the roller coaster")
    elif age >=12 and age < 18:
        print("Pay 7$ and you can ride the roller coaster")
    else:
        print("Pay 5$ and still you can ride")
else:
    print("height is sufficient to ride the roller coaster")
    '''
#Excerise:- Calculate the cost of pizza in the pizza delivery shop
'''
Pizza delivery need to calculate the cost of pizza 
sale person has to ask user 3 question
question 1: - size of pizza : Small (S)- $15 , Medium (M) - $20 , Large (L) - $25
question 2 : Pepproni required or not ? if yes then small pizza is $2 and remaining 2 its $3
question3 :- cheese required or not ? if Yes then $1


Size_of_pizza = input("What size of pizza required for Small(S),Medium (M) and Large is (L)?")
if Size_of_pizza == 'S':
    cost_pizza_based_On_Size = 15
elif Size_of_pizza == 'M':
    cost_pizza_based_On_Size = 20
elif Size_of_pizza =='L':
    cost_pizza_based_On_Size = 25
else:
    print("User Entered wrong pizze size")
    cost_pizza_based_On_Size = 0
pepproni_needed = input("Pepproni is required Yes(Y)/No(N)?")

if pepproni_needed == 'Y':
    if Size_of_pizza == 'S':
        cost_pepproni = 1
    elif Size_of_pizza == 'M' or Size_of_pizza == 'L':
        cost_pepproni = 2
    else:
        cost_pepproni = 0
else:
    cost_pepproni = 0

extra_cheese_needed = input("Extra cheese is required Yes(Y)/No(N)?")

if extra_cheese_needed == 'Y':
    if Size_of_pizza =='S' or Size_of_pizza == ' M' or Size_of_pizza == 'L':
        cost_extracheese = 1
    else:
        cost_extracheese =0
else:
        cost_extracheese = 0

print("total cost of pizza is :", cost_pizza_based_On_Size+cost_pepproni+cost_extracheese ,'$' )
'''


# Logical Operator and,or, not

