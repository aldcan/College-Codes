# Aldrian P. Cabaccan
# January 15, 2024
# Asterisk Patterns

# Set number of rows
n = 5
while True:
    while True: 
        try:
# Input prompts
            print("Asterisk pattern selection: \n")
            print("1 - Left sided asterisk pattern")
            print("2 - Right sided asterisk pattern")
            print("3 - Combination of left and right sided pattern")
            print("4 - Exit the program\n")
            pattern_type = float(input("Select the corresponding number of the asterisk pattern: "))
            if pattern_type == 4:
                exit ("Program terminated.")
            elif pattern_type >= 5 or pattern_type <= 0:
                print ("Invalid input. Enter numbers 1 - 4 only.")
            else:
                break
        except ValueError:
            print ("Enter numbers only.")
# Left Asterisk Pattern
    if pattern_type == 1:  
        for i in range(n):
            for j in range(i+1):
                print("*", end="")
            print()
        for i in range(n):
            for j in range(i,n-1):
                print("*", end="")
            print()
# Right Asterisk Pattern
    elif pattern_type == 2: 
        for i in range(n):
            for j in range(i, 4):
                print(" ", end="")
            for k in range(i + 1):
                print("*", end="")
            print()
        for i in range(n-1):
            for j in range (i + 1):
                print(" ", end="")
            for k in range(i, 4):
                print("*", end="")
            print()
# Combination of Right and Left Asterisk Pattern
    elif pattern_type == 3:  
        for i in range(4):
                for j in range(i + 1):
                    print("*", end="")
                for j in range((i % 4) + i, 7):
                    print(" ", end="")
                for j in range(i + 1):
                    print("*", end="")
                print()
        for i in range(4, -1, -1):
                if i == 4:
                    print("*" * 9)
                else:
                    for j in range(i + 1):
                        print("*", end="")
                    for j in range((i % 4) + i, 7):
                        print(" ", end="")
                    for j in range(i + 1):
                        print("*", end="")
                    print()
# Retry loop
    while True:
        retry = input("Do you want to try again? Enter 'yes' or 'no'. ")
        print ("\n")
        if retry.lower() == "yes":
            break
        elif retry.lower() == "no":
            exit ("Program terminated.")
        else:
            print ("Invalid input. Enter 'yes' or 'no' only. ")





