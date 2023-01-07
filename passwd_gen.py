import random
import string

def generate_password(length):
    # Create a list of all the possible characters that can be included in the password
    characters = list(string.ascii_letters + string.digits + string.punctuation)
    # Shuffle the characters to ensure a more random password
    random.shuffle(characters)
    # Select the desired number of characters from the list
    password = ''.join(random.choices(characters, k=length))
    return password

# Get the desired password length from the user
length = int(input("Enter the desired password length: "))

# Generate and print the password
password = generate_password(length)
print(password)
