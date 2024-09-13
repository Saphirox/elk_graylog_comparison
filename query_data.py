from flask import Flask, jsonify
import pymysql
import random

app = Flask(__name__)

# Database connection details
DB_CONFIG = {
    'host': 'localhost',  # Replace with your database host
    'user': 'root',  # Replace with your database username
    'password': 'changeme',  # Replace with your database password
    'database': 'changeme',  # Replace with your database name
    'cursorclass': pymysql.cursors.DictCursor
}


# GET endpoint to retrieve employees with random salary filter
@app.route('/employees', methods=['GET'])
def get_employees():
    # Generate a random salary value
    random_salary = round(random.uniform(30000, 120000), 2)

    # Create a SQL query
    sql_query = "SELECT * FROM employees WHERE salary = %s LIMIT 1"

    try:
        # Establish a database connection
        connection = pymysql.connect(**DB_CONFIG)

        with connection.cursor() as cursor:
            # Execute the query with the random salary filter
            cursor.execute(sql_query, (random_salary,))

        # Close the database connection
        connection.close()

        # Return the result as JSON
        return jsonify(cursor.fetchall())
    except Exception as e:
        # Handle errors and return a meaningful message
        return jsonify({'error': str(e)}), 500


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=8345)
