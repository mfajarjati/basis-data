-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 08, 2024 at 04:23 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `posyandu_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id_admin` int(11) NOT NULL,
  `nama` varchar(250) NOT NULL,
  `username` varchar(250) NOT NULL,
  `password` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id_admin`, `nama`, `username`, `password`) VALUES
(9, 'kelompok 2 (basis Data)', 'kelompok2', '12345678'),
(13, 'muhammad fajar jati permana', 'mfajarjati', '1w3r5y7i'),
(15, 'yosua adriel tamba', 'yosuaadrl', 'qwertyuiop'),
(16, 'mochammad Ramdhan', 'rmdhn', 'zxcvbnmasd'),
(17, 'wibi nugraha', 'wibinug', 'zmxncbvalsk'),
(18, 'muhammad fahreza', 'rezaaa', 'lkjhgfdsa');

-- --------------------------------------------------------

--
-- Table structure for table `anak`
--

CREATE TABLE `anak` (
  `id_anak` int(11) NOT NULL,
  `nama` varchar(250) NOT NULL,
  `tempat_lahir` varchar(250) NOT NULL,
  `tgl_lahir` date NOT NULL,
  `id_ibu` int(11) NOT NULL,
  `id_admin` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `anak`
--

INSERT INTO `anak` (`id_anak`, `nama`, `tempat_lahir`, `tgl_lahir`, `id_ibu`, `id_admin`) VALUES
(10, 'Janet Samosir', 'Bandung', '2023-05-28', 10, 9),
(11, 'Prabowo Putra', 'Bandung', '2021-01-27', 11, 9),
(12, 'Darman Sihombing', 'Palembang', '2022-11-07', 12, 9),
(13, 'Salsabila Kuswandari', 'Bandung', '2019-10-11', 13, 9),
(14, 'Rafi Siregar', 'Bandung', '2019-06-21', 14, 9),
(15, 'Victoria Anggraini', 'Palembang', '2020-02-03', 15, 9),
(16, 'Ajimin Saefullah', 'Kediri', '2018-11-12', 16, 9),
(17, 'Adika Melani', 'Bandung', '2019-07-01', 17, 9),
(18, 'Estiawan Lestari', 'Tangerang', '2019-08-22', 18, 9),
(19, 'Kamidin Yuliarti', 'Cimahi', '2019-01-30', 19, 9),
(20, 'Harsanto Wasita', 'Banten', '2023-03-19', 20, 9),
(21, 'Purwa Pangestu', 'Jakarta', '2019-10-03', 21, 9),
(22, 'Laila Nashiruddin', 'Jakarta', '2021-08-31', 22, 9),
(23, 'Bakiono Kuswandari', 'Jakarta', '2022-02-10', 23, 9),
(24, 'Banawa Pranowo', 'Surabaya', '2021-05-17', 24, 9),
(25, 'Maras Hardiansyah', 'Yogyakarta', '2023-04-09', 25, 9),
(26, 'Dewi Nasyidah', 'Lampung', '2019-03-06', 26, 9),
(27, 'Jagapati Prasetya', 'Bandung', '2020-12-30', 27, 9),
(28, 'Okta Mardhiyah', 'Surabaya', '2021-01-21', 28, 9),
(29, 'Niyaga Puspita', 'Jakarta', '2022-11-03', 29, 9),
(31, 'Muhammad Ali', 'Bandung', '2023-01-02', 31, 9);

-- --------------------------------------------------------

--
-- Table structure for table `cabang`
--

CREATE TABLE `cabang` (
  `id_cabang` int(11) NOT NULL,
  `nama_cabang` varchar(250) NOT NULL,
  `nama_owner` varchar(250) NOT NULL,
  `telepon` varchar(50) NOT NULL,
  `alamat` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cabang`
--

