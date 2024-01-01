import streamlit as st
import pandas as pd
import datetime
from halaman.koneksi import create_connection

connection, cursor = create_connection()


# @st.cache_data
def show():
    display_query = """
        SELECT p.id_periksa as "ID Periksa",
        p.tgl as "Waktu",
        i.nama as "Nama Ibu",
        a.nama as "Nama Anak",
        p.hasil_anak as "Hasil Anak",
        p.hasil_ibu as "Hasil Ibu",
        p.keterangan as Keterangan,
        pr.nama as "Pemeriksa",
        c.nama_cabang as "Nama Cabang"
        FROM periksa p
        LEFT JOIN ibu i ON p.id_ibu = i.id_ibu
        LEFT JOIN anak a ON p.id_anak = a.id_anak
        LEFT JOIN pemeriksa pr ON p.id_pemeriksa = pr.id_pemeriksa
        LEFT JOIN cabang c ON p.id_cabang = c.id_cabang
    """
    cursor.execute(display_query)
    save_display = cursor.fetchall()
    st.subheader("Data :gray[Tabel Pemeriksaan] saat ini !")
    df = pd.DataFrame(
        save_display,
        columns=[
            "ID Periksa",
            "Waktu",
            "Nama Ibu",
            "Nama Anak",
            "Hasil Anak",
            "Hasil Ibu",
            "Keterangan",
            "Pemeriksa",
            "Nama Cabang",
        ],
    )
    df.set_index("ID Periksa", inplace=True)
    st.dataframe(df, use_container_width=True)


