import streamlit as st
import os
import importlib.util
from pagelogin import *
from halaman import *
import time


def intro(user_id):
    st.write("# Selamat Datang di Dashboard Database Posyandu! 🏥")

    st.header("", divider="rainbow")
    st.markdown(
        """
        ### About database
        Database ini berisi informasi mengenai data-data dalam bentuk tabel yang digunakan untuk keperluan posyandu.
        Tabel-Tabel yang digunakan yaitu :
        - Tabel Admin 🙍🏻‍♂️  
        - Tabel Biodata Pemeriksa 👩🏻‍⚕️
        - Tabel Biodata Ibu 👩🏻 
        - Tabel Biodata Anak 👶🏻 
        - Tabel Hasil Pemeriksaan 📋
        - Tabel Cabang Posyandu 🏢 
        """
    )


pages_dict = {
    "Dashboard": "dashboard.py",
    "Tabel Admin": "admin.py",
    "Tabel Biodata Pemeriksa": "pemeriksa.py",
    "Tabel Biodata Ibu": "ibu.py",
    "Tabel Biodata Anak": "anak.py",
    "Tabel Data Cabang": "cabang.py",
    "Tabel Hasil Pemeriksaan": "pemeriksaan.py",
    # Tambahkan pemetaan untuk tabel lainnya
}

# Judul atau navigasi untuk memilih halaman

if __name__ == "__main__":
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        user_id = login_page()
        if user_id:
            st.session_state.logged_in = True
            time.sleep(1)
            st.rerun()

    if st.session_state.logged_in:
        selected_page = st.sidebar.selectbox(
            "Silahkan Pilih :", list(pages_dict.keys())
        )
        if selected_page != "Dashboard":
            unique_key = f"{selected_page}_selectbox"
            module_path = f"halaman.{pages_dict[selected_page]}"
            spec = importlib.util.spec_from_file_location(
                pages_dict[selected_page],
                os.path.join("halaman", pages_dict[selected_page]),
            )
            selected_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(selected_module)
            selected_module.main()

        elif selected_page == "Dashboard":
            intro(None)  # No need for user_id here

    if st.session_state.logged_in and st.sidebar.button("Log Out"):
        st.session_state.logged_in = False
        time.sleep(1)
        st.rerun()


st.markdown("")
st.markdown("")
st.caption("Copyright (c) - Created by kelompok 2 (Basis Data) - 2024")
