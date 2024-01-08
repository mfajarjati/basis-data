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
            <h3 class="text-center bold">Laporan Cabang Posyandu</h3>
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
    pdf_file = "tabel_cabang.pdf"
    pdfkit.from_string(
        html_with_bootstrap, pdf_file, options=options, configuration=config
    )
    return pdf_file


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
    modified_data = []
    for row in save_display:
        modified_row = list(row)
        # Modifying the 'ID Admin' column
        modified_row[0] = f"CBG-{modified_row[0]}"
        modified_data.append(modified_row)
    df = pd.DataFrame(
        modified_data,
        columns=["ID Cabang", "Nama Cabang", "Nama Owner", "Telepon", "Alamat"],
    )
    df.set_index("ID Cabang", inplace=True)
    st.subheader("Silahkan pilih :red[Filter] :")
    with st.expander("Filter Kolom"):
        if not df.empty:
            selected_columns = st.multiselect(
                "Pilih kolom:",
                df.columns.tolist(),
                default=df.columns.tolist(),
            )
    st.subheader("Data :red[Tabel Cabang] saat ini !")
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

        modified_data = []
        for row in save_display:
            modified_row = list(row)
            # Modifying the 'ID Admin' column
            modified_row[0] = f"CBG-{modified_row[0]}"
            modified_data.append(modified_row)
        df = pd.DataFrame(
            modified_data,
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
