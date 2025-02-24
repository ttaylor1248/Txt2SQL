from sqlalchemy import create_engine, text
from dotenv import load_dotenv, set_key, dotenv_values


class Connection():
    def __init__(self, conn_type, host, username=None, password=None, port=None, database=None, service_name=None):
        self.key = None
        self.value = None
        self.conn_type = conn_type
        self.host = host
        self.user = username
        self.pw = password
        self.port = port
        self.database = database
        self.service = service_name
        self.connection_test = False

    def create_connection(self):

        if self.conn_type == "MySQL":
            self.key = f'conn_MySQL_{self.host}_{self.database}'
            self.value = f'mysql+pymysql://{self.user}:{self.pw}@{self.host}:{self.port}/{self.database}'
        elif self.conn_type == "Postgres":
            self.key = f'conn_Pg_{self.host}_{self.database}'
            self.value = f'postgresql+psycopg2://{self.user}:{self.pw}@{self.host}:{self.port}/{self.database}'
        elif self.conn_type == "MS_SQL":
            driver = 'ODBC Driver 17 for SQL Server'
            self.key = f'conn_MS_{self.host}_{self.database}'
            self.value = f'mssql+pyodbc://{self.user}:{self.pw}@{self.host}/{self.database}?driver={driver}'
        elif self.conn_type == "SQLLite":
            self.key = f'conn_SQLLite_{self.host}'
            self.value = f'sqlite:///{self.host}'
        elif self.conn_type == "Oracle":
            self.key = f'conn_Oracle_{self.host}'
            self.value = (f'oracle+cx_oracle://{self.user}:{self.pw}@{self.host}:{self.port}/?service_name'
                          f'={self.service}')
        else:
            self.key = None
            self.value = None

    def test_connection(self):
        engine = create_engine(self.value)
        try:
            with engine.connect() as connection:
                result = connection.execute(text("SELECT 1;"))
                if result is not None:
                    self.connection_test = True
        except Exception as e:
            print(f"The error '{e}' occurred")

    def save_connection(self, env_path='.env'):
        # Load existing .env file if it exists
        if self.connection_test:
            try:
                load_dotenv(dotenv_path=env_path)
                set_key(env_path, self.key, self.value)
                print("Connection Saved")
            except Exception as e:
                print(f"The error '{e}' occurred")
        else:
            print("Connection Not Saved, Test Failed")


def list_connections():
    # Load environment variables from .env file
    load_dotenv()
    # Retrieve all key-value pairs
    env_vars = dotenv_values()

    # Extract keys and apply filter
    keys = list(env_vars.keys())
    connection_list = list(filter(lambda s: s.startswith("conn_"), keys))

    return sorted(connection_list)
