PASSWORD = "Pythonista"


password = input("Enter your password: ")
while len(password) < len(PASSWORD):
    print(f"Password must be at least {len(PASSWORD)} long.")
    password = input("Enter your password: ")
print(f"{'*' * len(PASSWORD)}")
