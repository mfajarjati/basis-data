import streamlit as st
import pandas as pd
from halaman.koneksi import create_connection

connection, cursor = create_connection()


# @st.cache_data
def show():
    display_query = """
        SELECT id_cabang as "ID Cabang",
        nama_cabang as "Nama Cabang",
        nama_owner as "Nama Owner",
        telepon as Telepon,
        alamat as Alamat
        FROM cabang
    """
    cursor.execute(display_query)
    save_display = cursor.fetchall()
    # st.markdown("")
    st.subheader("Data :red[Tabel Cabang] saat ini !")
    df = pd.DataFrame(
        save_display,
        columns=["ID Cabang", "Nama Cabang", "Nama Owner", "Telepon", "Alamat"],
    )
    df.set_index("ID Cabang", inplace=True)
    st.dataframe(df, use_container_width=True)


def insert():
    # function to insert data
    # st.markdown("")
    st.subheader("Silahkan Masukkan :red[Data Cabang] ! ")
    nama = st.text_input("Nama Cabang : ")
    owner = st.text_input("Nama Owner : ")
    telepon = st.text_input("Telepon : ")
    alamat = st.text_area("Alamat : ")

    data_complete = nama != "" and owner != "" and telepon != "" and alamat != ""
    if data_complete and st.button(
        "Insert",
    ):
        data_in = """
            INSERT INTO cabang (nama_cabang, nama_owner, telepon, alamat) VALUES (%s, %s, %s, %s)
        """
        value = (nama, owner, telepon, alamat)
        # cursor.execute is to execute the mysql command
        cursor.execute(data_in, value)
        # connection.commit is to save the changes
        connection.commit()
        st.success("Data Telah Dimasukkan")
    elif not data_complete:
        st.warning("Harap isi semua bidang sebelum memasukkan data!")


def update():
    # function to update data
    command = """SELECT id_cabang, nama_cabang from cabang"""
    cursor.execute(command)
    id_data = cursor.fetchall()

    # Membuat daftar opsi dengan format 'id_cabang - nama'
    id_options = [f"{result[0]} - {result[1]}" for result in id_data]

    st.subheader("Silahkan pilih :red[Nama Cabang] yang akan di-update !")
    select_id = st.selectbox(
        "Nama cabang: ", id_options, format_func=lambda x: x.split(" - ")[1]
    )

    # Mendapatkan hanya id_cabang dari opsi yang dipilih
    selected_cabang_id = int(select_id.split(" - ")[0]) if select_id else None

    if selected_cabang_id is not None:
        st.subheader("")
        st.subheader("Silahkan Masukkan :red[Data cabang] yang Baru: ")
        update_name = st.text_input("Nama Cabang: ")
        update_owner = st.text_input("Nama Owner: ")
        update_telepon = st.text_input("telepon: ")
        update_alamat = st.text_area("Alamat: ")

        data_complete = (
            update_name != ""
            and update_owner != ""
            and update_telepon != ""
            and update_alamat != ""
        )

        if data_complete and st.button(
            "Update",
        ):
            update_comd = """
            UPDATE cabang
            SET nama_cabang = %s, nama_owner = %s, telepon = %s, alamat = %s
            WHERE id_cabang = %s
            """
            val = (
                update_name,
                update_owner,
                update_telepon,
                update_alamat,
                selected_cabang_id,
            )
            cursor.execute(update_comd, val)
            connection.commit()
            st.success("Data Telah di-Update")
        elif not data_complete:
            st.warning("Harap isi semua bidang sebelum memasukkan data!")


def delete():
    # function for deleting data
    command = """SELECT id_cabang, nama_cabang from cabang"""
    cursor.execute(command)
    id_data = cursor.fetchall()

    # Membuat daftar opsi dengan format 'id_cabang - nama'
    id_options = [f"{result[0]} - {result[1]}" for result in id_data]

    st.subheader("Silahkan pilih :red[Nama cabang] yang akan di hapus !")
    select_id = st.selectbox(
        "Nama cabang: ", id_options, format_func=lambda x: x.split(" - ")[1]
    )

    # Mendapatkan hanya id_cabang dari opsi yang dipilih
    selected_cabang_id = int(select_id.split(" - ")[0]) if select_id else None

    if selected_cabang_id:
        st.subheader("")
        st.markdown("Data cabang :")
        display_query = """
        SELECT id_cabang as "ID Cabang",
        nama_cabang as "Nama Cabang",
        nama_owner as "Nama Owner",
        telepon as Telepon,
        alamat as Alamat
        FROM cabang
        WHERE id_cabang = %s
        """
        cursor.execute(display_query, (selected_cabang_id,))
        save_display = cursor.fetchall()

        df = pd.DataFrame(
            save_display,
            columns=["ID Cabang", "Nama Cabang", "Nama Owner", "Telepon", "Alamat"],
        )
        df.set_index("ID Cabang", inplace=True)
        st.dataframe(df, use_container_width=True)

        if st.button("Delete"):
            delete_comd = """
                DELETE FROM cabang
                WHERE id_cabang = %s
            """
            cursor.execute(delete_comd, (selected_cabang_id,))
            connection.commit()
            st.success("Data Telah Dihapus")
    else:
        st.warning("Silahkan Masukkan Data Nama Cabang terlebih dahulu")


def main():
    st.title("Dashboard :red[Tabel cabang] 🏢")
    st.header("", divider="rainbow")
    page = st.sidebar.selectbox(
        "Menu :", ["DISPLAY", "INSERT", "UPDATE", "DELETE"], key="cabang_key"
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
