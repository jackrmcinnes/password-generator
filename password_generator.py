# password_generator.py
import random
import string

def generate_password(length=12, include_special_chars=True):
    """Generates a random password of specified length.
    
    Args:
    length (int): The length of the password to be generated (default is 12).
    include_special_chars (bool): Whether to include special characters in the password (default is True).
    
    Returns:
    str: The generated password.
    """
    characters = string.ascii_letters + string.digits
    
    # Include special characters only if the user chose to
    if include_special_chars:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Main function to take user input and generate a password
if __name__ == "__main__":
    try:
        password_length = int(input("Enter password length: "))
        
        # Ask user if they want special characters
        user_input = input("Include special characters? (y/n): ").lower()
        include_special_chars = True if user_input == 'y' else False
        
        # Generate and display the password
        print("Generated Password:", generate_password(password_length, include_special_chars))
        
    except ValueError:
        print("Please enter a valid number.")
