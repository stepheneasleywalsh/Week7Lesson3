# QUADRATIC SOLVER

#Greet
print("I can solve ax^2 + bx + c = 0 for you!")

# Input Loop
validInput = False
while validInput == False:
    try:
        a = float(input("Please give me the 'a' coefficient: "))
        b = float(input("Please give me the 'b' coefficient: "))
        c = float(input("Please give me the 'c' coefficient: "))
        delta = b**2 - 4*a*c
        if a == 0:
            print("Sorry, but 'a' cannot be zero.")
        elif delta < 0:
            print("Sorry, but that quadratic does not have real roots.")
        else:
            print("Thank you, that is a valid input :) OKAY I'LL SOLVE IT NOW.")
            validInput = True
    except:
        print("That is not real number!")

# Print the Roots or Root
if delta > 0:
    root1 = (-b-delta**0.5)/(2*a)
    root2 = (-b+delta**0.5)/(2*a)
    print("Root 1:", root1)
    print("Root 2:", root2)
else:
    root = (-b) / (2 * a)
    print("Root:", root)

# Quit
quit()