import psycopg2
import csv


conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="1111",
    database="north"
)

cur = conn.cursor()
try:
    with open("customers_data.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cur.execute(f'INSERT INTO customers_data VALUES (%s, %s, %s)',
                    (f"{row['customer_id']}", f"{row['company_name']}", f"{row['contact_name']}"))

    with open("employees_data.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        i = 1
        for row in reader:
            cur.execute(f'INSERT INTO employees_data VALUES (%s, %s, %s, %s, %s, %s)',
                        (f"{i}", f"{row['first_name']}", f"{row['last_name']}", f"{row['title']}", f"{row['birth_date']}", f"{row['notes']}"))
            i += 1

    with open("orders_data.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cur.execute(f'INSERT INTO orders_data VALUES (%s, %s, %s, %s, %s)',
                        (f"{row['order_id']}", f"{row['customer_id']}", f"{row['employee_id']}",f"{row['order_date']}", f"{row['ship_city']}"))

    conn.commit()

except Exception as e:
    print(e)

finally:
    cur.close()
    conn.close()