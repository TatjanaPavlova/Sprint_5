import random
from faker import Faker

faker = Faker()

def generate_registration_data():
    name = faker.first_name()
    email = faker.email()
    password_length = random.randint(6, 12)
    password = faker.password(length=password_length, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return name, email, password

def generate_registration_data_with_short_password():
    name = faker.first_name()
    email = faker.email()
    short_password = faker.password(length=5, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return name, email, short_password