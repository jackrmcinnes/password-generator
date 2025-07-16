import random
import string

def generate_password(length=12, char_type="all"):
    """Generates a random password of specified length and type."""
    if char_type == "letters":
        characters = string.ascii_letters
    elif char_type == "digits":
        characters = string.digits
    elif char_type == "punctuation":
        characters = string.punctuation
    else:
        characters = string.ascii_letters + string.digits + string.punctuation  # All types

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Main function to take user input and generate a password
if __name__ == "__main__":
    try:
        password_length = int(input("Enter password length: "))
        char_type = input("Enter character type (letters/digits/punctuation/all): ").lower()
        print("Generated Password:", generate_password(password_length, char_type))
    except ValueError:
        print("Please enter a valid number.")
