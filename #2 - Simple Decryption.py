#**************************************
# Lab #2 Assignment #1: Problem No. 2
# Programmed by: Aldrian P. Cabaccan
# BSCpE 1-3
# Instructor: Engr. Julius S. Cansino
# Date Submitted: March 9, 2024
#**************************************

print("\nProgram Title: Lanum2Assignment #1 | Problem No.2")
print("Programmed by Aldrian P. Cabaccan\n")

# Input prompt for the encrypted text.
encrypted_text = input("Enter num1string to decrypt: ")

# Setting up the characters' corresponding decryption.
decryption = {'*': 'a', '&': 'e', '#': 'i', '+': 'o', '!': 'u'}

# Decrypting the encrypted text to plain text.
for char, decrypt in decryption.items():
    encrypted_text = encrypted_text.replace(char, decrypt)
print("The plain text:", encrypted_text)

