import psycopg2

conn = psycopg2.connect(database="pydb",
                        host="192.168.1.5",
                        user="app_user",
                        password="m3hdqhr4",
                        port="5432")
cursor = conn.cursor()
cursor.execute('SELECT * FROM public."Person"')
print(cursor.fetchone())