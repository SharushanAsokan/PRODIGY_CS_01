print("//////////////////////////////////////////////////////////")
print("            Welcome to Caesar Cipher Program")
print("//////////////////////////////////////////////////////////")
print(" ")

# Gives user the options to choose which Technique to perform
print("Enter '1' for Encryption")
print("Enter '2' for Decryption")

#Taking input and converting it into integer
choice=int(input("Select Which Encryption Technique you desire:"))

# Defined the fixed shift value
shift= 4

# Function for encrypting plain text    
def encrypt(text,shift):
# Empty string to store final encrypted result
    result = ""
# Loop through each character in the input text
    for char in text:
# If the character is an uppercase letter
        if char.isupper():  
# Convert char to its ASCII number using ord()
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
# If the character is a lowercase letter
        elif char.islower():
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
# If the character is not a letter (e.g., space, number, symbol)
        else:  
            result += char
    return result
    
# Function for decrypting cipher text
def decrypt(text,shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            result += char
    return result

# Condition for checking which technique the user chooses
if choice==1:
# Take plain text input     
    plain_text = input("Enter the Plain Text: ")
# Encrypt using function and print the result   
    print("Encrypted Text:", encrypt(plain_text, shift))
    
elif choice==2:
# Take cipher text input     
    cipher_text = input("Enter the Cipher Text: ")
# Decrypt using functions and print the result    
    print("Decrypted Text:", decrypt(cipher_text, shift))
        
# If user entered an invalid choice         
else:
     print("Wrong Choice, Try Again")