import os
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="credit",
    user="postgres",
    password="1085")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS creditcards;')
cur.execute(
    'CREATE TABLE creditcards(id serial PRIMARY KEY,'
    'bank VARCHAR(255) NOT NULL,'
    'card_number VARCHAR(19) UNIQUE NOT NULL,'
    'date_of_issue TIMESTAMP NOT NULL,'
    'date_of_expire TIMESTAMP NOT NULL,'
    'cvc INT NOT NULL,'
    'owner_name VARCHAR ( 50 ) UNIQUE NOT NULL );'
)

# Insert data into the table

cur.execute('INSERT INTO creditcards (bank, card_number, date_of_issue, date_of_expire,cvc,owner_name)'
            'VALUES (%s, %s, %s, %s,%s,%s)',
            ("privatbank",
             "1234 1234 1234 1234",
             "2020-01-01",
             "2025-01-01",
             123,
             "Bob"))

cur.execute('INSERT INTO creditcards (bank, card_number, date_of_issue, date_of_expire,cvc,owner_name)'
            'VALUES (%s, %s, %s, %s,%s,%s)',
            ("monobank",
             "4321 4321 4321 4321",
             "2021-02-02",
             "2026-02-02",
             321,
             "Tom"))

conn.commit()

cur.close()
conn.close()
