"""
SELECT id_cabang as "ID Cabang",
        nama_cabang as "Nama Cabang",
        nama_owner as "Nama Owner",
        telepon as Telepon,
        alamat as Alamat
        FROM cabang

nama = st.text_input("Nama Cabang : ")
    owner = st.text_input("Nama Owner : ")
    telepon = st.text_input("Telepon : ")
    alamat = st.text_input("Alamat : ")
    """

import streamlit as st

st.form()

st.subheader("Belum punya akun?")
    if st.button("Sign Up", key="sign_"):
        with st.form("Sign Up"):
            kosong = st.empty()
            kosong.title("Silahkan Mendaftar")
            nama = st.text_input("Nama")
            username = st.text_input("Username", key="_up")
            password = st.text_input("Password", type="password", key="sign_up")

            if st.form_submit_button("Daftar"):
                data_in = """
                            INSERT INTO admin (nama, username, password) VALUES (%s, %s, %s)
                        """
                value = (nama, username, password)
                # cursor.execute is to execute the mysql command
                cursor.execute(data_in, (value,))
                # connection.commit is to save the changes
                connection.commit()
                st.success("Registrasi Berhasil! Silahkan Login")
                time.sleep(1)
                st.rerun()
