# Generates headings (eg:----Heading----)
def statement_generator(statement,decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Display instructions
def instructions():
    statement_generator("Instructions","-")

    print('''
To use this program simply enter an integer between 
1 and 200.The program will show the factors of your 
chosen integer.

It will also tell you if your chosen number...
- is a prime number (ie: it has two factors)
- is a perfect square

To exit the program, please type 'xxx' .
    ''')


# Ask user for an integer between 1 and 200
def num_check (question):

    error = "Please enter number that is between 1 and 200 inclusive\n "
    while True:
        try:
            response = input(question).lower()
            if response == "xxx":
                return response


            # ask the user for a number
            response = int(response)

            # check that the number is between 1 and 200
            if 1 <= response <= 200:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

# Work out factors, return sorted list
def factor(var_to_factor):


    all_numbers = []
    
    # Square root the number to work out when to stop looping
    stop = to_factor ** 0.5
    stop = int(stop)

    for item in range(1, stop+1):

        # check if number is a factor
        if var_to_factor % item == 0:
            all_numbers.append(item)

    all_numbers.sort()
    return all_numbers



# Main Routine Goes Here

statement_generator("The Ultimate Factor Finder", "-")

# Display instructions if requested
want_instructions = input("Press <enter> to read the instructions"
                          "or any key to continue")

if want_instructions == "":
    instructions()

while True:

    comment = ""

    # ask user for number to be factorised
    to_factor = num_check("\nEnter an integer (or xxx to quit) : ")

    if to_factor == "xxx":
        break
    # get factors for integers that are 2 or more
    elif to_factor != 1:
            all_factors = factor(to_factor )

    #Set up comment for unity
    else:
        all_factors = ""
        comment = "One is UNITY! It only has one factor. Itself :)"

    # comments for squares /primes

    # Prime numbers have only two factors
    if len(all_factors) == 2:
        comment = f"{to_factor} is a prime number"

    # check if the list has an odd number of factors
    elif len(all_factors) % 2 == 1:
        comment = f"{to_factor} is a perfect square"

    # Set up headings
    if to_factor > 1:
        heading = f"Factor of {to_factor}"
    else:
        heading = "One is special..."

    # output factors and comment
    print()
    statement_generator(heading, "*")
    print (all_factors)
    print(comment)

print("Thank you for using the factor calculator")









