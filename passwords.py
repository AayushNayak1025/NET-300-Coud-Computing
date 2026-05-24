password = input("Enter password: ")

special_chars = "!@#$%^&*"

missing = []

if len(password) < 8:
    missing.append("At least 8 characters")

if not any(char.isupper() for char in password):
    missing.append("One uppercase letter")

if not any(char.islower() for char in password):
    missing.append("One lowercase letter")

if not any(char.isdigit() for char in password):
    missing.append("One digit")

if not any(char in special_chars for char in password):
    missing.append("One special character (!@#$%^&*)")

if len(missing) == 0:
    print("Strong Password")
else:
    print("Weak Password")
    print("Missing:")
    
    for item in missing:
        print("-", item)