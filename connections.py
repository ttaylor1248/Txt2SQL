from sqlalchemy import create_engine
from dotenv import load_dotenv, set_key, dotenv_values
import psycopg2
import pymysql
import pyodbc
import cx_Oracle


def create_connection(conn_type, host, username=None, password=None, port=None, database=None, service_name=None):

    if conn_type == "MySQL":
        key = f'conn_MySQL_{host}_{database}'
        connection_string = f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'
    elif conn_type == "Postgres":
        key = f'conn_Pg_{host}_{database}'
        connection_string = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'
    elif conn_type == "MS_SQL":
        driver = 'ODBC Driver 17 for SQL Server'
        key = f'conn_MS_{host}_{database}'
        connection_string = f'mssql+pyodbc://{username}:{password}@{host}/{database}?driver={driver}'
    elif conn_type == "SQLLite":
        key = f'conn_SQLLite_{host}'
        connection_string = f'sqlite:///{host}'
    elif conn_type == "Oracle":
        key = f'conn_Oracle_{host}'
        connection_string = f'oracle+cx_oracle://{username}:{password}@{host}:{port}/?service_name={service_name}'
    else:
        key = None
        connection_string = None

    return conn_type, key, connection_string


def test_connection(conn_type, key, connection_string):
    try:
        engine = create_engine(connection_string)

        with engine.connect() as connection:
            if conn_type in ['MySQL', 'Postgres']:
                result = connection.execute("SELECT VERSION();")
            elif conn_type == "MS_SQL":
                result = connection.execute("SELECT @@VERSION AS 'SQL Server Version';")
            elif conn_type == "SQLLite":
                result = connection.execute("SELECT sqlite_version();")
            elif conn_type == "Oracle":
                result = connection.execute("SELECT * FROM DUAL")
            else:
                result = None

            if result is not None:
                result_text = 'Connection Successful'
            else:
                result_text = 'Connection failed'
    except Exception as e:
        result_text = f"The error '{e}' occurred"

    return key, connection_string, result_text


def save_connection(key, value, env_path='.env'):
    # Load existing .env file if it exists
    load_dotenv(dotenv_path=env_path)
    try:
        set_key(env_path, key, value)
        err_text = "Key Saved"
    except Exception as e:
        err_text = f"The error '{e}' occurred"

    return err_text


def list_connections():
    # Load environment variables from .env file
    load_dotenv()
    # Retrieve all key-value pairs
    env_vars = dotenv_values()

    # Extract keys and apply filter
    keys = list(env_vars.keys())
    connection_list = list(filter(lambda s: s.startswith("conn_"), keys))

    return sorted(connection_list)