INSERT INTO `cabang` (`id_cabang`, `nama_cabang`, `nama_owner`, `telepon`, `alamat`) VALUES
(51, 'Susanti Raya asri', 'Ir. Ega Nashiruddin, S.Kom', '+62-89-734-1540', 'jl. Cigondewah KR 05465'),
(52, 'Marpaung Laksmiwati', 'Zahra Agustina', '+62 (060) 389 9', 'Gg. Dipenogoro No. 031'),
(53, 'Permata Purwanti', 'Uchita Marpaung', '(0670) 383-3026', 'Gang Cihampelas No. 72'),
(54, 'Wacana Jamiri', 'Unjani Mahendra, M.Farm', '+62-0074-780-29', 'Jalan Cikutra Barat No. 756'),
(55, 'Tarihoran', 'Vino Tarihoran', '+62 (65) 183-97', 'Jl. R.E Martadinata No. 98'),
(56, 'Suryatmi Asri Pradana', 'Gasti Pranowo', '+62 (33) 031 53', 'Jl. H.J Maemunah No. 289'),
(57, 'Tunas Hidayat', 'Cahya Handayani', '+62-37-057-1623', 'Jl. Rajawali Barat No. 512'),
(58, 'Sekapur Siri', 'Titi Pudjiastuti', '+62-72-289-1952', 'Kota Administrasi, No. 50322'),
(59, 'Laksita Januar', 'Ir. Lili Permata', '+62 (57) 483 23', 'Jalan Kutisari Selatan No. 62'),
(60, 'Bulan Mas', 'drg. Suci Hastuti, S.E.I', '+62-0573-637-06', 'Gang K.H. Wahid Hasyim No. 885'),
(61, 'Rajasa Lailasari', 'Sarah Nugroho, S.H.', '+62 (0967) 162 ', 'Jalan Merdeka No. 489'),
(62, 'Lestari Mekar', 'Najam Utama, S.Kom', '+62-206-923-737', 'Jalan Kutisari Selatan No. 54'),
(63, 'Bunga Raya', 'Irnanto Sihotang', '+62 (35) 521-59', 'Jl. Raya Ujungberung No. 55'),
(64, 'Jamiri Raya', 'Humaira Anggriawan', '+62 (0369) 600 ', 'Gg. Gegerkalong Hilir No. 5'),
(65, 'Sekapur Sirih', 'Tgk. Heryanto Suryono, M.M.', '+62 (587) 670-3', 'Jl. Veteran No. 6'),
(66, 'Pertiwi Raya', 'Sutan Darmanto Prastuti, S.Pt', '(016) 645-9771', 'Gg. Medokan Ayu No. 591'),
(67, 'Marpaung Mustofa', 'Karya Sinaga, M.Kom.', '(098) 207 0451', 'Tanjungpinang, BE 38592'),
(68, 'Bunga Tamba', 'Hafshah Oktaviani', '+62 (0743) 223-0929', 'Jl. Suniaraja No. 40'),
(69, 'Damanik Kusumo', 'Drs. Saiful Nasyidah, M.Farm', '+62-89-143-4493', 'Seloka, No. 16185'),
(70, 'Wastuti Sirih', 'Zamira Fujiati', '+62 (135) 783 4662', 'Gang Sadang Serang No. 435'),
(87, 'wong jowo', 'nugraha adi', '+62-897-144-9322', 'jln. padasuka no. 10');

-- --------------------------------------------------------

--
-- Table structure for table `ibu`
--

