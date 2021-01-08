import psycopg2

connection = psycopg2.connect(
    database="football_world",
    user="postgres",
    password="value",
    host="127.0.0.1",
    port="5432"
)

cursor = connection.cursor()
