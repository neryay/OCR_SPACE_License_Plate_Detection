import sqlite3
_database_name = 'LicensePlates_DB.db'

def run_database(vehicles):
    connection = sqlite3.connect(_database_name)
    tables = vehicles.keys()
    cursor = connection.cursor()

    __create_tables(tables, cursor)

    for table_name, license_dataset in vehicles.items():
        __update_table(table_name, license_dataset, cursor)

    connection.commit()
    connection.close()


def __update_table(table_name, vehicles, cursor):
    insert_query = f"INSERT INTO {table_name} VALUES (?, ?)"
    vehicles_list = [(k, v) for k, v in vehicles.items()]
    cursor.executemany(insert_query, vehicles_list)


def __create_tables(tables, cursor):

    for name in tables:
        create_table = f"CREATE TABLE IF NOT EXISTS {name}(license_plate text UNIQUE, timestamp text)"
        cursor.execute(create_table)

