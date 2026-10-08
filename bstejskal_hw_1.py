# Blake Stejskal

# 9/13/26

# Homework 1

#--------------------------------------------

# Question 1 - Sales Tax Calcultor

price = float(input("How much does the item cost? "))
quant = int(input('How many items are you purchasing? Enter a whole number. '))

subtotal = round((price*quant),2)

tax = round(subtotal * .075, 2)

total = subtotal + tax

print("The subtotal, tax, and total cost are as follows:", subtotal, "$,", tax, "$,", total, "$.")

# Get inputs from the user using the input command, also use float and int to get accurate information. 
# Calculate all the deliverables using the round function. 
#Finally, print the subtotal, tax, and total in a readable format. 

#--------------------------------------------------

# Question 2 - Employee weekly pay calculator

wage = float(input('What is your hourly wage? '))
hours = float(input('How many hours did you work? '))

if hours > 40:
    overtime = hours - 40
    base = 40 * wage
    ot_pay = overtime * wage * 1.5
else:
    base = hours * wage
    ot_pay = 0

total_pay = base + ot_pay

print("Your base pay was:", round(base,2), "your overtime pay was:", round(ot_pay,2), "and your total pay was:", round(total_pay,2))

#Start by getting the inputs for the wage and hours. Simple commands.
#Then create an if statement saying if hours are over 40 it needs to calculate any hours over that 40 threshold differently,
#Add an else statement if it were less than 40
# Create your total pay, and then print all of the various amounts. 


#----------------------------------------------------

# Question 3 - Student Grade Categorizer

number_grade = int(input("What is the grade percentage you received as a whole number? "))

print("Your numeric grade is: ", number_grade)

if number_grade <= 100 and number_grade >= 90:
    print("You received an A!")
elif number_grade <= 89 and number_grade >= 80:
    print("You received a B.")
elif number_grade <= 79 and number_grade >= 70:
    print("You received a C.")
elif number_grade <= 69 and number_grade >= 60:
    print("You received a D...")
elif number_grade <= 59 and number_grade >= 0:
    print("You failed...")
else:
    print("Try entering a different number.")
    
#Start by creating the input for number grade.
# Then just create a string of if and elif statements classifying where each number would land. Using <=, >=, etc. 
#Finish with the 'else' statement in case they enter an unrealistic number. 

#--------------------------------------------------------

# Question 4 - Bonus Eligibility Checker

hours = float(input("How many hours did you work this week?"))
performance = int(input("What was your performance score as a whole number?"))

if hours > 35 and performance > 85:
    print("Congratulations! You have received a $100 bonus for this week.")
elif hours > 35 and performance < 85:
    performance_short = 85 - performance
    print("You are short", performance_short, "performance points to be eligble for a bonus.")
elif hours < 35 and performance > 85:
    hours_short = 35 - hours
    print("You are short", hours_short, "hours to be eligble for a bonus.")
else:
    hours_short = 35 - hours
    performance_short = 85 - performance
    print("You are short", hours_short, "hours and", performance_short, "points on your performance score this week to be eligble for your bonus.")
    
#Start by getting hours and performance inputs
#Then create the if statement for successfully getting your bonus.
#Then create seperate elif statements for both scenarios if you are short one category and not the other. 
#Finish by creating the else statement if they are short in both categories. 