CREATE TABLE `ibu` (
  `id_ibu` int(11) NOT NULL,
  `nama` varchar(250) NOT NULL,
  `tempat_lahir` varchar(250) NOT NULL,
  `tgl_lahir` date NOT NULL,
  `alamat` text NOT NULL,
  `telepon` varchar(15) NOT NULL,
  `nik` varchar(18) NOT NULL,
  `id_admin` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `ibu`
--

INSERT INTO `ibu` (`id_ibu`, `nama`, `tempat_lahir`, `tgl_lahir`, `alamat`, `telepon`, `nik`, `id_admin`) VALUES
(10, 'Rahmi Winarno', 'Bandung', '1977-08-25', 'Gg. Ir. H. Djuanda No. 3', '083097447', '8541264594913154', 9),
(11, 'Halima Setiawan', 'Jakarta', '1990-03-18', 'Jalan Ahmad Yani No. 62', '089623377', '3640033035347383', 9),
(12, 'Viman Nuraini', 'Palembang', '1976-12-10', 'Gang Gegerkalong Hilir No. 96', '082117447', '1165885943831287', 9),
(13, 'Lamar Usada', 'Bandung', '1992-07-29', 'Gg. M.T Haryono No. 751', '086229330', '0888614073977319', 9),
(14, 'Suci Simbolon', 'Bandung', '1982-08-16', 'Pematangsiantar, JA 14064', '088394242', '9064572833323648', 9),
(15, 'Puti Diah Wijayanti', 'Palembang', '1974-11-24', 'Jl. Cikutra Barat No. 28', '081505235', '3902654749765704', 9),
(16, 'Zulfa Sitorus', 'Kediri', '1995-09-15', 'Gg. Rungkut Industri No. 6', '089108099', '9931664351182457', 9),
(17, 'Lalita Habibi', 'Sumedang', '1985-09-03', 'Gang Bangka Raya No. 667', '084952884', '6244527375674458', 9),
(18, 'Agnes Riyanti', 'Tangerang', '1990-05-23', 'Jl. Moch. Ramdan No. 06', '082262729', '6448350532910468', 9),
(19, 'Kamila Yuniar', 'Cimahi', '1989-08-04', 'Jl. Sadang Serang No. 9', '080924426', '8671736851614759', 9),
(20, 'Safina Utami', 'Banten', '1995-08-21', 'Gang W.R. Supratman No. 8', '080045107', '2471275606657679', 9),
(21, 'Yuliana Suryono', 'Cimahi', '1999-08-04', 'Jalan Medokan Ayu No. 3', '087288918', '6174542295791634', 9),
(22, 'Kayla Situmorang', 'Jakarta', '1992-01-16', 'Jalan Gegerkalong Hilir No. 9', '081556129', '2930406001366378', 9),
(23, 'Faizah Marbun', 'Jakarta', '1979-09-06', 'Gang Gegerkalong Hilir No. 802', '080119257', '3888875672480303', 9),
(24, 'Ana Kurniawan', 'Surabaya', '1993-01-03', 'Gg. BKR No. 552', '084829036', '8993690260199793', 9),
(25, 'Jamalia Nainggolan', 'Yogyakarta', '1994-05-27', 'Jalan Rumah Sakit No. 97', '089409874', '4316571720967044', 9),
(26, 'Hafshah Sihombing', 'Lampung', '1981-04-24', 'Jalan W.R. Supratman No. 06', '081924698', '8656228722219601', 9),
(27, 'Anita Saragih', 'Bandung', '1992-11-09', 'Jl. Ciumbuleuit No. 631', '089313806', '0158234911525268', 9),
(28, 'Elvina Kurniawan', 'Surabaya', '1996-06-27', 'Jalan Cihampelas No. 986', '083640872', '8662032373589743', 9),
(29, 'Zaenab Wasita', 'Jakarta', '1984-10-05', 'Gg. Rumah Sakit No. 2', '085664108', '8281064568024407', 9),
(31, 'Rahmi milah fauziah', 'Bandung', '1990-08-15', 'jalan cibadak no. 98', '0984759223944', '4439281138499494', 9);

-- --------------------------------------------------------

--
-- Table structure for table `pemeriksa`
--

CREATE TABLE `pemeriksa` (
  `id_pemeriksa` int(11) NOT NULL,
  `nama` varchar(250) NOT NULL,
  `jabatan` varchar(250) NOT NULL,
  `jk_pemeriksa` varchar(11) NOT NULL,
  `telepon` varchar(15) NOT NULL,
  `alamat` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pemeriksa`
--

INSERT INTO `pemeriksa` (`id_pemeriksa`, `nama`, `jabatan`, `jk_pemeriksa`, `telepon`, `alamat`) VALUES
(7, 'Farhunnisa Fujiati, S.Kep', 'perawat', 'Perempuan', '082336119', 'Jl. Astana Anyar No. 58'),
(8, 'Dr. Tri Nashiruddin', 'dokter', 'Perempuan', '087730808', 'Jl. Bangka Raya No. 66'),
(9, 'Purwa Lazuardi, S.Keb', 'bidan', 'Laki-Laki', '087012022', 'Cilegon, KT 67744'),
(10, 'Dr. Jarwi Mayasari', 'dokter', 'Laki-Laki', '086943553', 'Jalan Peta No. 6'),
(11, 'Dr. Aditya Nashiruddin, M.Pd', 'dokter', 'Laki-Laki', '089989565', 'Jl. Lembong No. 690'),
(12, 'Tami Ardianto, S.Kep', 'perawat', 'Perempuan', '087239354', 'Gang Cempaka No. 263'),
(13, 'Padma Wasita, S.Keb', 'bidan', 'Perempuan', '083530955', 'Jl. S. Parman No. 81'),
(14, 'Candrakanta Prasetya, S.Keb', 'bidan', 'Laki-Laki', '085820538', 'Gg. Gedebage Selatan No. 497'),
(15, 'Umaya Putri, S.Kep', 'perawat', 'Perempuan', '085037219', 'Jalan Tubagus Ismail No. 501'),
(16, 'Dr. Gabriella Simanjuntak', 'dokter', 'Laki-Laki', '084826576', 'Jalan Tebet Barat Dalam No. 650'),
(17, 'Kayun Wasita, S.Kep', 'perawat', 'Perempuan', '087390302', 'Jalan Abdul Muis No. 747'),
(18, 'Dr. Hj. Elisa Permata', 'dokter', 'Perempuan', '080316528', 'Gang Pasteur No. 829'),
(19, 'Hj. Jane Puspasari, S.Kep', 'perawat', 'Perempuan', '081381300', 'Gang KH Amin Jasuta No. 578'),
(20, 'Wawan Waskita, S.Kep', 'perawat', 'Laki-Laki', '083041955', 'Jalan Laswi No. 30'),
(21, 'Dr. Adiarja Nasyidah', 'dokter', 'Laki-Laki', '089947452', 'Gang Moch. Toha No. 60'),
(22, 'Rahmi Lestari, S.Keb', 'bidan', 'Perempuan', '083724385', 'Jalan Astana Anyar No. 321'),
(23, 'Ir. Omar Megantara, S.Keb', 'bidan', 'Laki-Laki', '082440600', 'Gang Laswi No. 5'),
(24, 'Jasmin Winarno, S.Kep', 'perawat', 'Perempuan', '085507062', 'Gang Laswi No. 1'),
(25, 'Gasti Agustina, S.Keb', 'bidan', 'Perempuan', '083878626', 'Gang Cihampelas No. 994'),
(26, 'Nasim Saragih, S.Kep', 'perawat', 'Perempuan', '083729458', 'Jalan Pacuan Kuda No. 02'),
(28, 'Dr. Radjiman Sotowirjo', 'dokter', 'Laki-Laki', '08974321098', 'jln. cigurui no.79');

-- --------------------------------------------------------

--
-- Table structure for table `periksa`
--

CREATE TABLE `periksa` (
  `id_periksa` int(11) NOT NULL,
  `tgl` date NOT NULL,
  `id_anak` int(11) NOT NULL,
  `id_ibu` int(11) NOT NULL,
  `hasil_anak` varchar(250) NOT NULL,
  `hasil_ibu` varchar(250) NOT NULL,
  `keterangan` text NOT NULL,
  `id_admin` int(11) NOT NULL,
  `id_pemeriksa` int(11) NOT NULL,
  `id_cabang` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `periksa`
--

INSERT INTO `periksa` (`id_periksa`, `tgl`, `id_anak`, `id_ibu`, `hasil_anak`, `hasil_ibu`, `keterangan`, `id_admin`, `id_pemeriksa`, `id_cabang`) VALUES
(9, '2023-03-30', 10, 10, 'sehat', 'sehat', '-', 9, 7, 51),
(10, '2023-12-20', 11, 11, 'sehat', 'sehat', '-', 9, 7, 51),
(11, '2023-10-13', 12, 12, '-', 'sakit', 'ibu mengalami gejala flu ringan', 9, 7, 52),
(12, '2023-01-16', 13, 13, 'sakit', '-', 'anak mengalami demam tinggi', 9, 10, 52),
(13, '2023-09-18', 14, 14, 'sehat', '-', '-', 9, 10, 52),
(14, '2023-06-06', 15, 15, 'sehat', 'sehat', '-', 9, 10, 52),
(15, '2023-12-04', 16, 16, '-', 'sakit', 'ibu mengalami batuk ringan', 9, 12, 55),
(16, '2023-02-15', 17, 17, 'sakit', 'sehat', 'anak mengalami gangguan pencernaan', 9, 12, 56),
(17, '2023-10-18', 18, 18, 'sehat', 'sakit', 'ibu mengalami tekanan darah yang tinggi', 9, 13, 56),
(18, '2023-12-31', 19, 19, '-', 'sehat', '-', 9, 15, 56),
(19, '2023-10-23', 20, 20, 'sakit', '-', 'anak mengalami demam', 9, 15, 57),
(20, '2023-01-01', 21, 21, 'sakit', 'sehat', 'anak mengalami batuk ringan', 9, 16, 59),
(21, '2023-07-14', 22, 22, 'sakit', '-', '-', 9, 18, 59),
(22, '2023-06-10', 23, 23, 'sehat', '-', '-', 9, 18, 60),
(23, '2023-01-22', 24, 24, '-', '-', '-', 9, 20, 61),
(24, '2023-11-12', 25, 25, 'sakit', '-', 'anak mengalami gangguan pernapasan ringan', 9, 23, 63),
(25, '2023-12-01', 26, 26, '-', 'sehat', '-', 9, 23, 63),
(26, '2023-09-29', 27, 27, 'sehat', 'sakit', 'anak dan ibu mengalami batuk ringan', 9, 23, 64),
(27, '2023-12-15', 28, 28, 'sakit', 'sehat', '-', 9, 24, 64),
(28, '2023-01-01', 29, 29, 'sehat', 'sehat', '-', 9, 7, 51);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id_admin`);

--
-- Indexes for table `anak`
--
ALTER TABLE `anak`
  ADD PRIMARY KEY (`id_anak`),
  ADD KEY `id_admin` (`id_admin`),
  ADD KEY `id_ibu` (`id_ibu`);

--
-- Indexes for table `cabang`
--
ALTER TABLE `cabang`
  ADD PRIMARY KEY (`id_cabang`);

--
-- Indexes for table `ibu`
--
ALTER TABLE `ibu`
  ADD PRIMARY KEY (`id_ibu`),
  ADD KEY `id_admin` (`id_admin`);

--
-- Indexes for table `pemeriksa`
--
ALTER TABLE `pemeriksa`
  ADD PRIMARY KEY (`id_pemeriksa`);

--
-- Indexes for table `periksa`
--
ALTER TABLE `periksa`
  ADD PRIMARY KEY (`id_periksa`),
  ADD KEY `id_pasien` (`id_anak`),
  ADD KEY `id_cabang` (`id_cabang`),
  ADD KEY `id_pemeriksa` (`id_pemeriksa`),
  ADD KEY `id_ibu` (`id_ibu`),
  ADD KEY `id_admin` (`id_admin`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id_admin` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `anak`
--
ALTER TABLE `anak`
  MODIFY `id_anak` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `cabang`
--
ALTER TABLE `cabang`
  MODIFY `id_cabang` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=88;

--
-- AUTO_INCREMENT for table `ibu`
--
ALTER TABLE `ibu`
  MODIFY `id_ibu` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `pemeriksa`
--
ALTER TABLE `pemeriksa`
  MODIFY `id_pemeriksa` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `periksa`
--
ALTER TABLE `periksa`
  MODIFY `id_periksa` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `anak`
--
ALTER TABLE `anak`
  ADD CONSTRAINT `anak_ibfk_1` FOREIGN KEY (`id_admin`) REFERENCES `admin` (`id_admin`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `anak_ibfk_2` FOREIGN KEY (`id_ibu`) REFERENCES `ibu` (`id_ibu`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `ibu`
--
ALTER TABLE `ibu`
  ADD CONSTRAINT `ibu_ibfk_1` FOREIGN KEY (`id_admin`) REFERENCES `admin` (`id_admin`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `periksa`
--
ALTER TABLE `periksa`
  ADD CONSTRAINT `periksa_ibfk_1` FOREIGN KEY (`id_anak`) REFERENCES `anak` (`id_anak`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `periksa_ibfk_2` FOREIGN KEY (`id_ibu`) REFERENCES `ibu` (`id_ibu`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `periksa_ibfk_3` FOREIGN KEY (`id_cabang`) REFERENCES `cabang` (`id_cabang`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `periksa_ibfk_4` FOREIGN KEY (`id_pemeriksa`) REFERENCES `pemeriksa` (`id_pemeriksa`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `periksa_ibfk_5` FOREIGN KEY (`id_admin`) REFERENCES `admin` (`id_admin`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
