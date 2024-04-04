import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    special_char_error = re.search(r"[!@#$%^&*()_+{}\[\]:;<>,.?/~`]", password) is None
    
    errors = [length_error, digit_error, uppercase_error, lowercase_error, special_char_error]
    error_types = ["length", "digit", "uppercase", "lowercase", "special character"]

    password_strength = {
        "Very Weak": errors.count(True) >= 3,
        "Weak": errors.count(True) >= 2,
        "Moderate": errors.count(True) >= 1,
        "Strong": errors.count(True) == 0
    }

    feedback = []
    for strength, condition in password_strength.items():
        if condition:
            feedback.append(strength)
    
    if not feedback:
        feedback.append("Very Strong")

    if length_error:
        feedback.append("Password length should be at least 8 characters.")
    if digit_error:
        feedback.append("Password should contain at least one digit.")
    if uppercase_error:
        feedback.append("Password should contain at least one uppercase letter.")
    if lowercase_error:
        feedback.append("Password should contain at least one lowercase letter.")
    if special_char_error:
        feedback.append("Password should contain at least one special character.")

    return ", ".join(feedback)


def main():
    password = input("Enter your password: ")
    strength_feedback = check_password_strength(password)
    print("Password strength:", strength_feedback)


if __name__ == "__main__":
    main()
