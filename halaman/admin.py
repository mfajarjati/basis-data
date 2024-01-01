import streamlit as st
import pandas as pd
from halaman.koneksi import create_connection

connection, cursor = create_connection()


# @st.cache_data
def show():
    import pandas as pd
    import streamlit as st

    display_query = """
        SELECT id_admin as "ID Admin",
        nama as Nama,
        username as Username,
        password as Password
        FROM admin
    """
    cursor.execute(display_query)
    save_display = cursor.fetchall()
    # st.markdown("")
    st.subheader("Data :blue[Tabel Admin] saat ini !")
    df = pd.DataFrame(
        save_display,
        columns=["ID Admin", "Nama", "Username", "Password"],
    )
    df.set_index("ID Admin", inplace=True)
    st.dataframe(df, use_container_width=True)


def insert():
    # function to insert data
    # st.markdown("")
    st.subheader("Silahkan Masukkan :blue[Data Admin] ! ")
    nama = st.text_input("nama : ")
    username = st.text_input("username : ")
    password = st.text_input("password : ", type="password")

    data_complete = nama != "" and username != "" and password != ""
    if " " in username:
        st.warning("username tidak boleh mengandung spasi!")
        return username
    if data_complete and st.button(
        "Insert",
    ):
        data_in = """
            INSERT INTO admin (nama, username, password) VALUES (%s, %s, %s)
        """
        value = (nama, username, password)
        # cursor.execute is to execute the mysql command
        cursor.execute(data_in, value)
        # connection.commit is to save the changes
        connection.commit()
        st.success("Data Telah Dimasukkan")
    elif not data_complete:
        st.warning("Harap isi semua bidang sebelum memasukkan data!")


def update():
    # function to update data
    command = """SELECT id_admin, nama from admin"""
    cursor.execute(command)
    id_data = cursor.fetchall()

    # Membuat daftar opsi dengan format 'id_admin - nama'
    id_options = [f"{result[0]} - {result[1]}" for result in id_data]

    st.subheader("Silahkan pilih :blue[Nama Admin] yang akan di-update !")
    select_id = st.selectbox(
        "Nama Admin: ", id_options, format_func=lambda x: x.split(" - ")[1]
    )

    # Mendapatkan hanya id_admin dari opsi yang dipilih
    selected_admin_id = int(select_id.split(" - ")[0]) if select_id else None

    if selected_admin_id is not None:
        st.subheader("")
        st.subheader("Silahkan Masukkan :blue[Data Admin] yang Baru: ")
        update_name = st.text_input("Nama: ")
        update_username = st.text_input("Username: ")
        update_password = st.text_input("Password: ", type="password")

        data_complete = (
            update_name != "" and update_username != "" and update_password != ""
        )

        if " " in update_username:
            st.warning("username tidak boleh mengandung spasi!")
            return update_username

        if data_complete and st.button(
            "Update",
        ):
            update_comd = """
            UPDATE admin
            SET nama = %s, username = %s, password = %s
            WHERE id_admin = %s
            """
            val = (update_name, update_username, update_password, selected_admin_id)
            cursor.execute(update_comd, val)
            connection.commit()
            st.success("Data Telah di-Update")
        elif not data_complete:
            st.warning("Harap isi semua bidang sebelum memasukkan data!")


def delete():
    # function for deleting data
    command = """SELECT id_admin, nama from admin"""
    cursor.execute(command)
    id_data = cursor.fetchall()

    # Membuat daftar opsi dengan format 'id_admin - nama'
    id_options = [f"{result[0]} - {result[1]}" for result in id_data]

    st.subheader("Silahkan pilih :blue[Nama Admin] yang akan di hapus !")
    select_id = st.selectbox(
        "Nama Admin: ", id_options, format_func=lambda x: x.split(" - ")[1]
    )

    # Mendapatkan hanya id_admin dari opsi yang dipilih
    selected_admin_id = int(select_id.split(" - ")[0]) if select_id else None

    if selected_admin_id:
        st.subheader("")
        st.markdown("Data Admin :")
        display_query = """
            SELECT * from admin where id_admin = %s
        """
        cursor.execute(display_query, (select_id,))
        save_display = cursor.fetchall()

        df = pd.DataFrame(
            save_display,
            columns=["id_admin", "nama", "username", "password"],
        )
        df.set_index("id_admin", inplace=True)
        st.dataframe(df, use_container_width=True)

        if st.button("Delete"):
            delete_comd = """
                DELETE FROM admin
                WHERE id_admin = %s
            """
            cursor.execute(delete_comd, (select_id,))
            connection.commit()
            st.success("Data Telah Dihapus")


def main():
    st.title("Dashboard :blue[Tabel Admin] 🙍🏻‍♂️")
    st.header("", divider="rainbow")
    page = st.sidebar.selectbox(
        "Select page", ["DISPLAY", "INSERT", "UPDATE", "DELETE"], key="admin_key"
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
