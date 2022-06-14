import math


# User to choose which calculator to use - investment or bond.

calc_type = input("Choose either 'investment' or 'bond' from the menu below "
                  "to proceed:\n\n"
                  "investment  - to calculate the amount of interest you'll "
                  "earn on interest\n"
                  "bond        - to calculate the amount you'll have to pay "
                  "on a home loan\n\n")


# Convert user input to lowercase so that the way the user capitilises their 
# selection doesn't affect the program.

calc_type = calc_type.lower()


# User to enter various inputs if investment calculator option chosen.

if calc_type == "investment":
    amount = float(input("How much money are you depositing? "))
    rate = float(input("Please enter the annual interest rate (number of "
                       "interest rate only, exclude the '%' sign): "))
    rate = (rate / 100)
    term = float(input("Number of years you plan on investing for: "))
    interest = input("Would you like simple or compound interest? ")
    
    # Check if user wants simple or compound interest.
    # Use if and elif to calculate answer based on simple or compound input.
    # Also check if user entered incorrect input and display error message.
    
    if interest.lower() == "simple":
        maturity_value = round(amount * (1 + rate * term), 2)
        print("\nAt the end of the term your investment will be worth "
              f"R{maturity_value}.")

    elif interest.lower() == "compound":
        maturity_value = round(amount * math.pow((1 + rate), term), 2)
        print("\nAt the end of the term your investment will be worth "
              f"R{maturity_value}.")

    else:
        print("\nInvalid entry. Please enter 'simple' or 'compound'.")


# User to enter various inputs if bond calculator option chosen.

elif calc_type == "bond":
    house_value = float(input("What is the present value of the house? "))
    rate = float(input("Please enter the annual interest rate (number of "
                       "interest rate only, exclude the '%' sign): "))
    rate = (rate / 100 / 12)  # Convert interest rate to monthly interest rate.
    term = int(input("Number of months you plan to take to repay the bond: "))

    # Calculate monthly bond repayment and print answer.

    repayment = round((rate * house_value) 
                      / (1 - math.pow(1 + rate, (-term))), 2)

    print(f"\nYour monthly bond repayment is R{repayment}.")


# Display error message if user didn't enter 'investment' or 'bond' correctly.

else:
    print("Invalid entry. Please enter 'investment' or 'bond'.")
