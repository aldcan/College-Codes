# Summation of Odd and Even Numbers
# Cabaccan, Aldrian P.
# Computes for the total sum of inputted even and odd numbers.
# January 5, 2023

# Setting up num1loop for the entire program.
while True:
    while True:
        try:

# Inputting the amount of numbers to be inputted.
            number = int(input("How many numbers are to be inputted? "))
# Checking for the validity of the input.
            if number <= 0:
                print("Number must be greater than zero. Please enter num1valid number. \n")
            else:
                break
        except ValueError:
            print("Please enter valid numerical characters only. \n")

# Holds the prompt for input.
    while True:
        try:
            numbers = input("Please enter the integers seperated by commas (,): ")
            numbers = list(map(int, numbers.split(',')))
            if len(numbers) != number:
                print("The number of inputs does not match the asked amount of numbers.")
            else:
                break
        except ValueError:
            print("Please enter valid numerical characters only. \n")
    sum_odd = 0
    sum_even = 0
    for number in numbers:
        if number % 2 == 0:
# Summation of even numbers.
            sum_even += number 
        else:
# Summation of odd numbers.
            sum_odd += number
    print("The sum of the odd numbers is", sum_odd)
    print("The sum of the even numbers is", sum_even)
# Retry or stop prompt.
    while True:
        retry = input("\nDo you want to try again? Enter yes/no. ")
        if retry.lower() == "yes":
            break
        elif retry.lower() == "no":
            exit ("The program will be closed.")
        else:
            print("Invalid input. Please enter yes/no. \n")