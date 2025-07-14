from flask import Flask, jsonify
from flask_cors import CORS
import os
import psycopg2

app = Flask(__name__)
CORS(app)

@app.route('/api/hello')
def hello():
    return jsonify({"message": "Hello from Flask + PostgreSQL!"})

@app.route('/api/db')
def test_db():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB", "mydb"),
            user=os.getenv("POSTGRES_USER", "myuser"),
            password=os.getenv("POSTGRES_PASSWORD", "mypassword"),
            host=os.getenv("POSTGRES_HOST", "postgres"),
            port=5432
        )
        cur = conn.cursor()
        cur.execute("SELECT 'DB Connected!'")
        result = cur.fetchone()
        return jsonify({"db": result[0]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
