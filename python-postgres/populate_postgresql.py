import psycopg2
from csv import reader
import vars
import os


def create_tables(connection):
    # SQL commands

    commands = ["""DROP TABLE  deliveries""",
                """DROP TABLE  order_items""",
                """DROP TABLE  orders"""
                ]

    commands += [
        """
                CREATE TABLE deliveries (
                id INTEGER PRIMARY KEY,
                order_item_id INTEGER NOT NULL,
                delivered_quantity INTEGER NOT NULL
                )
                """,
        """
                CREATE TABLE order_items (
                id INTEGER PRIMARY KEY,
                order_id INTEGER NOT NULL,
                price_per_unit DECIMAL DEFAULT -1,
                quantity INTEGER NOT NULL,
                product VARCHAR(255) NOT NULL
                )
                """,
        """
                CREATE TABLE orders (
                id INTEGER PRIMARY KEY,
                created_at TIMESTAMP WITH TIME ZONE NOT NULL,
                order_name VARCHAR(255),
                customer_id VARCHAR(255) NOT NULL
                )
                """
    ]

    commands += [
        f"""
                ALTER TABLE deliveries
                ADD COLUMN updated_at TIMESTAMP WITH TIME ZONE,
                ADD COLUMN deleted_at TIMESTAMP WITH TIME ZONE
                """,
        f"""
                ALTER TABLE order_items
                ADD COLUMN updated_at TIMESTAMP WITH TIME ZONE,
                ADD COLUMN deleted_at TIMESTAMP WITH TIME ZONE
                """,
        f"""
                ALTER TABLE orders
                ADD COLUMN updated_at TIMESTAMP WITH TIME ZONE,
                ADD COLUMN deleted_at TIMESTAMP WITH TIME ZONE
                """
    ]

    # initializing the cursor
    cursor = connection.cursor()

    # executing the commands
    for command in commands:
        cursor.execute(command)

    # commiting the changed
    connection.commit()

    # closing the cursor
    cursor.close()


def insert_data(connection):
    for csv_file in os.listdir('./data'):
        # initliazing the cursor
        cursor = connection.cursor()

        # getting the path to the csv
        path = os.path.join(os.getcwd(), 'data', csv_file)

        with open(path, 'r') as read_obj:
            # getting the table name
            table_name = csv_file.split('.')[0]

            # reading the csv
            csv_reader = reader(read_obj)

            # getting the header and %s formats
            header = next(csv_reader)
            formats = get_string_formats(header)

            # check file as empty
            if header != None:
                # itterate over each row after the header in the csv
                headers = format_header(header)

                # inserting the data
                for row in read_obj:
                    # cleaning the data
                    row = clean_list(row)
                    cursor.execute(
                        f'insert into {table_name} ({headers}) values ({formats})', tuple(row))

        # commiting the changes
        connection.commit()

        # closing the cursor
        cursor.close()

    # closing the connection
    connection.close()


def get_string_formats(list):
    formats = '%s ' * len(list)
    formats = formats.strip()
    formats = formats.replace(' ', ', ')
    return formats


def format_header(header):
    output = ', '.join(header)
    return output


def clean_list(lst):
    lst = lst.strip().split(',')
    for index in range(len(lst)):
        if lst[index] == '':
            lst[index] = None

    return lst


if __name__ == '__main__':
    # establishing the conenciton.
    connection = psycopg2.connect(
        host=vars.HOSTNAME,
        database=vars.DATABASE_NAME,
        user=vars.USERNAME,
        password=vars.PASSWORD,
        port=vars.PORT
    )

    create_tables(connection)
    insert_data(connection)
