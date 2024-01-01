import mysql.connector
import streamlit as st
import time
from halaman.koneksi import create_connection

connection, cursor = create_connection()


def verify_login(username, password):
    try:
        cursor.execute(
            "SELECT * FROM admin WHERE username = %s AND password = %s",
            (username, password),
        )
        user = cursor.fetchone()
        return user
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
        return None


def login_page():
    st.title("Selamat Datang Di Database Posyandu 🏥 !")
    st.header("", divider="rainbow")
    with st.form("Silahkan Masuk"):
        st.title("Silahkan Masuk")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.form_submit_button("Login"):
            user = verify_login(username, password)
            if user:
                st.success("Login Successful!")
                return user[0]  # Returning user ID or some identifier
            else:
                st.error("Invalid username/password, Please try again.")
    return None
