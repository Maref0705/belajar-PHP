#PHP.py
import os, sys, time
os.system('clear')
def main (kata):
        for e in kata:
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.2)
print ("""
\033[1;91m           ____    _   _   ____  
          |  _ \  | | | | |  _ \ 
          | |_) | | |_| | | |_) |
\033[1;37m          |  __/  |  _  | |  __/ 
          |_|     |_| |_| |_|    
                \033[1;33mversi \033[1;92m9.9
""")
print ("\033[1;91m[\033[1;37m=======================================\033[1;91m]")
main("""
        \033[1;37mSelamat datang Gaess \033[1;92m>_

   \033[1;37mSemoga bermanfaat buat kalian \033[1;92m>_<

""")
print ("\033[1;91m[\033[1;37m=======================================\033[1;91m]")
nama = input('\033[1;34m( \033[1;33mSTAR \033[1;34m) \033[1;92m--> \033[1;91mEnter \033[1;92m: ')
time.sleep(3)
print ('\n')
main('  \033[1;92mLoading\033[1;37m....')
time.sleep(4)
os.system('clear')
print ("""
       \033[1;91m(\033[1;33mAuthor\033[1;91m) \033[1;92m: \033[1;37mM_aref

       \033[1;34m(\033[1;37mYoutub\033[1;34m) \033[1;92m: \033[1;33mThe-X-Cyber
""")
main("""
\033[1;37mpada PHP sering diawali dengan tanda <? atau <?php dan diakhiri dengan tanda ?>. Dan untuk menambahkan komentar diawali dengan tanda /* dan diakhiri dengan *? atau //, berikut saya tuliskan Syntax PHP yang mungkin dapat menjadi pedoman. Silahkan…

1. Struktur Dasar
Berikut struktur dasar kode HTML :
<?php
?>
Dapat juga ditulis :
<?
?>
Kode PHP dapat digabung dengan HTML seperti pada contoh berikut :
<html>
<body>
<?php
Echo Hello World;
?>
</body>
</html>
2. /* */
Mendefinisikan komentar. Teks yang berada dalam kode ini tidak akan diakses oleh webserver.
Contoh:
<?php
/*Ini adalah kolom komentar*/
Echo Hello World;
?>
3. Variabel
Penulisan variabel dalam PHP diawali dengan symbol $.
Syntax dasar :
$nama_variabel = value;
Contoh :
<?php
$teks=Hello World;
$bil=10;
?>
4. if else
=======================================
Merupakan statemen kondisi yang digunakan untuk menentukan aksi yang akan dilakukan pada kondisi tertentu.
PHP memiliki 4 macam statemen kondisi, yaitu :
if digunakan untuk menjalankan kode-kode berikutnya hanya jika kondisi bernilai benar (true).
Syntax dasar:
if (condition) kode yang akan dijalankan ketika kondisi bernilai benar;
Contoh:
<?php
$d=date (D);
if ($d= =Fri)
echo Selamat weekend;
?>
Ifelse digunakan untuk menjalankan kkode-kode berikutnya jika kondisi bernilai benar (true) dan akan menjalankan kode-kode yang lain jika kondisi bernilai salah (false).
Sytax dasar:
if (condition) kode yang akan dijalankan ketika kondisi bernilai benar;
else
kode yang akan dijalankan ketika kondisi bernilai salah;
contoh:
=======================================
<?php
$d=date (D);
if ($d= =Fri)
echo Selamat weekend;
else
echo Hari yang menyenangkan;
?>
ifelseifelse digunakan untuk memilih salah satu dari beberapa blok kode yang akan dijalankan.
if (condition) kode yang akan dijalankan ketika kondisi bernilai benar;
elseif (condition) kode yang akan dijalankan ketika kondisi berikutnya bernilai benar;
else
kode yang akan dijalankan ketika kondisi bernilai salah;
contoh:
<?php
$d=date (D);
if ($d= =Fri)
echo Selamat weekend;
elseif ($d= `=Sun)
echo Senin yang penuh semangat;
else
echo Hari yang menyenangkan;
?>
Switch digunakan untuk memilih salah satu dari banyak blok kode yang akan dijalankan.
=======================================
5. switch
Merupakan statemen kondisi yang digunakan untuk memilih salah satu dari banyak blok kode yang akan digunakan.
Syntax dasar:
switch (n)
{
case label1 :
kode yang akan dijalankan jika n=label1;
break;
case label2 :
kode yang akan dijalankan jika n=label2;
break;
default:
=======================================
kode yang akan dijalankan jika n tidak sama dengan label1 dan label2;
}
Contoh :
<?php
switch ($x)
{
case 1:
echo Bilangan = 1;
break;
case 2:
echo Bilangan = 2;
break;
case 3:
echo Bilangan = 3;
break;
default:
echo Bilangan selain 1, 2, 3;
}
?>
6. while loop
Merupakan statemen perulangan yang akan menjalankan suatu blok kode selama kondisi terpenuhi (true).
Syntax dasar :
while (condition)
{
kode yang akan dijalankan;
}
Contoh :
<?php
$i=1;
while($i<=5)
{
echo Nomor ke . $i .<br />;
$i++;
}
?>
Hasil :
Nomor ke 1
Nomor ke 2
Nomor ke 3
Nomor ke 4
Nomor ke 5
7. do while
=======================================
Merupakan statemen perulangan yang akan selalu menjalankan sebuah blok kode dan akan berhenti sampai dengan kondisi tidak terpenuhi.
Syntax dasar :
do
{
Kode yang akan dijalankan;
}
while (condition);
contoh :
<?php
$i=1;
do
{
$i++;
echo Nomor ke . $i .<br />;
}
while($i<=5)
?>
Hasil :
Nomor ke 2
Nomor ke 3
Nomor ke 4
Nomor ke 5
Nomor ke 6
8. for loop
=======================================
Merupakan statemen perulangan yang digunakan jika Anda sudah mengetahui sebelumnya berapa kali blok kode harus dijalankan.
Syntax dasar :
For (init; condition; increment;)
{
Kode yang akan dijalankan;
}
Contoh:
<?php
for ($i=1; $i<=5; $i++)
{
echo Nomor ke . $i .<br />;
}
?>
Hasil :
Nomor ke 2
Nomor ke 3
Nomor ke 4
Nomor ke 5
Nomor ke 6
9. foreach
=======================================
Merupakan statemen perulangan yang digunakan pada tipe array.
Syntax dasar :
Foreach ($array as $value)
{
kode yang akan dijalankan;
}
Contoh :
<?php
$x=array(satu,dua,tiga);
foreach ($x as $value)
{
echo $value . <br />;
}
?>
Hasil :
satu
dua
tiga
10. $_GET
=======================================
Digunakan untuk mengumpulkan dan mengambil nilai yang dikirim melalui form dengan parameter method=get. Informasi yang dikirim menggunakan metode ini akan terlihat melalui address bar browser dan jumlahnya terbatas (maksimum 100 karakter).
Contoh :
Pada form pengirim:
<form action=,welcome.php method=get>
Name: <input type=text name=fnama/>
Age: <input type=text name=umur />
<input type=submit />
</form>
Pada file penerima:
Selamat datang <?php echo $_GET[fnama]; ?>.<br />
Usia Anda <?php echo $_GET[umur]; ?> tahun
11. Checkdate( )
Digunakan untuk validasi penanggalan. Fungsi ini akan menghasilkan nilai true jika tanggal valid dan false jika tanggal tidak valid.
Syntax dasar :
checkdate (month,day ,year)
contoh:
=======================================
<?php
var_dump (checkdate(12,31,2000));
var_dump (checkdate(2,29,2003));
var_dump (checkdate(2,29,2004));
?>
Hasil
bool (true) bool (false) bool(true)
12. date_default_timezone_get( )
Digunakan untuk mendapatkan informasi daerah waktu (timezone) default yang digunakan oleh seluruh fungsi pada sebuah dokumen PHP.
Syntax dasar :
date_default_timezone_get (void)
contoh:
=======================================
<?php
echo date_default_timezone_get( ) );
?>
Hasil :
Asia/Krasnoyarsk
13. date_default_timezone_set( )
digunakan untuk menerapkan (set) daerah waktu (timezone) default yang akan digunakan oleh seluruh fungsi pada sebuah dokumen PHP. Daftar timezone yang mendukung PHP dapat dilihat pada web http://www.php.net/manual/en/timezones.p….
Syntax dasar :
date_default_timezone_set (timezone)
Contoh :
<?php
echo (date_default_timezone_set(Asia/Krasnoyarsk) );
?>
14. date( )
Digunakan untuk memformat tanggal dan waktu lokal (local time). Referensi parameter dapat dilihat dapat dilihat pada web http://php.net/manual/en/function.date.p….
Syntax dasar :
date (format,timestamp)
contoh :
=======================================
<?php
echo (Tanggal saat ini<br>);
echo (date(1 d F Y h:i:s:A) . <br />);
?>
Hasil :
Tanggal saat ini
Sunday 27 June 2010 01:33:57 AM
15. getdate( )
Digunakan untuk mendapatkan informasi tanggal dan waktu dalam bentuk array. Informasi yang dihasilkan memiliki format :
[seconds] detik
[minutes] menit
[hours] jam
[mday] hari dalam sebulan
[wday] hari dalam seminggu
[year] tahun
[yday] hari dalam setahun
[weekday] nama hari
[month] nama bulan
Syntax dasar :
getdate (timestamp)
Contoh :
=======================================
<?php
$my_t=getdate(date(U));
print($my_t[weekday], $my_t[month],
$my_t[mday], $my_t[year]);
?>
Hasil :
Sunday, June 27, 2010
16. idate( )
Digunakan untuk memformat tanggal dan waktu lokal (local time) ke dalam bentuk bilangan bulat (integer).
Syntax dasar :
idate (format,timestamp)
contoh :
=======================================
<?php
echo(idate(Y));
?>
Hasil :
2010
17. strtotime( )
Digunakan untuk mengubah tipe string menjadi format penanggalan/waktu.
Syntax dasar :
strtotime (time,now)
contoh :
<?php
echo date (F d Y, strtotime(5-1-2010));
?>
Hasil :
January 05 2010
18. time( )
Digunakan untuk mendapatkan informasi saat ini.
Syntax dasar :
time(void)
contoh :
=======================================
<?php
$t=time();
echo (date(D F d Y,$t));
?>
Hasil :
Sun June 27 2010
19. cal_days_in_month( )
Digunakan untuk mendapatkan informasi jumlah hari dalam bulan dan tahun tertentu berdasarkan kalender yang digunakan.
Syntax dasar :
cal_days_in_month(calendar,month,year)
contoh :
=======================================
""")
time.sleep(4)
os.system("python3 PHP.py")
