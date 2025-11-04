import secrets
import string


def password_length(min_len=8):
    while True:
        try:
            user_input = int(input(f"Enter Password Length (minimum {min_len}): "))
            if user_input < min_len:
                print(
                    f"Password Length Error: {user_input} is less than minimum required length ({min_len})"
                )
                continue
            return user_input
        except ValueError:
            print("Password Length Error: Please enter a valid number.")


def generate_password(length):
    charset = (
        string.ascii_uppercase
        + string.ascii_lowercase
        + string.digits
        + string.punctuation
    )
    # Include each type at least once
    password = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation),
    ]
    password += [secrets.choice(charset) for _ in range(length - 4)]
    secrets.SystemRandom().shuffle(password)
    return "".join(password)
