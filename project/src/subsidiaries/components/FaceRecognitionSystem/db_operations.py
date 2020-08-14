import sqlite3


def createConnection():
    con = sqlite3.connect(
        "C:\\Users\\sumitsingh\\Documents\\Python\\face-recogModule\\module\\code\\db\\database.db"
    )
    return con


def destroyConnection(con):
    con.commit()
    con.close()


def insertOrUpdate(id, name, age, gender):
    # BELOW CODE IS FOR DYNAMIC INSERTION
    con = createConnection()
    user = (name, age, gender)
    insertQuery = "INSERT INTO users(name, age, gender) VALUES (?,?,?)"
    cursor = con.execute(insertQuery, user)
    destroyConnection(con)
    return cursor.rowcount


def view():
    res = any
    con = createConnection()
    cmd = "select * from users"
    cursor = con.execute(cmd)
    res = cursor.fetchall()
    destroyConnection(con)
    return res


def getLastRowId():
    con = createConnection()
    cmd = "select id from users ORDER BY id DESC LIMIT 1;"
    cursor = con.execute(cmd)
    destroyConnection(con)
    return cursor
