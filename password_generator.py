# password_generator.py
import random
import string

def generate_password(length=12):
    """Generates a random password of specified length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Main function to take user input and generate a password
if __name__ == "__main__":
    try:
        password_length = int(input("Enter password length: "))
        print("Generated Password:", generate_password(password_length))
    except ValueError:
        print("Please enter a valid number.")
