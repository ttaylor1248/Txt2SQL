from sqlalchemy import create_engine, inspect
import os
from dotenv import load_dotenv

# load environment
load_dotenv()


def create_conn(db=None):
    # Replace with your PostgreSQL connection details
    host = os.getenv('Postgres_HOST')
    username = os.getenv('Postgres_USER')
    password = os.getenv('Postgres_PASS')
    port = os.getenv('Postgres_PORT')

    if db is None:
        connection_string = f'postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{port}'
    else:
        connection_string = f'postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{port}/{db}'
    return connection_string


# List schemas and tables
def list_schemas_and_tables():
    schema_table_dict = {}
    schemas = inspector.get_schema_names()
    for schema in schemas:
        tables = inspector.get_table_names(schema=schema)
        schema_table_dict[schema] = tables
    return schema_table_dict


# Create the SQLAlchemy engine
engine = create_engine(create_conn('polls'))
inspector = inspect(engine)

databases = list_databases()
for db in databases:
    if db != "information_schema":
        # engine = create_engine(create_conn(db))
        # inspector = inspect(engine)

        schemas_and_tables = list_schemas_and_tables()
        print("\nSchemas and Tables:")
        for schema, tables in schemas_and_tables.items():
            # print(f"Schema: {schema}")
            for table in tables:
                print(f"{schema}.{table}")
