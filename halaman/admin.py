import streamlit as st
import pandas as pd
import pdfkit
from halaman.koneksi import create_connection

connection, cursor = create_connection()

# Konfigurasi PDF kit
config = pdfkit.configuration(
    wkhtmltopdf="C://Program Files//wkhtmltopdf//bin//wkhtmltopdf.exe"
)
bootstrap_stylesheet = (
    "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
)


def save_to_pdf(html_content):
    # Tambahkan stylesheet Bootstrap ke dalam HTML content
    html_with_bootstrap = f"""
    <html>
        <head>
            <link rel="stylesheet" href="{bootstrap_stylesheet}">
            <style>
                .text-center {{
                    text-align: center;
                }}
                .bold {{
                    font-weight: bold;
                }}
            </style>
        </head>
        <body>
            <h3 class="text-center bold">Laporan Admin Posyandu</h3>
            {html_content}
        </body>
    </html>
    """

    options = {
        "page-size": "A4",
        "margin-top": "0.75in",
        "margin-right": "0.75in",
        "margin-bottom": "0.75in",
        "margin-left": "0.75in",
    }
    pdf_file = "tabel_admin.pdf"
    pdfkit.from_string(
        html_with_bootstrap, pdf_file, options=options, configuration=config
    )
    return pdf_file


# @st.cache_data
def show():
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
    modified_data = []
    for row in save_display:
        modified_row = list(row)
        # Modifying the 'ID Admin' column
        modified_row[0] = f"ADM-{modified_row[0]}"
        modified_data.append(modified_row)

    df = pd.DataFrame(
        modified_data,
        columns=["ID Admin", "Nama", "Username", "Password"],
    )
    df.set_index("ID Admin", inplace=True)
    st.subheader("Silahkan pilih :blue[Filter] :")
    with st.expander("Filter Kolom"):
        st.subheader("Pilih :blue[kolom untuk ditampilkan] :")
        if not df.empty:
            selected_columns = st.multiselect(
                "Pilih kolom:",
                df.columns.tolist(),
                default=df.columns.tolist(),
            )

    st.subheader("Data :blue[Tabel Admin] saat ini !")
    st.dataframe(df[selected_columns], use_container_width=True)
    if set(selected_columns).issubset(df.columns):
        if st.button("Simpan ke PDF"):
            html_content = df[selected_columns].to_html(
                index=False,
                justify="left",
                classes="table table-bordered table-striped table-hover",
            )
            pdf_file = save_to_pdf(
                html_content
            )  # Anda perlu mengimplementasikan fungsi ini
            with open(pdf_file, "rb") as file:
                st.download_button(
                    label="Download PDF",
                    data=file.read(),
                    file_name=pdf_file,
                    mime="application/pdf",
                )


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
        modified_data = []
        for row in save_display:
            modified_row = list(row)
            # Modifying the 'ID Admin' column
            modified_row[0] = f"ADM-{modified_row[0]}"
            modified_data.append(modified_row)

        df = pd.DataFrame(
            modified_data,
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
        "Menu : ", ["DISPLAY", "INSERT", "UPDATE", "DELETE"], key="admin_key"
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
