"""python01-hw-advanced % random password generator. """
import logging
import random
import string


def generate_password(length: int) -> str:
    """
    Generate a random password of a given length.

    The generated password will contain at least one uppercase letter, one lowercase letter,
    one digit, and one special character. The rest of the password is composed of a random
    mixture of these types of characters.

    Parameters:
    length (int): The desired length of the password.

    Returns:
    str: The generated password.
    """
    if length < 4:
        logging.error("Password length should be at least 4")
        return

    # Separate all possible types of characters into different variables
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    # Ensure one character from each type is included
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(num),
        random.choice(symbols),
    ]

    # Fill the rest of the length with random choices from all characters
    all_characters = lower + upper + num + symbols
    for i in range(length - 4):
        password.append(random.choice(all_characters))

    # Shuffle to ensure random order
    random.shuffle(password)

    # Join list elements to form a string
    password = "".join(password)
    return password


if __name__ == "__main__":
    print("Welcome to the Linux User Password Generator!\n")
    while True:
        try:
            password_length = int(input("Please enter the desired password length: "))
            break
        except ValueError:
            print("That's not a valid length, please enter a number.")
    print(f"Generated password: {generate_password(password_length)}")