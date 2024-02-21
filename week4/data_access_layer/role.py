from week4.database_layer import create_database as database
import sqlite3


# CREATE

def create_role(role_name):
    conn = sqlite3.connect(database.DATABASE_NAME)
    cursor = conn.cursor()

    query = "INSERT INTO Role (role_name) VALUES (?)"
    params = (role_name,)
    result = cursor.execute(query, params)

    conn.commit()
    conn.close()

    if result.rowcount > 0:
        return cursor.lastrowid
    else:
        return False


# READ

def get_role(role_id):
    conn = sqlite3.connect(database.DATABASE_NAME)
    cursor = conn.cursor()

    query = "SELECT * FROM Role WHERE id=?"
    params = (role_id,)
    cursor.execute(query, params)
    user = cursor.fetchone()

    conn.close()
    return user

def get_all_roles():
    conn = sqlite3.connect(database.DATABASE_NAME)
    cursor = conn.cursor()

    query = "SELECT * FROM Role"
    cursor.execute(query)
    users = cursor.fetchall()

    conn.close()
    return users


# UPDATE

def update_role(role_id, role_name):
    conn = sqlite3.connect(database.DATABASE_NAME)
    cursor = conn.cursor()

    query = "UPDATE Role SET role_name=? WHERE id=?"
    params = (role_name, role_id)
    result = cursor.execute(query, params)

    conn.commit()
    conn.close()

    if result.rowcount > 0:
        return True
    else:
        return False


# DELETE

def delete_role(role_id):
    conn = sqlite3.connect(database.DATABASE_NAME)
    cursor = conn.cursor()

    query = "DELETE FROM Role WHERE id=?"
    params = (role_id,)
    result = cursor.execute(query, params)

    conn.commit()
    conn.close()

    if result.rowcount > 0:
        return True
    else:
        return False

if __name__ == "__main__":
    # create_role("Admin")
    # create_role("Professor")
    # create_role("Lab Attendent")
    for role in get_all_roles():
        print(role)
