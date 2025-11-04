from utils import password_length, generate_password


def main():
    print("*-*-*-*-*-*-*-*-*-*-*-*- Welcome to Eigen Vault -*-*-*-*-*-*-*-*-*-*-*-*")

    print("Generated Password:", generate_password(password_length()))


if __name__ == "__main__":
    main()
