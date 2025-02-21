import random
import string

def generate_password(length=12):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for i in range(length))

    return password

if __name__ == "__main__":
    # Generate a password of length 12
    password = generate_password(12)
    print("Generated password:", password)