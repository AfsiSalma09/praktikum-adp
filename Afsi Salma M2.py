print()
nama = str(input("Masukkan nama anda : "))
print()
print(f"Selamat datang {nama}")
print("Berikut kami tampilkan film yang akan tayang :")
print("01 : Captain Amerika ")
print("     Harga = Rp 55.000 ")
print("02 : Keluarga Cemara ")
print("     Harga = Rp 40.000 ")
print("03 : Senandung Kasih ")
print("     Harga = Rp 30.000 ")
print("04 : Cinta Kasih Ibu ")
print("     Harga = Rp 40.000 ")
print("05 : kisah Myesha ")
print("     Harga = Rp 45.000 ")

print()
x = int(input("Masukkan kode film pilihan anda : "))
if x==1 :
    harga = 55000
    judul = str("Captain Amerika")
elif x==2 :
    harga = 40000
    judul = str("Keluarga Cemara")
elif x==3 :
    harga = 30000
    judul = str("Senandung Kasih")
elif x==4 :
    harga = 40000
    judul = str("Cinta Kasih Ibu")
elif x==5 :
    harga = 45000
    judul = str("Kisah Myesha")
else :
    harga = 0
    judul = str("Data tidak tersedia")

y = int(input("jumlah tiket : "))
total_pesanan = harga*y
if total_pesanan<100000 :
    diskon = 0
elif 100000<total_pesanan<=250000 :
    diskon = (15/100) * total_pesanan 
else :
    diskon = (35/100) * total_pesanan
total = total_pesanan - diskon 

print()
if total == 0 :
    print("Kode yang anda masukkan tidak tersedia")
else :
    print("Struk pemesanan")
    print(f"    Nama            : {nama}")
    print(f"    Judul Film      : {judul}")
    print(f"    Jumlah tiket    : {y}")
    print(f"    Harga Satuan    : Rp {harga}")
    print(f"    Potongan Harga  : Rp {diskon}")
    print(f"    Total Harga     : Rp {total}")

print()
if total == 0 :
    print()
else :
    print(f"Semoga anda menikmati film {judul}")