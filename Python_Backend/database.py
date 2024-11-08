import sqlite3


def get_connection():

    conn = sqlite3.connect('something_something.db')
    return conn


def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    # Create new table or edit already existing table?
    # No idea?

    conn.commit()
    conn.close()

    print("Database initialized.")


def store_data(conv_name, conv_id, user, messages_json):
    conn = get_connection()
    cursor = conn.cursor()

    # Something to handle the data insertion into a table
    # Also need method for checking if the conversation is already existent or if we need to create a new table instead

    conn.commit()
    conn.close()

    print("Data stored successfully.")
