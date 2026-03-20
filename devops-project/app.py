from flask import Flask
import psycopg2
import redis
import os

app = Flask(__name__)

# 🔹 Database connection function
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "db"),
            database=os.getenv("DB_NAME", "mydb"),
            user=os.getenv("DB_USER", "user"),
            password=os.getenv("DB_PASS", "password")
        )
        return conn
    except Exception as e:
        return None

# 🔹 Redis connection
def get_redis_connection():
    try:
        r = redis.Redis(
            host=os.getenv("REDIS_HOST", "redis"),
            port=6379
        )
        return r
    except Exception:
        return None


# 🔹 Home route
@app.route('/')
def home():
    return "🚀 DevOps Flask App Running Successfully!"


# 🔹 Database test route
@app.route('/db')
def db():
    conn = get_db_connection()
    if conn:
        return "✅ Connected to Postgres Database!"
    else:
        return "❌ Failed to connect to Database"


# 🔹 Redis test route
@app.route('/cache')
def cache():
    r = get_redis_connection()
    if r:
        try:
            r.set("message", "Hello from Redis 🚀")
            return r.get("message").decode()
        except Exception as e:
            return f"❌ Redis Error: {e}"
    else:
        return "❌ Failed to connect to Redis"


# 🔹 Run app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
