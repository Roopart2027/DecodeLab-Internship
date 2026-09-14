import random
import string

print("===== RANDOM PASSWORD GENERATOR =====")

try:
    length = int(input("Enter password length: "))

    if length < 4:
        print("Password length should be at least 4 characters.")

    else:
        characters = string.ascii_letters + string.digits + string.punctuation

        password = ''.join(random.choice(characters) for i in range(length))

        print("\nYour Generated Password is:")
        print(password)

except ValueError:
    print("Please enter a valid number.")
