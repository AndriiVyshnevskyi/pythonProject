import random
import string

def generate_password():
    length = 12
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    numbers =  string.digits
    special_characters = string.punctuation

    while True:
        password = random.choices(uppercase_letters, k=1) +\
                   random. choices(lowercase_letters, k=1) +\
                   random.choices(numbers, k=1) +\
                   random.choices(special_characters, k=1) +\
                   random.choices(uppercase_letters + lowercase_letters + numbers + special_characters, k=length-4)
        password = ''.join(random.sample(password, len(password)))
        if (any(char.isupper() for char in password) and
                any(char.islower() for char in password) and
                any(char.isdigit() for char in password) and
                any(char in special_characters for char in password)):
            break
    return password
user_database = {"user1": "password", "user2": "password2"}
print("Welcome to the Linux User Password Generator!")
username = input("please enter your username: ")
if username in user_database:
    print("\nUsername already exist.")
else:
    password = generate_password()
    user_database[username] = password
    print("\nGenerated password for", username, ":", password)