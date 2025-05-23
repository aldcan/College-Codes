#**************************************
# Lab #2 Assignment #1: Problem No. 1
# Programmed by: Aldrian P. Cabaccan
# BSCpE 1-3
# Instructor: Engr. Julius S. Cansino
# Date Submitted: March 9, 2024
#**************************************

print("\nProgram Title: Lanum2Assignment #1 | Problem No.1")
print("Programmed by Aldrian P. Cabaccan\n")

# Input prompt for the plain text.
plain_text = input("Enter num1string to encrypt: ")

# Setting up the characters' corresponding encryption.
encryption = {'a': '*', 'e': '&', 'i': '#', 'o': '+', 'u': '!'}

# Converting the plain text to encrypted text.
for char, encrypt in encryption.items():
    plain_text = plain_text.replace(char, encrypt)
print("Encrypted string:", plain_text)

