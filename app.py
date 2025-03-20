from flask import Flask, request
import sqlite3
import uuid

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect('drivers.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS drivers (
                        id TEXT PRIMARY KEY,
                        name TEXT,
                        mobile TEXT,
                        email TEXT,
                        address TEXT,
                        license TEXT,
                        issue_date TEXT,
                        expiry_date TEXT,
                        aadhaar TEXT
                    )''')
    conn.commit()
    conn.close()

init_db()

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        driver_id = str(uuid.uuid4())[:8]  # Generate a unique ID
        name = request.form["name"]
        mobile = request.form["mobile"]
        email = request.form["email"]
        address = request.form["address"]
        license = request.form["license"]
        issue_date = request.form["issue_date"]
        expiry_date = request.form["expiry_date"]
        aadhaar = request.form["aadhaar"]

        conn = sqlite3.connect('drivers.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO drivers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                       (driver_id, name, mobile, email, address, license, issue_date, expiry_date, aadhaar))
        conn.commit()
        conn.close()

        return f"Registration Successful! Your Driver ID is {driver_id}"

    return '''
    <html>
    <head>
        <title>Driver Registration</title>
        <style>
            body { font-family: Arial, sans-serif; background-color: #f4f4f4; text-align: center; }
            form { background: white; padding: 20px; border-radius: 10px; width: 300px; margin: auto; }
            label { display: block; margin-top: 10px; }
            input { width: 100%; padding: 8px; margin-top: 5px; border: 1px solid #ccc; border-radius: 5px; }
            button { width: 100%; padding: 10px; background: #28a745; color: white; border: none; border-radius: 5px; margin-top: 15px; cursor: pointer; }
            button:hover { background: #218838; }
        </style>
    </head>
    <body>
        <h2>Driver Registration Form</h2>
        <form method="POST">
            <label>Name:</label> <input type="text" name="name" required>
            <label>Mobile Number:</label> <input type="text" name="mobile" required>
            <label>Email ID:</label> <input type="email" name="email" required>
            <label>Address:</label> <input type="text" name="address" required>
            <label>License Number:</label> <input type="text" name="license" required>
            <label>License Issued Date:</label> <input type="date" name="issue_date" required>
            <label>License Expiry Date:</label> <input type="date" name="expiry_date" required>
            <label>Aadhaar Number:</label> <input type="text" name="aadhaar" required>
            <button type="submit">Submit</button>
        </form>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(debug=True)
