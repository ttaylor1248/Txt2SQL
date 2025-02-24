from sqlalchemy import create_engine, inspect
import os
from dotenv import load_dotenv

load_dotenv()

# Replace with your PostgreSQL connection details
db_host = os.getenv('Postgres_HOST')
db_user = os.getenv('Postgrest_USER')
db_pass = os.getenv('Postgres_PASS')
port = os.getenv('Postgrest_PORT')


# Create the SQLAlchemy engine
engine = create_engine(connection_string)
inspector = inspect(engine)


# List databases
def list_databases():
    databases = inspector.get_schema_names()
    return databases


databases = list_databases()
for db in databases:
    print(db)


# Replace with your MySQL connection details
username = 'your_username'
password = 'your_password'
host = 'your_host'
port = 'your_port'  # Default MySQL port is 3306
database = 'your_database'

# Create the connection string
connection_string = f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'

# Create the SQLAlchemy engine
engine = create_engine(connection_string)

# Test the connection
with engine.connect() as connection:
    result = connection.execute("SELECT VERSION();")
    for row in result:
        print(row)

# Replace with your Microsoft SQL Server connection details
username = 'your_username'
password = 'your_password'
server = 'your_server'
database = 'your_database'
driver = 'ODBC Driver 17 for SQL Server'

# Create the connection string
connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}'

# Path to the SQLite database file
database_file = 'my_database.db'

# Create the SQLite connection string
connection_string = f'sqlite:///{database_file}'

# Create the SQLAlchemy engine
engine = create_engine(connection_string)

# Test the connection
with engine.connect() as connection:
    result = connection.execute("SELECT sqlite_version();")
    for row in result:
        print(row)
# Replace with your Oracle connection details
username = 'your_username'
password = 'your_password'
host = 'your_host'
port = 'your_port'  # Default Oracle port is 1521
service_name = 'your_service_name'

# Create the connection string
connection_string = f'oracle+cx_oracle://{username}:{password}@{host}:{port}/?service_name={service_name}'

# Create the SQLAlchemy engine
engine = create_engine(connection_string)

# Test the connection
with engine.connect() as connection:
    result = connection.execute("SELECT * FROM DUAL")
    for row in result:
        print(row)

# Replace with your PostgreSQL connection details
username = 'your_username'
password = 'your_password'
host = 'your_host'
port = '5432'  # Default PostgreSQL port is 5432
database = 'your_database'

# Create the connection string
connection_string = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'

# Create the SQLAlchemy engine
engine = create_engine(connection_string)

# Test the connection
try:
    with engine.connect() as connection:
        result = connection.execute("SELECT version();")
        for row in result:
            print(row)
    print("Connection to PostgreSQL DB successful")
except Exception as e:
    print(f"The error '{e}' occurred")

# Replace with your Microsoft SQL Server connection details
username = 'your_username'
password = 'your_password'
server = 'your_server'
database = 'your_database'
driver = 'ODBC Driver 17 for SQL Server'

# Create the connection string
connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}'

# Create the SQLAlchemy engine
engine = create_engine(connection_string)

# Test the connection
try:
    with engine.connect() as connection:
        result = connection.execute("SELECT @@VERSION AS 'SQL Server Version';")
        for row in result:
            print(row)
    print("Connection to Microsoft SQL Server DB successful")
except Exception as e:
    print(f"The error '{e}' occurred")

from sqlalchemy import create_engine, text

# Replace with your PostgreSQL connection details
username = 'your_username'
password = 'your_password'
host = 'your_host'
port = '5432'  # Default PostgreSQL port is 5432
database = 'your_database'

# Create the connection string
connection_string = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'

# Create the SQLAlchemy engine
engine = create_engine(connection_string)

# Test the connection
try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        for row in result:
            print(row)
    print("Connection to PostgreSQL DB successful")
except Exception as e:
    print(f"The error '{e}' occurred")


