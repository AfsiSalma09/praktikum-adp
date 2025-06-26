import time
import cv2
import qrcode
import os

menu = [
    ["kawa original" , 5000],
    ["kawa susu" , 7000],
    ["kawa telur" , 10000],
    ["kawa dingin" , 6000],
    ["kawa susu dingin" , 8000],
    ["mojito" , 10000],
    ["kawa telur tapai" , 12000],
    ["teh es" , 6000],
    ["gorengan" , 1500]
]
menu = {nama:harga for nama,harga in menu}

def buat_qr_menu():
    isi = "https://drive.google.com/file/d/1LTep-QFNH-SrobeipgKZQgqObp94Gc9q/view?usp=drivesdk"
    qr = qrcode.QRCode(version=1, box_size=8, border=4)
    qr.add_data(isi)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("menu_qr.jpg")

def tampilkan_qr_menu():
    img = cv2.imread("menu_qr.jpg")
    cv2.imshow("Scan Menu Disini 📱", img)
    cv2.waitKey(10000) 
    cv2.destroyAllWindows()

def buat_qr_pembayaran():
    isi = "https://drive.google.com/file/d/1NSO6e_R3jfXoI69ZqjlXKgltcXblq289/view?usp=drivesdk"
    qr = qrcode.QRCode(version=1, box_size=8, border=4)
    qr.add_data(isi)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr_pembayaran.jpg")

def tampilkan_qr_pembayaran():
    img = cv2.imread("qr_pembayaran.jpg")
    cv2.imshow("📱 QR Code Pembayaran", img)
    cv2.waitKey(10000)
    cv2.destroyAllWindows()

def animasi_teks(teks): 
    for huruf in teks :
        print(huruf, end='', flush=True)
        time.sleep(0.04)
    print()

def input_pesanan() :
    pesanan = {}
    while True:
        pilihan = input("Masukkan nama menu yang ingin dibeli (ketik '0' untuk selesai): ").strip().lower()
        if pilihan == '0':
            break
        if pilihan not in menu:
            print("Menu tidak tersedia, coba lagi!")
            continue
        try:
            jumlah = int(input(f"Jumlah {pilihan}: "))
            if jumlah <= 0:
                print("Jumlah harus lebih dari 0.")
                continue
            if pilihan in pesanan:
                pesanan[pilihan] += jumlah
            else:
                pesanan[pilihan] = jumlah
        except ValueError:
            print("Input jumlah harus angka!")
    return pesanan

def hitung_total(pesanan):
    total = 0
    for nama, jumlah in pesanan.items():
        total += menu[nama] * jumlah
    return total

def simpan_struk(pesanan,pelanggan,metode, meja):
    f = open("struk belanja.txt", "a", encoding="utf-8")
    f.write("\n=========== STRUK BELANJA ===========")
    f.write(f"\nPelanggan         : {pelanggan}")
    f.write(f"\nNo meja pelanggan : {meja}")
    f.write(f"\nMetode pembayaran : {metode}\n")
    f.write("\nPesanan ")
    for nama, jumlah in pesanan.items():
        harga = menu[nama]
        subtotal = harga * jumlah
        f.write(f"\n{nama:<19} x{jumlah:<3} = Rp {subtotal}")
    total = hitung_total(pesanan)
    f.write("\n=====================================")
    f.write(f"{"\nTotal Bayar" :<24}  : Rp {total}")
    f.write("\nTerimakasih sudah berbelanja di Kawa Daun Mangkuto🙌")
    f.write("\nSelamat menikmati pesanan anda\n")
    f.close()

def cetak_struk(pesanan, pelanggan, metode, meja) :
    animasi_teks("\nMencetak struk belanja...")
    time.sleep(0.5)
    print("=========== STRUK BELANJA ===========")
    print(f"Pelanggan         : {pelanggan}")
    print(f"No meja pelanggan : {meja}")
    print(f"Metode pembayaran : {metode}\n")
    print("Pesanan")
    for nama, jumlah in pesanan.items() :
        harga = menu[nama]
        subtotal = harga * jumlah
        print(f"{nama:<19} x{jumlah:<3} = Rp {subtotal}")
        time.sleep(0.3)
    total = hitung_total(pesanan)
    print("=====================================")
    print(f"{"Total Bayar" :<24} : Rp {total}")
    print("\nTerimakasih sudah berbelanja di Kawa Daun Mangkuto🙌")
    print("Selamat menikmati pesanan anda")
    
def main() :
    os.system("cls")
    animasi_teks("Halo👋, Selamat datang di Kawa Daun Mangkuto")
    pelanggan = input("Masukkan nama pelanggan : ")
    meja = input("No meja pelanggan       : ")
    time.sleep(1)
    animasi_teks("silahkan scan barcode berikut untuk melihat menu😉")
    time.sleep(1)
    buat_qr_menu()
    tampilkan_qr_menu()
    print()
    pesanan = input_pesanan()
    if not pesanan:
        animasi_teks("Tidak ada pesanan. Terima kasih sudah berkunjung🙌\n")
        return
    total = hitung_total(pesanan)
    animasi_teks(f"Total belanja Anda   : Rp {total}")
    print()
    while True :
        metode = input("Bayar via (1) Kasir Langsung, (2) QR Code? Ketik 1 atau 2: ").strip()
        if metode == "1" :
            metode = "Cash"
            cetak_struk(pesanan,pelanggan,metode,meja)
            animasi_teks('\nsilahkan menuju kasir untuk pembayaran!') 
            break
        elif metode == "2":
            metode = "Cashless"
            animasi_teks("siapkan kamera anda!")
            time.sleep(3)
            animasi_teks("Menampilkan QR Code pembayaran...")
            time.sleep(3)
            buat_qr_pembayaran()
            tampilkan_qr_pembayaran()
            time.sleep(8)
            cetak_struk(pesanan,pelanggan,metode,meja)
            break
        else :
            print("Pilihan tidak valid. Silahkan pilih angka 1 atau 2!")
    simpan_struk(pesanan, pelanggan, metode, meja)
main()