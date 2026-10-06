import psycopg2


conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="1111",
    database="tests"
)

cur = conn.cursor()
cur.execute("INSERT INTO post VALUES ('4', 'pidr', ' ', '1')")
cur.execute("SELECT * FROM post")
conn.commit()

rows = cur.fetchall()

for row in rows:
    print(row)



cur.close()
conn.close()