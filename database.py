import mysql.connector

def select(q):
    cnx = mysql.connector.connect(user='root', password='', host='localhost', database='keystrokeexam')
    cur = cnx.cursor(dictionary=True)  # to view o/p in dictionary otherwise it in tuple in list
    cur.execute(q)
    result=cur.fetchall()
    cnx.close
    cur.close()
    return result

def insert(q):
    cnx = mysql.connector.connect(user='root', password='', host='localhost', database='keystrokeexam')
    cur = cnx.cursor(dictionary=True)  # to view o/p in dictionary otherwise it in tuple in list
    cur.execute(q)
    result=cur.lastrowid
    cnx.commit()
    cnx.close
    cur.close()
    return result

def update(q):
    cnx = mysql.connector.connect(user='root', password='', host='localhost', database='keystrokeexam')
    cur = cnx.cursor(dictionary=True)  # to view o/p in dictionary otherwise it in tuple in list
    cur.execute(q)
    result = cur.rowcount
    cnx.commit()
    cnx.close
    cur.close()
    return result

def delete(q):
    cnx = mysql.connector.connect(user='root', password='', host='localhost', database='keystrokeexam')
    cur = cnx.cursor(dictionary=True)  # to view o/p in dictionary otherwise it in tuple in list
    cur.execute(q)
    result = cur.rowcount
    cnx.commit()
    cnx.close
    cur.close()
    return  result
