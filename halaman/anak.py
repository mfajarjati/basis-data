import streamlit as st
import pandas as pd
import datetime
from halaman.koneksi import create_connection

connection, cursor = create_connection()


# @st.cache_data
def show():
    display_query = """
        SELECT id_anak as "ID Anak",
        nama as Nama,
        tempat_lahir as "Tempat Lahir",
        tgl_lahir as "Tanggal Lahir"
        FROM anak
    """
    cursor.execute(display_query)
    save_display = cursor.fetchall()
    # st.markdown("")
    st.subheader("Data :orange[Tabel Anak] saat ini !")
    modified_data = []
    for row in save_display:
        modified_row = list(row)
        # Modifying the 'ID Admin' column
        modified_row[0] = f"CHI-{modified_row[0]}"
        modified_data.append(modified_row)
    df = pd.DataFrame(
        modified_data,
        columns=[
            "ID Anak",
            "Nama",
            "Tempat Lahir",
            "Tanggal Lahir",
        ],
    )
    df.set_index("ID Anak", inplace=True)
    st.dataframe(df, use_container_width=True)


def insert():
    # function to insert data
    # st.markdown("")
    awal = datetime.date(2000, 1, 1)
    akhir = datetime.date(2025, 1, 1)
    st.subheader("Silahkan Masukkan :orange[Data Anak] ! ")
    nama = st.text_input("nama:")
    tempat_lahir = st.text_input("tempat lahir : ")
    tgl_lahir = st.date_input(
        "tgl lahir : ", value=None, min_value=(awal), max_value=(akhir)
    )

    # Mendapatkan nama admin dari st.selectbox
    st.subheader("")
    st.subheader("", divider="orange")
    cursor.execute("SELECT nama FROM admin")
    nama_admins = [result[0] for result in cursor.fetchall()]
    selected_admin = st.selectbox("Pilih Admin:", nama_admins)

    # Mendapatkan nama ibu dari st.selectbox
    cursor.execute("SELECT nama FROM ibu")
    nama_ibus = [result[0] for result in cursor.fetchall()]
    selected_ibu = st.selectbox("Pilih Ibu:", nama_ibus)

    data_complete = nama != "" and tempat_lahir != "" and tgl_lahir != ""

    if data_complete and st.button("Insert"):
        # Mengambil id_admin berdasarkan nama admin yang dipilih
        get_admin_id_query = """
            SELECT id_admin FROM admin WHERE nama = %s
        """
        cursor.execute(get_admin_id_query, (selected_admin,))
        admin_id = cursor.fetchone()

        # Mengambil id_ibu berdasarkan nama ibu yang dipilih
        get_ibu_id_query = """
            SELECT id_ibu FROM ibu WHERE nama = %s
        """
        cursor.execute(get_ibu_id_query, (selected_ibu,))
        ibu_id = cursor.fetchone()

        if admin_id and ibu_id:
            admin_id = admin_id[0]
            ibu_id = ibu_id[0]

            # Memasukkan data anak ke database
            data_in = """
                INSERT INTO anak (nama, tempat_lahir, tgl_lahir, id_admin, id_ibu) 
                VALUES (%s, %s, %s, %s, %s)
            """
            value = (nama, tempat_lahir, tgl_lahir, admin_id, ibu_id)
            cursor.execute(data_in, value)
            connection.commit()
            st.success("Data Telah Dimasukkan")
        else:
            st.warning("Nama admin atau ibu tidak ditemukan!")
    elif not data_complete:
        st.warning("Harap isi semua bidang sebelum memasukkan data!")


