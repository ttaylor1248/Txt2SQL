import os
from dotenv import load_dotenv
from connections import create_connection, test_connection, list_connections, save_connection

load_dotenv()

# Replace with your PostgreSQL connection details
host = os.getenv('Postgres_HOST')
username = os.getenv('Postgres_USER')
password = os.getenv('Postgres_PASS')
port = os.getenv('Postgres_PORT')

conn_type, key, connection_str = create_connection(conn_type="Postgres", host=host, username=username,
                                                   password=password, port=port, database='polls')
print(f'{conn_type}:  {key}:  {connection_str}')

key, connection_string, result_text = test_connection(conn_type=conn_type, key=key, connection_string=connection_str)
print(f'{key}: {connection_str}: {result_text}')

key_text = save_connection(key=key, value=connection_str)
print(key_text)

connections = list_connections()
print(connections)