def insert():
    st.subheader("Silahkan Masukkan :gray[Data Pemeriksaan] ! ")
    awal = datetime.date(1900, 1, 1)
    akhir = datetime.date(2025, 1, 1)
    tgl = st.date_input(
        "Masukkan Tanggal Pemeriksaan:", value=None, min_value=(awal), max_value=(akhir)
    )
    hasil_anak = st.text_input("Hasil Anak : ")
    hasil_ibu = st.text_input("Hasil Ibu : ")
    keterangan = st.text_area("Keterangan : ")

    st.subheader("")
    st.subheader("", divider="gray")
    # Mendapatkan nama admin dari st.selectbox
    cursor.execute("SELECT nama FROM admin")
    nama_admins = [result[0] for result in cursor.fetchall()]
    selected_admin = st.selectbox("Pilih Admin:", nama_admins)

    # Mendapatkan nama ibu dari st.selectbox
    cursor.execute("SELECT nama FROM ibu")
    nama_ibus = [result[0] for result in cursor.fetchall()]
    selected_ibu = st.selectbox("Pilih Ibu:", nama_ibus)

    # Mendapatkan nama anak dari st.selectbox
    cursor.execute("SELECT nama FROM anak")
    nama_anaks = [result[0] for result in cursor.fetchall()]
    selected_anak = st.selectbox("Pilih Anak:", nama_anaks)

    # Mendapatkan nama pemeriksa dari st.selectbox
    cursor.execute("SELECT nama FROM pemeriksa")
    nama_pemeriksas = [result[0] for result in cursor.fetchall()]
    selected_pemeriksa = st.selectbox("Pilih Pemeriksa:", nama_pemeriksas)

    cursor.execute("SELECT nama_cabang FROM cabang")
    nama_cabangs = [result[0] for result in cursor.fetchall()]
    selected_cabangs = st.selectbox("Pilih Cabang:", nama_cabangs)

    data_complete = (
        tgl != "" and hasil_anak != "" and hasil_ibu != "" and keterangan != ""
    )

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

        # Mengambil id_anak berdasarkan nama anak yang dipilih
        get_anak_id_query = """
            SELECT id_anak FROM anak WHERE nama = %s
        """
        cursor.execute(get_anak_id_query, (selected_anak,))
        anak_id = cursor.fetchone()

        # Mengambil id_pemeriksa berdasarkan nama pemeriksa yang dipilih
        get_pemeriksa_id_query = """
            SELECT id_pemeriksa FROM pemeriksa WHERE nama = %s
        """
        cursor.execute(get_pemeriksa_id_query, (selected_pemeriksa,))
        pemeriksa_id = cursor.fetchone()

        get_cabang_id_query = """
            SELECT id_cabang FROM cabang WHERE nama_cabang = %s
        """
        cursor.execute(get_cabang_id_query, (selected_cabangs,))
        cabang_id = cursor.fetchone()

        if admin_id and ibu_id and anak_id and pemeriksa_id and cabang_id:
            admin_id = admin_id[0]
            ibu_id = ibu_id[0]
            anak_id = anak_id[0]
            pemeriksa_id = pemeriksa_id[0]
            cabang_id = cabang_id[0]

            # Memasukkan data pemeriksaan ke database
            data_in = """
                INSERT INTO periksa (tgl, id_ibu, id_anak, hasil_anak, hasil_ibu, keterangan, id_admin, id_pemeriksa, id_cabang) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            value = (
                tgl,
                ibu_id,
                anak_id,
                hasil_anak,
                hasil_ibu,
                keterangan,
                admin_id,
                pemeriksa_id,
                cabang_id,
            )
            cursor.execute(data_in, value)
            connection.commit()
            st.success("Data Telah Dimasukkan")
        else:
            st.warning("Data yang dipilih tidak ditemukan!")
    elif not data_complete:
        st.warning("Harap isi semua bidang sebelum memasukkan data!")


def update():
    command = """ SELECT id_periksa FROM periksa """
    cursor.execute(command)
    id_data = cursor.fetchall()

    # Membuat daftar opsi dengan format 'id_pemeriksa - tgl - nama_anak - nama_ibu'
    # Membuat daftar opsi hanya dengan 'id_pemeriksa'
    id_options = [result[0] for result in id_data]

    st.subheader("Silahkan pilih :gray[Data Pemeriksaan] yang akan di-update !")
    select_id = st.selectbox("ID Pemeriksaan: ", id_options)

    # Mendapatkan hanya id_periksa dari opsi yang dipilih
    selected_periksa_id = select_id if select_id else None
    if selected_periksa_id is not None:
        awal = datetime.date(1800, 1, 1)
        akhir = datetime.date(2025, 1, 1)
        st.subheader("")
        st.subheader("Silahkan Masukkan :gray[Data Pemeriksaan] yang Baru ! ")
        update_tgl = st.date_input(
            "Tanggal Pemeriksaan : ", value=None, min_value=(awal), max_value=(akhir)
        )
        update_hasil_anak = st.text_input("Hasil Anak : ")
        update_hasil_ibu = st.text_input("Hasil Ibu : ")
        update_keterangan = st.text_area("Keterangan : ")

        st.subheader("")
        st.subheader("", divider="gray")

        cursor.execute("SELECT nama FROM anak")
        nama_anaks = [result[0] for result in cursor.fetchall()]
        selected_anak = st.selectbox("Pilih Anak:", nama_anaks)

        cursor.execute("SELECT nama FROM ibu")
        nama_ibus = [result[0] for result in cursor.fetchall()]
        selected_ibu = st.selectbox("Pilih Ibu:", nama_ibus)

        cursor.execute("SELECT nama FROM admin")
        nama_admins = [result[0] for result in cursor.fetchall()]
        selected_admin = st.selectbox("Pilih Admin:", nama_admins)

        cursor.execute("SELECT nama FROM pemeriksa")
        nama_pemeriksas = [result[0] for result in cursor.fetchall()]
        selected_pemeriksa = st.selectbox("Pilih Pemeriksa:", nama_pemeriksas)

        cursor.execute("SELECT nama_cabang FROM cabang")
        nama_cabangs = [result[0] for result in cursor.fetchall()]
        selected_cabangs = st.selectbox("Pilih Cabang:", nama_cabangs)

        data_complete = (
            update_tgl != ""
            and update_hasil_anak != ""
            and update_hasil_ibu != ""
            and update_keterangan != ""
        )

        update_comd = """
            UPDATE periksa
            SET tgl = %s, id_anak = %s, id_ibu = %s, hasil_anak = %s, hasil_ibu = %s, keterangan = %s, id_admin = %s, id_pemeriksa = %s, id_cabang = %s
            WHERE id_periksa = %s
        """

        if data_complete and st.button("Update"):
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

            # Mengambil id_anak berdasarkan nama anak yang dipilih
            get_anak_id_query = """
            SELECT id_anak FROM anak WHERE nama = %s
        """
            cursor.execute(get_anak_id_query, (selected_anak,))
            anak_id = cursor.fetchone()

            # Mengambil id_pemeriksa berdasarkan nama pemeriksa yang dipilih
            get_pemeriksa_id_query = """
            SELECT id_pemeriksa FROM pemeriksa WHERE nama = %s
        """
            cursor.execute(get_pemeriksa_id_query, (selected_pemeriksa,))
            pemeriksa_id = cursor.fetchone()

            get_cabang_id_query = """
            SELECT id_cabang FROM cabang WHERE nama_cabang = %s
        """
            cursor.execute(get_cabang_id_query, (selected_cabangs,))
            cabang_id = cursor.fetchone()

            if admin_id and ibu_id and anak_id and pemeriksa_id and cabang_id:
                admin_id = admin_id[0]
                ibu_id = ibu_id[0]
                anak_id = anak_id[0]
                pemeriksa_id = pemeriksa_id[0]
                cabang_id = cabang_id[0]

                value = (
                    update_tgl,
                    anak_id,
                    ibu_id,
                    update_hasil_anak,
                    update_hasil_ibu,
                    update_keterangan,
                    admin_id,
                    pemeriksa_id,
                    cabang_id,
                    selected_periksa_id,
                )
                cursor.execute(update_comd, value)
                connection.commit()
                st.success("Data Telah Di-Update")
            else:
                st.warning("Data yang dipilih tidak ditemukan!")
        elif not data_complete:
            st.warning("Harap isi semua bidang sebelum memasukkan data!")


def delete():
    # function for deleting data
    command = """
        SELECT id_periksa
        FROM periksa 
    """
    cursor.execute(command)
    id_data = cursor.fetchall()
    # Membuat daftar opsi hanya dengan 'id_pemeriksa'
    id_options = [result[0] for result in id_data]

    st.subheader("Silahkan pilih :gray[Data Pemeriksaan] yang akan di-update !")
    select_id = st.selectbox("ID Pemeriksaan: ", id_options)

    # Mendapatkan hanya id_periksa dari opsi yang dipilih
    selected_periksa_id = select_id if select_id else None

    if selected_periksa_id:
        st.subheader("")
        display_query = """
        SELECT p.id_periksa as "ID Periksa",
        p.tgl as "Waktu",
        i.nama as "Nama Ibu",
        a.nama as "Nama Anak",
        p.hasil_anak as "Hasil Anak",
        p.hasil_ibu as "Hasil Ibu",
        p.keterangan as Keterangan,
        pr.nama as "Pemeriksa",
        c.nama_cabang as "Nama Cabang"
        FROM periksa p
        LEFT JOIN ibu i ON p.id_ibu = i.id_ibu
        LEFT JOIN anak a ON p.id_anak = a.id_anak
        LEFT JOIN pemeriksa pr ON p.id_pemeriksa = pr.id_pemeriksa
        LEFT JOIN cabang c ON p.id_cabang = c.id_cabang
        WHERE id_periksa = %s
    """
        cursor.execute(display_query, (selected_periksa_id,))
        save_display = cursor.fetchall()
        st.markdown("Data Pemeriksaan :")
        df = pd.DataFrame(
            save_display,
            columns=[
                "ID Periksa",
                "Waktu",
                "Nama Ibu",
                "Nama Anak",
                "Hasil Anak",
                "Hasil Ibu",
                "Keterangan",
                "Pemeriksa",
                "Nama Cabang",
            ],
        )
        df.set_index("ID Periksa", inplace=True)
        st.dataframe(df, use_container_width=True)

        if selected_periksa_id is not None and st.button("Delete"):
            delete_query = "DELETE FROM periksa WHERE id_periksa = %s"
            cursor.execute(delete_query, (selected_periksa_id,))
            connection.commit()
            st.success("Data Telah Dihapus")
    else:
        st.warning("Silahkan Masukkan Data Pemeriksaan terlebih dahulu")


def main():
    st.title("Dashboard :gray[Tabel Pemeriksaan] 📋")
    st.header("", divider="rainbow")
    page = st.sidebar.selectbox(
        "Menu : ", ["DISPLAY", "INSERT", "UPDATE", "DELETE"], key="pemeriksaan_key"
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
