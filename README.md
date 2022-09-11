# Migrate WP User

This Python script gets a WordPress user and generates an insert SQL that can be used to insert him into any other WordPress project.

## How it works
First, run this command to install the pip dependencies:
```shell
python3 -m pip install -r requirements.txt
```

Copy the `environment_example.py` changing its name to `environment.py`, passing the WP database connection parameters and the user ID which will be imported.
```python
ORIGIN_DB = {
    'database': '{DB_NAME_GOES_HERE}',
    'host': '{DB_HOST_GOES_HERE}',
    'port': '{DB_PORT_GOES_HERE}',
    'user': '{DB_USER_GOES_HERE}',
    'pass': '{DB_PASSWORD_GOES_HERE}',
    'user_id': '{USER_ID_GOES_HERE}'
}
```

Then run this command to execute the SQL generation script:
```shell
python3 migratewpuser.py
```

When it's over, a SQL file is generated, containing the instructions to insert this user into any other WordPress project.