import sqlite3
from contextlib import contextmanager

@contextmanager
def connect():
    connection = sqlite3.connect('db/register.db')

    try:
        yield connection
    finally:
        connection.close()

def insert(name, age, mail, phone):
    with connect() as connection:
        with connection.cursor() as cursor:
            query = "INSERT OR IGNORE INTO user (name, age, mail, phone) VALUES (?, ?, ?, ?)"
            cursor.execute(query, (name, age, mail, phone))
            connection.commit()

    return True

def list_data():
    with connect() as connection:
        with connection.cursor() as cursor:
            query = "SELECT * FROM user"
            cursor.execute(query)

            for date in cursor.fetchall():
                print(date)

def update(data_table, value, identification):
    with connect() as connection:
        with connection.cursor() as cursor:
            query = f"UPDATE user SET {data_table}=? WHERE id=?"
            cursor.execute(query, (value, identification))
            connection.commit()

    return True

def delete(identification):
    with connect() as connection:
        with connection.cursor() as cursor:
            query = "DELETE FROM user WHERE id=?"
            cursor.execute(query, (identification,))
            connection.commit()
            
    return True


if __name__ == "__main__":
    pass