from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask + MySQL running 🚀"

@app.route("/db")
def db_check():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST", "db"),
            user=os.getenv("MYSQL_USER", "root"),
            password=os.getenv("MYSQL_PASSWORD", "root"),
            connection_timeout=5,
        )
        conn.close()
        return "Database Connected ✅"
    except mysql.connector.Error as err:
        app.logger.exception("Database connection failed")
        return f"Database Connection Failed ❌: {err}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
