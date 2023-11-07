"""python01-hw-advanced % random password generator. """

import subprocess
import string
import random
import getpass
import pty
import os


def check_user_exists(username):
    try:
        subprocess.check_output(['id', '-u', username])
        return True
    except subprocess.CalledProcessError:
        return False


def create_user(username):
    subprocess.call(['sudo', 'useradd', '-m', username])


def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def check_password_requirements(password):
    requirements = [
        lambda p: len(p) >= 8,
        lambda p: any(c.islower() for c in p),
        lambda p: any(c.isupper() for c in p),
        lambda p: any(c.isdigit() for c in p),
        lambda p: any(c in string.punctuation for c in p)
    ]

    return all(req(password) for req in requirements)


def change_password(username, password):
    master, slave = pty.openpty()
    subprocess.call(['sudo', 'chpasswd'], stdin=slave, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    pty_input = f'{username}:{password}\n'
    os.write(master, pty_input.encode())
    os.close(master)


def main():
    username = input("Enter the username: ")

    if not check_user_exists(username):
        create_user(username)
        print(f"User '{username}' created.")

    password = getpass.getpass("Enter a new password or leave blank to generate one: ")

    if not password:
        password = generate_password()

    meets_requirements = check_password_requirements(password)

    change_password(username, password)

    print(f"Username: {username}")
    print(f"Password: {password}")
    print(f"Meets requirements: {'Yes' if meets_requirements else 'No'}")


if __name__ == '__main__':
    main()
