import streamlit as st
import os
import importlib.util
from streamlit_option_menu import option_menu
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
        with st.sidebar:
            st.sidebar.image(
                "logo.png",
                width=50,
                use_column_width=True,
            )
            pages_dict = option_menu(
                menu_title="Main Menu",
                options=[
                    "Dashboard",
                    "Tabel Admin",
                    "Tabel Biodata Pemeriksa",
                    "Tabel Biodata Ibu",
                    "Tabel Biodata Anak",
                    "Tabel Data Cabang",
                    "Tabel Hasil Pemeriksaan",
                ],
                icons=[
                    "caret-right-fill",
                    "caret-right-fill",
                    "caret-right-fill",
                    "caret-right-fill",
                    "caret-right-fill",
                    "caret-right-fill",
                    "caret-right-fill",
                ],
                menu_icon="house",
                default_index=0,
                styles={
                    "icon": {"color": "white", "font-size": "13px"},
                    "nav-link": {
                        "font-size": "13px",
                        "text-align": "left",
                        "margin": "0px",
                        "--hover-color": "#666",
                        "font-family": "'Arial', sans-serif",
                    },
                    "menu-title": {
                        "font-size": "16px",
                    },
                },
            )
        selected_page = pages_dict

        # Memeriksa jika pilihan adalah "Tabel Admin"
        if selected_page == "Tabel Admin":
            module_path = f"halaman.admin"  # Hapus ekstensi .py
            spec = importlib.util.spec_from_file_location(
                "admin",  # Ganti 'pages_dict[pages_dict]' dengan nama modul yang benar
                os.path.join("halaman", "admin.py"),
            )
            selected_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(selected_module)
            selected_module.main()
        elif selected_page == "Tabel Biodata Pemeriksa":
            module_path = f"halaman.pemeriksa"  # Hapus ekstensi .py
            spec = importlib.util.spec_from_file_location(
                "admin",  # Ganti 'pages_dict[pages_dict]' dengan nama modul yang benar
                os.path.join("halaman", "pemeriksa.py"),
            )
            selected_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(selected_module)
            selected_module.main()
        elif selected_page == "Tabel Biodata Ibu":
            module_path = f"halaman.ibu"  # Hapus ekstensi .py
            spec = importlib.util.spec_from_file_location(
                "admin",  # Ganti 'pages_dict[pages_dict]' dengan nama modul yang benar
                os.path.join("halaman", "ibu.py"),
            )
            selected_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(selected_module)
            selected_module.main()
        elif selected_page == "Tabel Biodata Anak":
            module_path = f"halaman.anak"  # Hapus ekstensi .py
            spec = importlib.util.spec_from_file_location(
                "admin",  # Ganti 'pages_dict[pages_dict]' dengan nama modul yang benar
                os.path.join("halaman", "anak.py"),
            )
            selected_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(selected_module)
            selected_module.main()
        elif selected_page == "Tabel Data Cabang":
            module_path = f"halaman.cabang"  # Hapus ekstensi .py
            spec = importlib.util.spec_from_file_location(
                "admin",  # Ganti 'pages_dict[pages_dict]' dengan nama modul yang benar
                os.path.join("halaman", "cabang.py"),
            )
            selected_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(selected_module)
            selected_module.main()
        elif selected_page == "Tabel Hasil Pemeriksaan":
            module_path = f"halaman.pemeriksaan"  # Hapus ekstensi .py
            spec = importlib.util.spec_from_file_location(
                "admin",  # Ganti 'pages_dict[pages_dict]' dengan nama modul yang benar
                os.path.join("halaman", "pemeriksaan.py"),
            )
            selected_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(selected_module)
            selected_module.main()

        elif pages_dict == "Dashboard":
            intro(None)  # No need for user_id here

    if st.session_state.logged_in and st.sidebar.button("Log Out"):
        st.session_state.logged_in = False
        time.sleep(1)
        st.rerun()


st.markdown("")
st.markdown("")
st.caption("Copyright (c) - Created by kelompok 2 (Basis Data) - 2024")
