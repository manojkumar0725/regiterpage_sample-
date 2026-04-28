from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import mysql.connector
import hashlib
import os

app = Flask(__name__)
app.secret_key = "your_secret_key_change_this"

# ✅ MySQL Database Connection - Change these details
DB_CONFIG = {
    "host": "localhost",
    "user": "root",          # உங்கள் MySQL username
    "password": "",          # உங்கள் MySQL password
    "database": "auth_db"
}

def get_db():
    return mysql.connector.connect(**DB_CONFIG)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ─────────────────────────────────────────
# Home
# ─────────────────────────────────────────
@app.route("/")
def home():
    if "userid" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))

# ─────────────────────────────────────────
# Register Page
# ─────────────────────────────────────────
@app.route("/register", methods=["GET"])
def register():
    return render_template("register.html")

@app.route("/registeraction", methods=["POST"])
def registeraction():
    name     = request.form.get("name", "").strip()
    userid   = request.form.get("userid", "").strip()
    password = request.form.get("password", "").strip()
    mobile   = request.form.get("mobile", "").strip()
    email    = request.form.get("email", "").strip()

    # Basic validation
    if not all([name, userid, password, mobile, email]):
        return render_template("register.html", error="அனைத்து fields-ம் நிரப்பவும்!")

    if len(mobile) != 10 or not mobile.isdigit():
        return render_template("register.html", error="சரியான 10-digit mobile number கொடுக்கவும்!")

    hashed_pw = hash_password(password)

    try:
        db = get_db()
        cursor = db.cursor()

        # Check if userid already exists
        cursor.execute("SELECT userid FROM users WHERE userid = %s", (userid,))
        if cursor.fetchone():
            cursor.close()
            db.close()
            return render_template("register.html", error="இந்த User ID ஏற்கனவே பயன்படுத்தப்படுகிறது!")

        # Check if email already exists
        cursor.execute("SELECT email FROM users WHERE email = %s", (email,))
        if cursor.fetchone():
            cursor.close()
            db.close()
            return render_template("register.html", error="இந்த Email ஏற்கனவே பதிவு செய்யப்பட்டுள்ளது!")

        # Insert new user
        cursor.execute(
            "INSERT INTO users (name, userid, password, mobile, email) VALUES (%s, %s, %s, %s, %s)",
            (name, userid, hashed_pw, mobile, email)
        )
        db.commit()
        cursor.close()
        db.close()

        return render_template("register.html", success="Registration வெற்றிகரமாக முடிந்தது! Login பண்ணுங்க.")

    except mysql.connector.Error as e:
        return render_template("register.html", error=f"Database Error: {str(e)}")

# ─────────────────────────────────────────
# Login Page
# ─────────────────────────────────────────
@app.route("/login", methods=["GET"])
def login():
    if "userid" in session:
        return redirect(url_for("dashboard"))
    return render_template("login.html")

@app.route("/loginaction", methods=["POST"])
def loginaction():
    userid   = request.form.get("userid", "").strip()
    password = request.form.get("password", "").strip()

    if not userid or not password:
        return render_template("login.html", error="User ID மற்றும் Password கொடுக்கவும்!")

    hashed_pw = hash_password(password)

    try:
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM users WHERE userid = %s AND password = %s",
            (userid, hashed_pw)
        )
        user = cursor.fetchone()
        cursor.close()
        db.close()

        if user:
            session["userid"] = user["userid"]
            session["name"]   = user["name"]
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="தவறான User ID அல்லது Password!")

    except mysql.connector.Error as e:
        return render_template("login.html", error=f"Database Error: {str(e)}")

# ─────────────────────────────────────────
# Dashboard
# ─────────────────────────────────────────
@app.route("/dashboard")
def dashboard():
    if "userid" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html", name=session["name"], userid=session["userid"])

# ─────────────────────────────────────────
# Logout
# ─────────────────────────────────────────
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

# ─────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
