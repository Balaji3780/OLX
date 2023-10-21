from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)
# Replace with your MySQL database credentials
db_host = "localhost"
db_user = "root"
db_password = "password"
db_name = "olx"
# Function to establish a database connection
def create_connection():
    return mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
# Route for the form page
@app.route("/", methods=["GET", "POST"])
def loginpage():   
    if request.method == "POST":
        # Get form data
        username = request.form["username"]
        password = request.form["password"]
        
        # Convert the 'subscribe' checkbox value to BOOLEAN (0 or 1)
        #subscribe = 1 if "subscribe" in request.form else 0

        # Insert form data into the database
        connection = create_connection()
        cursor = connection.cursor()
        sql = "INSERT INTO login(username, password) VALUES (%s, %s)"
        values = (username, password)
        cursor.execute(sql, values)
        connection.commit()
        connection.close()
        return render_template("frontpage.html")
        # return "Form submitted successfully!"

          
    return render_template("loginpage.html")
@app.route("/frontpage", methods=["GET", "POST"])
def frontpage():   
    if request.method == "POST":
        # Get form data
        type = request.form["type"]
        make = request.form["make"]
        model = request.form["model"]
        year = request.form["year"]
        price = request.form["price"]
        description = request.form["description"]
        image = request.form["image"]
        # Convert the 'subscribe' checkbox value to BOOLEAN (0 or 1)
        #subscribe = 1 if "subscribe" in request.form else 0

        # Insert form data into the database
        connection = create_connection()
        cursor = connection.cursor()
        sql = "INSERT INTO dataupload(type,make,model,year,price,description,image) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (type, make, model, year, price, description, image)
        cursor.execute(sql, values)
        connection.commit()
        connection.close()
        return "upload successfully"

    return render_template("frontpage.html")
@app.route("/frontpage", methods=["GET", "POST"])
def books():
    return render_template('frontpage.html')


if __name__ == "__main__":
    app.run()