# Blake Stejskal
# 9/20/2026
# End of Week Assignment - Modlule 4

# Question 1 Definite Loop

start_value = int(input("Please enter your desired start value: "))
end_value = int(input("Please enter your desired end value: "))

# Total and count both start at 0 to be used for later as our constants. 

total = 0
count = 0

# The range() uses end_value + 1 because otherwise it would stop 1 short of the desired end value. 

for num in range(start_value, end_value + 1):
    total += num
    count += 1
# The total keeps increasing while the loop also keeps track of the count. 
# Then just take average and print your deliverables. 

average = total/count

print("Starting value:", start_value)
print("Ending value:", end_value)
print("Sum using for loop:", total)
print("Average using for loop:", average)


# -----------------------------------------------------

# Question 2 Indefinite Loop


scare_count = int(input("How many times would you like to be scared? "))

i = 0

# i = 0 keeps track of how many times the loop has run
# Essentially means, how many Boos have I printed so far?

while i < scare_count:
    print("Boo!!")
    i += 1
    
# The i += 1 just adds 1 to i to make sure it tracks how many times the user has been scared. 