def update():
    # function to update data
    command = """SELECT id_anak, nama from anak"""
    cursor.execute(command)
    id_data = cursor.fetchall()

    # Membuat daftar opsi dengan format 'id_ibu - nama'
    id_options = [f"{result[0]} - {result[1]}" for result in id_data]

    st.subheader("Silahkan pilih :orange[Nama Anak] yang akan di-update !")
    select_id = st.selectbox(
        "Nama Anak: ", id_options, format_func=lambda x: x.split(" - ")[1]
    )

    # Mendapatkan hanya id_ibu dari opsi yang dipilih
    selected_anak_id = int(select_id.split(" - ")[0]) if select_id else None

    if selected_anak_id is not None:
        awal = datetime.date(2000, 1, 1)
        akhir = datetime.date(2025, 1, 1)
        st.subheader("")
        st.subheader("Silahkan Masukkan :orange[Data Anak] yang Baru ! ")
        update_nama = st.text_input("nama : ")
        update_tempat_lahir = st.text_input("tempat lahir : ")
        update_tanggal_lahir = st.date_input(
            "tanggal lahir : ", value=None, min_value=(awal), max_value=(akhir)
        )

        st.subheader("")
        st.subheader("", divider="orange")

        cursor.execute("SELECT nama FROM admin")
        nama_admins = [result[0] for result in cursor.fetchall()]
        selected_admin = st.selectbox("Pilih Admin:", nama_admins)

        cursor.execute("SELECT nama FROM ibu")
        nama_ibus = [result[0] for result in cursor.fetchall()]
        selected_ibu = st.selectbox("Pilih Ibu:", nama_ibus)

        data_complete = (
            update_nama != ""
            and update_tempat_lahir != ""
            and update_tanggal_lahir != ""
        )

        # Define update_comd here before the if statement
        update_comd = """
            UPDATE anak
            SET nama = %s, tempat_lahir = %s, tgl_lahir = %s, id_ibu = %s, id_admin = %s
            WHERE id_anak = %s
        """

        if data_complete and st.button("Update"):
            # Mengambil id_admin dari st.selectbox
            # Mengambil id_admin berdasarkan nama admin yang dipilih
            get_admin_id_query = """
                SELECT id_admin FROM admin WHERE nama = %s
            """
            cursor.execute(get_admin_id_query, (selected_admin,))
            admin_id = cursor.fetchone()

            get_ibu_id_query = """
            SELECT id_ibu FROM ibu WHERE nama = %s
        """
            cursor.execute(get_ibu_id_query, (selected_ibu,))
            ibu_id = cursor.fetchone()

            if admin_id and ibu_id:
                admin_id = admin_id[0]
                ibu_id = ibu_id[0]

                # Update data pada tabel ibu
                val = (
                    update_nama,
                    update_tempat_lahir,
                    update_tanggal_lahir,
                    ibu_id,
                    admin_id,
                    selected_anak_id,
                )
                cursor.execute(update_comd, val)
                connection.commit()
                st.success("Data Telah di-Update")
            else:
                st.warning("Nama admin tidak ditemukan!")
        elif not data_complete:
            st.warning("Harap isi semua bidang sebelum memasukkan data!")


def delete():
    # function for deleting data
    command = """SELECT id_anak, nama from anak"""
    cursor.execute(command)
    id_data = cursor.fetchall()

    # Membuat daftar opsi dengan format 'id_anak - nama'
    id_options = [f"{result[0]} - {result[1]}" for result in id_data]

    st.subheader("Silahkan pilih :orange[Nama Anak] yang akan di hapus !")
    select_id = st.selectbox(
        "Nama Anak: ", id_options, format_func=lambda x: x.split(" - ")[1]
    )

    # Mendapatkan hanya id_anak dari opsi yang dipilih
    selected_anak_id = int(select_id.split(" - ")[0]) if select_id else None

    if selected_anak_id:
        st.subheader("")
        st.markdown("Data Anak :")
        display_query = """
        SELECT id_anak as "ID Anak",
        nama as Nama,
        tempat_lahir as "Tempat Lahir",
        tgl_lahir as "Tanggal Lahir"
        FROM anak
        WHERE id_anak = %s
        """
        cursor.execute(display_query, (selected_anak_id,))
        save_display = cursor.fetchall()
        # st.markdown("")
        df = pd.DataFrame(
            save_display,
            columns=[
                "ID Anak",
                "Nama",
                "Tempat Lahir",
                "Tanggal Lahir",
            ],
        )
        df.set_index("ID Anak", inplace=True)
        st.dataframe(df, use_container_width=True)

        if st.button("Delete"):
            delete_comd = """
                DELETE FROM anak
                WHERE id_anak = %s
            """
            cursor.execute(delete_comd, (selected_anak_id,))
            connection.commit()
            st.success("Data Telah Dihapus")
    else:
        st.warning("Silahkan Pilih Nama Anak terlebih dahulu")


def main():
    st.title("Dashboard :orange[Tabel Anak] 👶🏻")
    st.header("", divider="rainbow")
    page = st.sidebar.selectbox(
        "Menu : ", ["DISPLAY", "INSERT", "UPDATE", "DELETE"], key="ibu_key"
    )

    if page == "DISPLAY":
        show()

    elif page == "INSERT":
        insert()

    elif page == "UPDATE":
        update()

    elif page == "DELETE":
        delete()


if __name__ == "__main__":
    main()
    st.markdown("")
    st.markdown("")
    st.caption("Copyright (c) - Created by kelompok 2 (Basis Data) - 2024")
