data = {'A' : 4.00,'A-' : 3.75,'B+' : 3.50, 'B' : 3.00, 'B-' : 2.75, 'C+' : 2.50, 'C' : 2.00, 'D' : 1.00, 'E' : 0.00}

jml_mhs = int(input('Masukkan jumlah mahasiswa : '))
jml_mk = int(input('Masukkan jumlah mata kuliah : '))
data_mahasiswa = []
mata_kuliah = []
for i in range (jml_mk) :
    mata_kuliah.append(input(f'Mata Kuliah ke-{i+1} : '))

for i in range(jml_mhs) :
    print()
    nama = input(f'Masukkan nama mahasiswa {i+1}: ')
    nilai = []
    for j in range(jml_mk) :
        while True :
            index = str(input(f'Masukkan indeks nilai {mata_kuliah[j]} : ')).strip().upper()
            
            if index in data :
                nilai.append(data[index])
                break
            else :
                print('Index nilai tidak valid, Masukkan ulang.')
    IP = sum(nilai)/jml_mk
    IPK = f'{IP:.2f}'
    data_mahasiswa.append([nama, index, IPK])
    data_terurut = sorted(data_mahasiswa,key=lambda x:x[2], reverse=True)
    

# output tabel
print()
print('TABEL NILAI MAHASISWA : ')
header = []
a = 'Nama'
b = 'Index Nilai'
c = 'IP'
header.append([a,b,c,])
for row in header :
    print('+'+('-'*25)+'+'+('-'*13)+'+'+('-'*10)+'+')
    print('| {:<23} | {:<11} | {:<8} |'.format(*row))
    print('+'+('-'*25)+'+'+('-'*13)+'+'+('-'*10)+'+')
    for row in data_terurut :
        print('| {:<23} | {:<11} | {:<8} |'.format(*row))
        print('+'+('-'*25)+'+'+('-'*13)+'+'+('-'*10)+'+')