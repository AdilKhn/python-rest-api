import psycopg2
import json

def do_insert(cursor,conn):
    j = {"name": "foobar", "age": 45}
    js = json.dumps(j)
    postgres_insert_query = """ INSERT INTO app.jsonic(payload) VALUES (%s)"""
    record_to_insert = (js,)
    cursor.execute(postgres_insert_query, record_to_insert)
    conn.commit()



conn = psycopg2.connect(database="pydb",
                        host="192.168.1.5",
                        user="app_user",
                        password="m3hdqhr4",
                        port="5432")
cursor = conn.cursor()
cursor.execute('SELECT * FROM app.jsonic')
print(cursor.fetchall())
do_insert(cursor,conn)