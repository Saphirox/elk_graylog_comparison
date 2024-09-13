import mysql.connector
from mysql.connector import Error
from datetime import date, timedelta
import random
import string

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',  # Replace with your MySQL username
    'password': 'changeme',  # Replace with your MySQL password
    'database': 'changeme'
}


# Function to generate random string
def random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length)) + str(random.randint(0, 1000000000))


# Function to generate random email
def random_email():
    return f"{random_string(7)}@example.com"


# Function to generate random date
def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)


# Function to generate random employee data
def generate_employee_data(num_records):
    departments = ['Engineering', 'Marketing', 'Sales', 'Support', 'HR', 'Finance']
    start_date = date(2010, 1, 1)
    end_date = date(2024, 1, 1)

    employees = []
    for _ in range(num_records):
        first_name = random_string(5).capitalize()
        last_name = random_string(7).capitalize()
        email = random_email()
        hire_date = random_date(start_date, end_date)
        salary = round(random.uniform(40000, 120000), 2)
        department = random.choice(departments)
        employees.append((first_name, last_name, email, hire_date, salary, department))

    return employees


# SQL query to insert data
insert_employee_query = """
INSERT INTO employees (first_name, last_name, email, hire_date, salary, department)
VALUES (%s, %s, %s, %s, %s, %s)
"""


def populate_employees_bulk(num_records, batch_size=10000):
    try:
        # Establish a database connection
        connection = mysql.connector.connect(**db_config)

        if connection.is_connected():
            cursor = connection.cursor()

            # Insert records in batches
            for i in range(0, num_records, batch_size):
                batch_data = generate_employee_data(batch_size)
                cursor.executemany(insert_employee_query, batch_data)
                connection.commit()
                print(f"Inserted {i + len(batch_data)} records")

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Close the database connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


if __name__ == "__main__":
    # Populate 1 million records
    populate_employees_bulk(1000000)
