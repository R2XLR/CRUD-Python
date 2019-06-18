#!/usr/bin/python
# -*- coding: utf-8 -*-

import mysql.connector
from mysql.connector import errorcode

config = {
  'host':'<IP_HOST>',
  'user':'<DATABASE_USER>',
  'password':'<DATABASE_PASSWORD>',
  'database':'<DATABASE_NAME>'
}

try:
    conn = mysql.connector.connect(**config)
    print("Connection established")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with the user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cursor = conn.cursor()

    # INSERT
    print("Exemplo de INSERT:")
    cursor.execute("INSERT INTO teste (nome) VALUES ('DUDA');")
    print("Inserted",cursor.rowcount,"row(s) of data.")
    print("-----------------")

    #SELECT
    print("Exemplo de SELECT:")
    cursor.execute("SELECT * FROM teste;")
    rows = cursor.fetchall()
    print("Read",cursor.rowcount,"row(s) of data.")

    for row in rows:
        print("Data row = ", row)

    print("-----------------")

    #UPDATE
    print("Exemplo de UPDATE:")
    cursor.execute("UPDATE teste SET nome = 'CALOPSITA' WHERE nome = 'DUDA';")
    print("Updated",cursor.rowcount,"row(s) of data.")
    print("-----------------")

    #DELETE
    print("Exemplo de UPDATE:")
    cursor.execute("DELETE FROM teste WHERE nome='CALOPSITA';")
    print("Deleted",cursor.rowcount,"row(s) of data.")
    print("-----------------")

conn.commit()
cursor.close()
conn.close()
print("Done.")
