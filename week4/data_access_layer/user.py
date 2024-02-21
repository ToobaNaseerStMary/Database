from week4.database_layer import create_database as database
import sqlite3


# CREATE

def create_user(first_name, last_name, email, role_id):
    conn = sqlite3.connect(database.DATABASE_NAME)
    cursor = conn.cursor()

    query = "INSERT INTO User (first_name, last_name, email, role) VALUES (?, ?, ?, ?)"
    params = (first_name, last_name, email, role_id)
    result = cursor.execute(query, params)

    conn.commit()
    conn.close()

    if result.rowcount > 0:
        return cursor.lastrowid
    else:
        return False


# READ

def get_user(user_id):
    conn = sqlite3.connect(database.DATABASE_NAME)
    cursor = conn.cursor()

    query = "SELECT * FROM User WHERE id=?"
    params = (user_id,)
    cursor.execute(query, params)
    user = cursor.fetchone()

    conn.close()
    return user


def get_users_with_role(role_id):
    conn = sqlite3.connect(database.DATABASE_NAME)
    cursor = conn.cursor()

    query = "SELECT * FROM User WHERE role = ?"
    params = (role_id,)
    cursor.execute(query, params)
    users = cursor.fetchall()

    conn.close()
    return users


def get_all_users():
    conn = sqlite3.connect(database.DATABASE_NAME)
    cursor = conn.cursor()

    query = "SELECT * FROM User"
    cursor.execute(query)
    users = cursor.fetchall()

    conn.close()
    return users


# UPDATE

def update_user(user_id, new_first_name, new_last_name, new_email, new_role_id):
    conn = sqlite3.connect(database.DATABASE_NAME)
    cursor = conn.cursor()

    query = "UPDATE User SET first_name=?, last_name=?, email=?, role=? WHERE id=?"
    params = (new_first_name, new_last_name, new_email, new_role_id, user_id)
    result = cursor.execute(query, params)

    conn.commit()
    conn.close()

    if result.rowcount > 0:
        return True
    else:
        return False


# DELETE

def delete_user(user_id):
    conn = sqlite3.connect(database.DATABASE_NAME)
    cursor = conn.cursor()

    query = "DELETE FROM User WHERE id=?"
    params = (user_id,)
    result = cursor.execute(query, params)

    conn.commit()
    conn.close()

    if result.rowcount > 0:
        return True
    else:
        return False

if __name__ == "__main__":
    create_user("tooba", "naseer", "toobanaseer3@gmail.com", 1)
    for user in get_all_users():
        print(user)
    update_user(1, "toobaa", "khan", "toobanaseer2@gmail.com", 2)
    for user in get_all_users():
        print(user)
