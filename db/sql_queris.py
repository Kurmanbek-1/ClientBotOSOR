import sqlite3

DATABASE_NAME = 'db/review.db'  # Замените на реальное имя вашей базы данных

CREATE_TABLE_REVIEW = """
    CREATE TABLE IF NOT EXISTS reviews
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255),
    fullname VARCHAR(255),
    articule TEXT,
    info VARCHAR(255),
    city VARCHAR(255) NULL,
    photo TEXT)
"""

INSERT_INTO_TABLE_REVIEW = """
    INSERT INTO reviews(fullname, name, articule, info, city, photo) VALUES (?, ?, ?, ?, ?, ?)
"""

SELECT_CHECKS_REVIEWS = """
    SELECT * FROM reviews
"""

SELECT_PRODUCT_FROM_ARTICUL = """
    SELECT * FROM product_coming WHERE articul = $1

"""

async def execute_query(query, values):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute(CREATE_TABLE_REVIEW)

    cursor.execute(query, values)
    connection.commit()
    connection.close()
