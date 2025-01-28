import mysql.connector

def create_database():
    db = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password"
    )
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS game_db")
    cursor.execute("USE game_db")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scores (
            id INT AUTO_INCREMENT PRIMARY KEY,
            score INT NOT NULL
        )
    """)
    db.commit()
    db.close()

def connect_db():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database="game_db"
        )
    except mysql.connector.Error as err:
        if err.errno == 1049:
            create_database()
            return connect_db()
        else:
            raise


def save_score(score):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO scores (score) VALUES (%s)", (score,))
    db.commit()
    db.close()

def load_best_score():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT MAX(score) FROM scores")
    result = cursor.fetchone()
    db.close()
    return result[0] if result and result[0] is not None else 0

def load_top_scores():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT score FROM scores ORDER BY score DESC LIMIT 5")
    scores = cursor.fetchall()
    db.close()
    return [score[0] for score in scores]