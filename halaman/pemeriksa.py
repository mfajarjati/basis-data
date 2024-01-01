import streamlit as st
import pandas as pd
from halaman.koneksi import create_connection

connection, cursor = create_connection()


# @st.cache_data
def show():
    display_query = """
        SELECT id_pemeriksa as "ID Pemeriksa",
        nama as "Nama Pemeriksa",
        jabatan as "Jabatan",
        jk_pemeriksa as "Jenis Kelamin",
        telepon as Telepon,
        alamat as Alamat
        FROM pemeriksa
    """
    cursor.execute(display_query)
    save_display = cursor.fetchall()
    # st.markdown("")
    st.subheader(
        "Data :violet[Tabel Pemeriksa] saat ini !",
    )
    df = pd.DataFrame(
        save_display,
        columns=[
            "ID Pemeriksa",
            "Nama pemeriksa",
            "Jabatan",
            "Jenis Kelamin",
            "Telepon",
            "Alamat",
        ],
    )
    df.set_index("ID Pemeriksa", inplace=True)
    st.dataframe(df, use_container_width=True)


def insert():
    # function to insert data
    # st.markdown("")
    st.subheader("Silahkan Masukkan :violet[Data Pemeriksa] ! ")
    nama = st.text_input("Nama pemeriksa : ")
    jabatan = st.text_input("Jabatan : ")
    jk_pemeriksa = st.radio("Jenis Kelamin : ", ["Laki-Laki", "Perempuan"], index=None)
    telepon = st.text_input("Telepon : ")
    alamat = st.text_area("Alamat : ")

    data_complete = (
        nama != ""
        and jabatan != ""
        and jk_pemeriksa != ""
        and telepon != ""
        and alamat != ""
    )
    if data_complete and st.button(
        "Insert",
    ):
        data_in = """
            INSERT INTO pemeriksa (nama, jabatan, jk_pemeriksa, telepon, alamat) VALUES (%s, %s, %s, %s, %s)
        """
        value = (nama, jabatan, jk_pemeriksa, telepon, alamat)
        # cursor.execute is to execute the mysql command
        cursor.execute(data_in, value)
        # connection.commit is to save the changes
        connection.commit()
        st.success("Data Telah Dimasukkan")
    elif not data_complete:
        st.warning("Harap isi semua bidang sebelum memasukkan data!")


def update():
    # function to update data
    command = """SELECT id_pemeriksa, nama from pemeriksa"""
    cursor.execute(command)
    id_data = cursor.fetchall()

    # Membuat daftar opsi dengan format 'id_pemeriksa - nama'
    id_options = [f"{result[0]} - {result[1]}" for result in id_data]

    st.subheader("Silahkan pilih :violet[Nama Pemeriksa] yang akan di-update !")
    select_id = st.selectbox(
        "Nama Pemeriksa: ", id_options, format_func=lambda x: x.split(" - ")[1]
    )

    # Mendapatkan hanya id_pemeriksa dari opsi yang dipilih
    selected_pemeriksa_id = int(select_id.split(" - ")[0]) if select_id else None

    if selected_pemeriksa_id is not None:
        st.subheader("")
        st.subheader("Silahkan Masukkan :violet[Data Pemeriksa] yang Baru: ")
        update_name = st.text_input("Nama pemeriksa: ")
        update_jabatan = st.text_input("Jabatan: ")
        update_jk = st.radio("Jenis Kelamin : ", ["Laki-Laki", "Perempuan"], index=None)
        update_telepon = st.text_input("telepon: ")
        update_alamat = st.text_area("Alamat : ")

        data_complete = (
            update_name != ""
            and update_jabatan != ""
            and update_jk != ""
            and update_telepon != ""
            and update_alamat != ""
        )

        if data_complete and st.button(
            "Update",
        ):
            update_comd = """
            UPDATE pemeriksa
            SET nama = %s, jabatan = %s, jk_pemeriksa = %s, telepon = %s, alamat = %s
            WHERE id_pemeriksa = %s
            """
            val = (
                update_name,
                update_jabatan,
                update_jk,
                update_telepon,
                update_alamat,
                selected_pemeriksa_id,
            )
            cursor.execute(update_comd, val)
            connection.commit()
            st.success("Data Telah di-Update")
        elif not data_complete:
            st.warning("Harap isi semua bidang sebelum memasukkan data!")


def delete():
    # function for deleting data
    command = """SELECT id_pemeriksa, nama from pemeriksa"""
    cursor.execute(command)
    id_data = cursor.fetchall()

    # Membuat daftar opsi dengan format 'id_pemeriksa - nama'
    id_options = [f"{result[0]} - {result[1]}" for result in id_data]

    st.subheader("Silahkan pilih :violet[Nama Pemeriksa] yang akan di hapus !")
    select_id = st.selectbox(
        "Nama Pemeriksa: ", id_options, format_func=lambda x: x.split(" - ")[1]
    )

    # Mendapatkan hanya id_pemeriksa dari opsi yang dipilih
    selected_pemeriksa_id = int(select_id.split(" - ")[0]) if select_id else None

    if selected_pemeriksa_id:
        st.subheader("")
        st.markdown("Data Pemeriksa :")
        display_query = """
        SELECT id_pemeriksa as "ID Pemeriksa",
        nama as "Nama Pemeriksa",
        jabatan as "Jabatan",
        jk_pemeriksa as "Jenis Kelamin",
        telepon as Telepon,
        alamat as Alamat
        FROM pemeriksa
        WHERE id_pemeriksa = %s
        """
        cursor.execute(display_query, (selected_pemeriksa_id,))
        save_display = cursor.fetchall()

        if len(save_display) > 0:
            df = pd.DataFrame(
                save_display,
                columns=[
                    "ID Pemeriksa",
                    "Nama Pemeriksa",
                    "Jabatan",
                    "Jenis Kelamin",
                    "Telepon",
                    "Alamat",
                ],
            )
            df.set_index("ID Pemeriksa", inplace=True)
            st.dataframe(df, use_container_width=True)

            if st.button("Delete"):
                delete_comd = """
                    DELETE FROM pemeriksa
                    WHERE id_pemeriksa = %s
                """
                cursor.execute(delete_comd, (selected_pemeriksa_id,))
                connection.commit()
                st.success("Data Telah Dihapus")
        else:
            st.warning("Data tidak ditemukan")
    else:
        st.warning("Silahkan Masukkan Data Nama Pemeriksa terlebih dahulu")


def main():
    st.title("Dashboard :violet[Tabel Pemeriksa] 🏢")
    st.header("", divider="rainbow")
    page = st.sidebar.selectbox(
        "Menu :",
        ["DISPLAY", "INSERT", "UPDATE", "DELETE"],
        key="pemeriksa_key",
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
