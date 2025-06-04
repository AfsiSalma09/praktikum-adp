def hitung_nilai(pengalaman,wawancara,pilihan) :
    poin = 0 
    if 'ketua' in pengalaman.lower() :
        poin += 2
    if pilihan.lower() in pengalaman.lower() :
        poin +=3
    total_nilai = (wawancara + poin)*100
    return total_nilai

# membaca file
Bidang = {
    'Acara' : [],
    'Pubdok' : [],
    'Perlengkapan' : [],
    'Danus' : []
    }
with open('OrPSB22.txt','r') as file :
    for line in file :
        nama,nim,kelas,pengalaman,wawancara,pilihan = line.strip().split(',')
        nilai_akhir = hitung_nilai(pengalaman,wawancara,pilihan)
        data = {
        'nama' : nama,
        'nim' : nim,
        'kelas' : kelas,
        'pengalaman' : pengalaman,
        'wawancara' : float(wawancara),
        'pilihan' : pilihan,
        'nilai' : nilai_akhir
        }
        Bidang[pilihan].append(data)

# mungurutkan data
for bidang in Bidang :
    print(f'===== Koordinator Bidang {bidang} =====')
    daftar = sorted(Bidang[bidang], key=lambda x:x['nilai'], reverse = True)
    for i, name in enumerate(daftar[ :2], 1) :
        print(f'{i}. {name['nama']} ({name['nim']}) dengan nilai : {name['nilai']}')


