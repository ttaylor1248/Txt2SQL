from dotenv import load_dotenv, set_key, dotenv_values
import os

# Load existing .env file if it exists
env_path = '.env'
load_dotenv(dotenv_path=env_path)

# Define a function to add or update a variable in the .env file
def set_env_variable(key, value, env_path=env_path):
    # Check if the file already exists
    if os.path.exists(env_path):
        # Load existing values
        current_values = dotenv_values(env_path)
    else:
        current_values = {}

    # Update the value in the current values
    current_values[key] = value

    # Write all values back to the .env file
    with open(env_path, 'w') as f:
        for k, v in current_values.items():
            f.write(f'{k}="{v}"\n')

# Example usage
set_env_variable('DB_HOST', 'localhost')
set_env_variable('DB_USER', 'my_user')
set_env_variable('DB_PASS', 'my_password')
set_env_variable('DB_NAME', 'my_database')
set_env_variable('DB_PORT', '3306')

print("Environment variables have been updated.")


import os
from dotenv import load_dotenv, dotenv_values

# Load environment variables from .env file
load_dotenv()

# Retrieve all key-value pairs
env_vars = dotenv_values()

# Extract keys
keys = list(env_vars.keys())

# Print the keys to verify
print("Keys in .env file:")
for key in keys:
    print(key)


import os
from dotenv import load_dotenv, dotenv_values

# Load environment variables from .env file
load_dotenv()

# Retrieve all key-value pairs
env_vars = dotenv_values()

# Define a filter function
def filter_keys(keys, filter_func):
    return [key for key in keys if filter_func(key)]

# Example filter function: return keys that start with 'DB_'
def starts_with_db(key):
    return key.startswith('DB_')

# Extract keys and apply filter
keys = list(env_vars.keys())
filtered_keys = filter_keys(keys, starts_with_db)

# Print the filtered keys to verify
print("Filtered Keys:")
for key in filtered_keys:
    print(key)

# Sample list of strings
strings_list = ["conn_1", "conn_2", "test_1", "conn_3", "example"]

# Filter the list using a lambda expression
filtered_list = list(filter(lambda s: s.startswith("conn_"), strings_list))

# Print the filtered list
print(filtered_list)


