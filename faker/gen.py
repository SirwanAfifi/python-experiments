import json
import random
import secrets
import users

def generate_users(list, scale = 2):
    users = []
    for _ in range(scale):
        first_name = random.choice(list)
        newUser = {
            'name': first_name,
            'email': str.lower(first_name) + "@python.com",
            'password': secrets.token_urlsafe(8),
        }
        users.append(newUser)
    return users

def generate_tax_data(list, scale = 2):
    # Generate Random people and their tax information
    people = []
    for _ in range(scale):
        tax_rate = random.randint(0, 100)
        amount = random.randint(3000, 6000000)
        newPerson = {
            'name': random.choice(list),
            'tax_rate': tax_rate,
            'amount': int(amount + (amount * (tax_rate / 100))),
        }
        people.append(newPerson)
    # print(json.dumps(people, indent=4))
    return people

type = int(input("Users or Tax Data?\n 1) Users \n 2) Tax Data\n Enter 1 or 2: "))
scale = int(input("How many people would you like to generate? "))

if type == 1:
    print(json.dumps(generate_users(users.names, scale), indent=4))
elif type == 2:
    print(json.dumps(generate_tax_data(users.names, scale), indent=4))


