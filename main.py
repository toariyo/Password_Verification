def introduction(name):
        print("Hello {}. Your password must contain one uppercase letter, one lowercase letter, "
              "atleast one digit, and atleast 8 characters.".format(name))
        return name
def rules(password):
        rules = [lambda password: any(x.isupper() for x in password), # One uppercase condition
        lambda password: any(x.islower() for x in password),  # One lowercase condition
        lambda password: any(x.isdigit() for x in password),  # One digit condition
        lambda password: len(password) >= 8                   # 8 character condition
        ]
        if all(rule(password) for rule in rules):
                print("Your password:{} is verified.".format(password))
        else:
                print("Your password:{} is invalid. Try again.".format(password))

name = input("What is your name? ")
introduction(name)
password = input("What is your password? ")
rules(password)