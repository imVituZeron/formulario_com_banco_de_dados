import sqlite3

conncetion = sqlite3.connect('db/register.db')
cursor = conncetion.cursor()

def insert(name, age, mail, phone):
    query = "INSERT OR IGNORE INTO user (name, age, mail, phone) VALUES (?, ?, ?, ?)"
    cursor.execute(query, (name, age, mail, phone))
    conncetion.commit()
    return True

def list_data():
    query = "SELECT * FROM user"
    cursor.execute(query)

    for date in cursor.fetchall():
        print(date)

def update(data_table, value, identification):
    query = f"UPDATE user SET {data_table}=? WHERE id=?"
    cursor.execute(query, (value, identification))
    conncetion.commit()
    return True

def delete(identification):
    query = "DELETE FROM user WHERE id=?"
    cursor.execute(query, (identification,))
    conncetion.commit()
    return True


if __name__ == "__main__":
    pass