/* Nomer Satu - Tampilkan jumlah pelanggan berdasarkan tanggal_aktivasi */ 
SELECT COUNT(id_pelanggan) as JUMLAH_PELANGGAN, tanggal_aktivasi
FROM KARTU
GROUP BY tanggal_aktivasi;

/* Nomer Dua - Tampilkan nomor telepon dan promo layanan. Dimana kuota internet lebih besar 15 */
SELECT k.nomor_telepon, l.promo_layanan
FROM KARTU k
JOIN LAYANAN l ON k.id_layanan = l.id_layanan
WHERE l.kuota_internet > 15;

/* Nomer Tiga - Tampilkan nama pelanggan, nomor_telepon, biaya_layanan yang nama pelanggan dimulai dari A */
SELECT p.nama, k.nomor_telepon, i.biaya_layanan
FROM KARTU k
JOIN PELANGGAN p ON k.id_pelanggan = p.id_pelanggan
JOIN INVOICE i ON k.id_invoice = i.id_invoice
WHERE p.nama LIKE 'A%';

