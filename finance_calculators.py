import math

#selection input
print("Choose either 'investment' or 'bond' from the menu below to proceed:")
print(" ")
print("Investment     - to calculate the amount of interest you'll earn on interest")
print("Bond           - to calculate the amount you'll have to pay on a home loan")
fin_option = input("Option (Investment/Bond): ").lower()

#investment input
#calculations

if fin_option == "investment":
    deposit = float(input("Amount being deposited: R"))
    interest_rate = (float(input("What is the interest rate (no % sign required): ")))/100
    years = int(input("Number of years investing: "))
    interest_formulae = input("Simple/compound interest? ").lower()

    if interest_formulae == "simple":
        amount = deposit * (1 + (interest_rate * years))
        amount_round = round(amount, 2)

    if interest_formulae == "compound":
        amount = deposit * (math.pow((1 + interest_rate),years))
        amount_round = round(amount,2)

    print("You will have R" + str(amount_round) , "at the end of" , years , "years.")

#bond input
#calculations

elif fin_option == "bond":
    present_value = float(input("What is the value of the property?: R"))
    interest_rate = (float(input("What is the interest rate (no % sign required): ")))
    months = int(input("Repayment period in months: "))
    #PV ( r ( 1 + r)**n) / (((1 + r)**n) - 1 )
    #Note: tried doing all calculations once off, bodmas issues, had to split all into segments and steps
    interest_rate_p = ((interest_rate/100)/12)
    left_side1 = 1 + interest_rate_p
    left_side2 = left_side1 ** months
    left_side3 = interest_rate_p * left_side2
    right_side = left_side2 - 1
    amount = present_value * (left_side3 / right_side)
    amount_round = round(amount,2)

    print(str(amount_round), "rand per month over a" , months, "month period")