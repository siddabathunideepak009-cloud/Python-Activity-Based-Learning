import string

password = input("Enter password to validate: ")
failures = []

if len(password) < 8:
    failures.append("Must contain at least 8 characters.")
if not any(ch.isupper() for ch in password):
    failures.append("Must contain at least one uppercase letter.")
if not any(ch.islower() for ch in password):
    failures.append("Must contain at least one lowercase letter.")
if not any(ch.isdigit() for ch in password):
    failures.append("Must contain at least one digit.")
if not any(ch in string.punctuation for ch in password):
    failures.append("Must contain at least one special character.")
if any(password[i] == password[i + 1] == password[i + 2]
       for i in range(len(password) - 2)):
    failures.append("Must not contain three identical consecutive characters.")
if "password" in password.lower():
    failures.append("Must not contain the prohibited substring 'password'.")

if failures:
    print("Password rejected:")
    for failure in failures:
        print("-", failure)
else:
    print("Password accepted. All policy rules passed.")

