import os
from dotenv import load_dotenv
from connections import Connection, list_connections

load_dotenv()

# Replace with your PostgreSQL connection details
conn_type = "MS_SQL"
host = "MSI175"
username = "AI_Login"
password = "Kiyoshi1248"
port = 1433
database = "AdventureWorks2019"
conn = Connection(conn_type=conn_type, host=host, username=username, password=password, port=port, database=database)

conn.create_connection()
print(f'key: {conn.key}')
conn.test_connection()
conn.save_connection()
for c in list_connections():
    print(c)



