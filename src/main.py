from utils import password_length, generate_password


def main():
    print("*-*-*-*-*-*-*-*-*-*-*-*- Welcome to Eigen Vault -*-*-*-*-*-*-*-*-*-*-*-*")

    new_password = generate_password(password_length())
    print(f"New Generated Password:", new_password)


if __name__ == "__main__":
    main()
