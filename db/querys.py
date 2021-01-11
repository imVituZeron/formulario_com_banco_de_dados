import sqlite3
from contextlib import contextmanager


connection = sqlite3.connect('db/register.db')
cursor = connection.cursor()


def insert(name, age, mail, phone):
    query = "INSERT OR IGNORE INTO user (name, age, mail, phone) VALUES (?, ?, ?, ?)"
    cursor.execute(query, (name, age, mail, phone))
    connection.commit()

    return True


def list_data():
    query = "SELECT * FROM user"
    cursor.execute(query)

    for date in cursor.fetchall():
        print(date)


def get_date_select(value):
    query = "SELECT * FROM user"
    cursor.execute(query)

    for date in cursor.fetchall():
        ID, *othes = date

        if ID == int(value):
            return True
        else:
            return False


def update_name(value, identification):
    query = "UPDATE user SET name=? WHERE id=?"
    cursor.execute(query, (value, identification))
    connection.commit()

    return True


def update_age(value, identification):
    query = "UPDATE user SET age=? WHERE id=?"
    cursor.execute(query, (value, identification))
    connection.commit()

    return True


def update_mail(value, identification):
    query = "UPDATE user SET mail=? WHERE id=?"
    cursor.execute(query, (value, identification))
    connection.commit()

    return True


def update_phone(value, identification):
    query = "UPDATE user SET phone=? WHERE id=?"
    cursor.execute(query, (value, identification))
    connection.commit()

    return True


def delete(identification):
    query = "DELETE FROM user WHERE id=?"
    cursor.execute(query, (identification,))
    connection.commit()

    return True


if __name__ == "__main__":
    pass