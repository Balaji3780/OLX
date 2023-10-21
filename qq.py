from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)
# Replace with your MySQL database credentials
db_host = "localhost"
db_user = "root"
db_password = "password"
db_name = "ss"
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
def login():   
    if request.method == "POST":
        # Get form data
        USN = request.form["USN"]
        
        # Convert the 'subscribe' checkbox value to BOOLEAN (0 or 1)
        #subscribe = 1 if "subscribe" in request.form else 0

        # Insert form data into the database
        connection = create_connection()
        cursor = connection.cursor()
        sql = "INSERT INTO login(USN) VALUES (%s)"
        values = (USN)
        cursor.execute(sql, values)
        connection.commit()
        connection.close()
        return render_template("frontpage.html")
        # return "Form submitted successfully!"

          
    return render_template("login.html")
@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        # Get form data
        USN = request.form["USN"]
        Name = request.form["Name"]
        Password = request.form["Password"]
        
        # Convert the 'subscribe' checkbox value to BOOLEAN (0 or 1)
        #subscribe = 1 if "subscribe" in request.form else 0

        # Insert form data into the database
        connection = create_connection()
        cursor = connection.cursor()
        sql = "INSERT INTO Registration (Name,USN,Password) VALUES (%s, %s, %s)"
        values = (USN,Name,Password)
        cursor.execute(sql, values)
        connection.commit()
        connection.close()
        return render_template("frontpage.html")
        # return "Form submitted successfully!"
          

    return render_template("registration.html")
@app.route("/frontpage", methods=["GET", "POST"])
def frontpage():
    if request.method == "POST":
        # Get form data
        USN = request.form["USN"]
        Book_Name = request.form["Book_Name"]
        Issued_Date = request.form["Issued_Date"]
        Return_Date = request.form["Return_Date"]
        Returned_Date = request.form["Returned_Date"]
        # Convert the 'subscribe' checkbox value to BOOLEAN (0 or 1)
        #subscribe = 1 if "subscribe" in request.form else 0
        # Insert form data into the database
        connection = create_connection()
        cursor = connection.cursor()
        sql = "INSERT INTO book_issue (USN,Book_Name,Issued_Date,Return_Date,Returned_Date) VALUES (%s, %s, %s, %s, %s)"
        values = (USN,Book_Name,Issued_Date,Return_Date,Returned_Date)
        cursor.execute(sql, values)
        connection.commit()
        connection.close()
        # return render_template("books.html")
        return "book added successfully"

    return render_template("frontpage.html")
@app.route("/books", methods=["GET", "POST"])
def books():
    return render_template('books.html')
@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template('contact.html')
@app.route("/Userdetails", methods=["GET", "POST"])
def Userdetails():
    return render_template('Userdetails.html')
if __name__ == "__main__":
    app.run()