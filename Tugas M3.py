
M = int(input("Masukkan modal awal investasi anda     : Rp."))
r = int(input("Suku bunga tahunan (%)                 : "))
T = int(input("Target investasi yang ingin anda capai : Rp."))

tahun = 0
while M < T :
    bunga = M*(r/100)
    M = M + bunga
    tahun = tahun+1
    print(f"- Tahun ke-{tahun} : Rp.{M}")

print(f"Target investasi anda akan tercapai pada tahun ke-{tahun}!")