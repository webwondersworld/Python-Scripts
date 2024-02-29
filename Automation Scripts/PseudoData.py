from faker import Faker
from prettytable import PrettyTable
import random

fake = Faker()

def generate_fake_data(num_entries=10):
    data = []

    for _ in range(num_entries):
        entry = {
            "Employee Id": random.randint(1, 100),
            "Name": fake.name(),
            "City": fake.city(),
            "Email": fake.email(),
            "Phone Number": fake.phone_number(),
            "Date of Birth": fake.date_of_birth(minimum_age=18, maximum_age=65).strftime("%Y-%m-%d"),
            "Job Title": fake.job(),
            "Company": fake.company(),
            "Description": fake.text(),
        }
        data.append(entry)
    return data


if __name__ == "__main__":
    num_entries = 10  # You can adjust the number of entries you want to generate
    fake_data = generate_fake_data(num_entries)

    table = PrettyTable()
    table.field_names = ["Employee Id", "Name", "City", "Email", "Phone Number", "Date of Birth", "Job Title",
                         "Company", "Description"]

    for entry in fake_data:
        table.add_row([
            entry["Employee Id"],
            entry["Name"],
            entry["City"],
            entry["Email"],
            entry["Phone Number"],
            entry["Date of Birth"],
            entry["Job Title"],
            entry["Company"],
            entry["Description"]
        ])

    print(table)