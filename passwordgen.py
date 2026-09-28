import random
import string

print("=== Password Generator ===")

try:
    length = int(input("Enter password length: "))

    if length < 4:
        print("Password length must be at least 4.")
    else:
        uppercase = string.ascii_uppercase
        lowercase = string.ascii_lowercase
        numbers = string.digits
        special = string.punctuation

        # Ensure at least one character from each category
        password = [
            random.choice(uppercase),
            random.choice(lowercase),
            random.choice(numbers),
            random.choice(special)
        ]

        all_characters = uppercase + lowercase + numbers + special

        # Fill the remaining characters
        for _ in range(length - 4):
            password.append(random.choice(all_characters))

        # Shuffle the password
        random.shuffle(password)

        password = ''.join(password)

        print("Generated Password:", password)

except ValueError:
    print("Invalid input! Please enter a whole number.")