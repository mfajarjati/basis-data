import streamlit as st
import pandas as pd
from halaman.koneksi import create_connection
import datetime

connection, cursor = create_connection()


# @st.cache_data
def show():
    import pandas as pd
    import streamlit as st

    display_query = """
        SELECT id_ibu as "ID Ibu",
        nama as Nama,
        tempat_lahir as "Tempat Lahir",
        tgl_lahir as "Tanggal Lahir",
        alamat as Alamat,
        telepon as Telepon,
        nik as "NIK"
        FROM ibu
    """
    cursor.execute(display_query)
    save_display = cursor.fetchall()
    # st.markdown("")
    st.subheader("Data :green[Tabel Ibu] saat ini !")
    df = pd.DataFrame(
        save_display,
        columns=[
            "ID Ibu",
            "Nama",
            "Tempat Lahir",
            "Tanggal Lahir",
            "Alamat",
            "Telepon",
            "NIK",
        ],
    )
    df.set_index("ID Ibu", inplace=True)
    st.dataframe(df, use_container_width=True)


def insert():
    # function to insert data
    # st.markdown("")
    awal = datetime.date(1800, 1, 1)
    akhir = datetime.date(2024, 1, 1)
    st.subheader("Silahkan Masukkan :green[Data Ibu] ! ")
    nama = st.text_input("nama : ")
    tempat_lahir = st.text_input("tempat lahir : ")
    tanggal_lahir = st.date_input(
        "tanggal lahir : ", value=None, min_value=(awal), max_value=(akhir)
    )
    alamat = st.text_area("alamat : ")
    telepon = st.text_input("telepon : ")
    nik = st.text_input("NIK : ")

    # Mendapatkan nama admin dari st.selectbox
    st.subheader("")
    st.subheader("", divider="green")
    cursor.execute("SELECT nama FROM admin")
    nama_admins = [result[0] for result in cursor.fetchall()]
    selected_admin = st.selectbox("Pilih Admin:", nama_admins)

    data_complete = (
        nama != ""
        and tempat_lahir != ""
        and tanggal_lahir != ""
        and alamat != ""
        and telepon != ""
        and nik != ""
    )

    if data_complete and st.button("Insert"):
        # Mengambil id_admin berdasarkan nama admin yang dipilih
        get_admin_id_query = """
            SELECT id_admin FROM admin WHERE nama = %s
        """
        cursor.execute(get_admin_id_query, (selected_admin,))
        admin_id = cursor.fetchone()

        if admin_id:
            admin_id = admin_id[0]

            # Memasukkan data ibu ke database
            data_in = """
                INSERT INTO ibu (nama, tempat_lahir, tgl_lahir, alamat, telepon, nik, id_admin) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            value = (nama, tempat_lahir, tanggal_lahir, alamat, telepon, nik, admin_id)
            cursor.execute(data_in, value)
            connection.commit()
            st.success("Data Telah Dimasukkan")
        else:
            st.warning("Nama admin tidak ditemukan!")
    elif not data_complete:
        st.warning("Harap isi semua bidang sebelum memasukkan data!")


def update():
    # function to update data
    command = """SELECT id_ibu, nama from ibu"""
    cursor.execute(command)
    id_data = cursor.fetchall()

    # Membuat daftar opsi dengan format 'id_ibu - nama'
    id_options = [f"{result[0]} - {result[1]}" for result in id_data]

    st.subheader("Silahkan pilih :green[Nama Ibu] yang akan di-update !")
    select_id = st.selectbox(
        "Nama Ibu: ", id_options, format_func=lambda x: x.split(" - ")[1]
    )

    # Mendapatkan hanya id_ibu dari opsi yang dipilih
    selected_ibu_id = int(select_id.split(" - ")[0]) if select_id else None

    if selected_ibu_id is not None:
        awal = datetime.date(1800, 1, 1)
        akhir = datetime.date(2024, 1, 1)
        st.subheader("")
        st.subheader("Silahkan Masukkan :green[Data Ibu] yang Baru: ")
        update_nama = st.text_input("nama : ")
        update_tempat_lahir = st.text_input("tempat lahir : ")
        update_tanggal_lahir = st.date_input(
            "tanggal lahir : ", value=None, min_value=(awal), max_value=(akhir)
        )
        update_alamat = st.text_area("alamat : ")
        update_telepon = st.text_input("telepon : ")
        update_nik = st.text_input("NIK : ")
        st.subheader("")
        st.subheader("", divider="green")
        cursor.execute("SELECT nama FROM admin")
        nama_admins = [result[0] for result in cursor.fetchall()]
        selected_admin = st.selectbox("Pilih Admin:", nama_admins)

        data_complete = (
            update_nama != ""
            and update_tempat_lahir != ""
            and update_tanggal_lahir != ""
            and update_alamat != ""
            and update_telepon != ""
            and update_nik != ""
        )

        # Define update_comd here before the if statement
        update_comd = """
            UPDATE ibu
            SET nama = %s, tempat_lahir = %s, tgl_lahir = %s, alamat = %s, telepon = %s, nik = %s, id_admin = %s
            WHERE id_ibu = %s
        """

        if data_complete and st.button("Update"):
            # Mengambil id_admin dari st.selectbox
            # Mengambil id_admin berdasarkan nama admin yang dipilih
            get_admin_id_query = """
                SELECT id_admin FROM admin WHERE nama = %s
            """
            cursor.execute(get_admin_id_query, (selected_admin,))
            admin_id = cursor.fetchone()

            if admin_id:
                admin_id = admin_id[0]

                # Update data pada tabel ibu
                val = (
                    update_nama,
                    update_tempat_lahir,
                    update_tanggal_lahir,
                    update_alamat,
                    update_telepon,
                    update_nik,
                    admin_id,
                    selected_ibu_id,
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
    command = """SELECT id_ibu, nama from ibu"""
    cursor.execute(command)
    id_data = cursor.fetchall()

    # Membuat daftar opsi dengan format 'id_admin - nama'
    id_options = [f"{result[0]} - {result[1]}" for result in id_data]

    st.subheader("Silahkan pilih :green[Nama Ibu] yang akan di hapus !")
    select_id = st.selectbox(
        "Nama Ibu: ", id_options, format_func=lambda x: x.split(" - ")[1]
    )

    # Mendapatkan hanya id_admin dari opsi yang dipilih
    selected_ibu_id = int(select_id.split(" - ")[0]) if select_id else None

    if selected_ibu_id:
        st.subheader("")
        st.markdown("Data Ibu :")
        display_query = """
        SELECT id_ibu as "ID Ibu",
        nama as Nama,
        tempat_lahir as "Tempat Lahir",
        tgl_lahir as "Tanggal Lahir",
        alamat as Alamat,
        telepon as Telepon,
        nik as "NIK"
        FROM ibu
        WHERE id_ibu = %s
        """
        cursor.execute(display_query, (selected_ibu_id,))
        save_display = cursor.fetchall()

        df = pd.DataFrame(
            save_display,
            columns=[
                "ID Ibu",
                "Nama",
                "Tempat Lahir",
                "Tanggal Lahir",
                "Alamat",
                "Telepon",
                "NIK",
            ],
        )
        df.set_index("ID Ibu", inplace=True)
        st.dataframe(df, use_container_width=True)

        if st.button("Delete"):
            delete_comd = """
                DELETE FROM ibu
                WHERE id_ibu = %s
            """
            cursor.execute(delete_comd, (selected_ibu_id,))
            connection.commit()
            st.success("Data Telah Dihapus")
    else:
        st.warning("Silahkan Masukkan Data terlebih dahulu")


def main():
    st.title("Dashboard :green[Tabel Ibu] 👩🏻")
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
