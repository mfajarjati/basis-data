import mysql.connector
import streamlit as st


def create_connection():
    try:
        db_config = {
            "host": "localhost",
            "user": "",
            "password": "",
            "database": "posyandu_db",
        }
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

    except mysql.connector.Error as err:
        # Establish the connection
        st.error("wrong user/password in database")
        # Create a cursor object
    return connection, cursor
