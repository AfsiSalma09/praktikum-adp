M = int(input("Masukkan modal awal investasi anda    : Rp."))
r = int(input("Suku bunga tahunan (%)                : "))
T = int(input("Target ivestasi yang ingin anda capai : Rp."))
tahun = 0
modal = M
while M < T :
    bunga = M*(r/100)
    M = M+bunga
    tahun = tahun+1
    print(f"Tahun ke-{tahun} : Rp.{M}")

print(f"Target anda tercapai setelah {tahun} tahun")

    
    