# Blake Stejskal
# 10/3/2026
# Homework 2

# Loan Amortization

# Inputs
loan_amt = int(input("Enter the loan amount:    "))
interest_percent = int(input("Enter the annual interest rate as a percentage:    "))
loan_len = int(input("Enter the length of the loan in years:    "))

annual_interest = interest_percent/100

monthly_rate = annual_interest/12

payments = loan_len*12

monthly_payment = loan_amt*(monthly_rate*(1+monthly_rate)**payments)/(((1+monthly_rate)**payments)-1)
print()

print(f"Monthly Payment: ${monthly_payment:.2f}")


print()
print(f"{'Month':>5} {'Payment':>10} {'Principal':>12} {'Interest':>10} {'Balance':>12}")
print()

# We make the new variable month, and each payment adds one month
# Define interest, principal paid, and balance
for month in range(1, payments + 1):
    interest = loan_amt * monthly_rate
    principal_paid = monthly_payment - interest
    balance = loan_amt - principal_paid

# Print this in f string formatting with the new variables andd the proper formatting indicators. 
    print(f"{month:5} {monthly_payment:10,.2f} {principal_paid:12,.2f} {interest:10,.2f} {balance:12,.2f}")

    # Add this at end of the loop to create the new balance
    principal = balance