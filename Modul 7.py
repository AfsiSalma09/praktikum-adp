# Menghitung GLBB

def output_tabel(data) :
    print('+'+('-'*6)+'+'+('-'*22)+'+'+('-'*17)+'+'+('-'*10)+'+'+('-'*22)+'+'+('-'*12)+'+')
    print(f'|{'No' :<5} | {'Kecepatan Awal' :<20} | {'Percepatan' :<15} | {'Waktu' :<8} | {'Kecepatan Akhir' :<20} | {'Jarak' :<10} |')
    print('+'+('-'*6)+'+'+('-'*22)+'+'+('-'*17)+'+'+('-'*10)+'+'+('-'*22)+'+'+('-'*12)+'+')
    for i, (v0, a, t, v, s) in enumerate (data,1) :
        print(f'| {i :<4} | {v0 :<20} | {a :<15} | {t :<8} | {v :<20.2f} | {s :<10.2f} |')
        print('+'+('-'*6)+'+'+('-'*22)+'+'+('-'*17)+'+'+('-'*10)+'+'+('-'*22)+'+'+('-'*12)+'+')
        
def main() :
    n = int(input('Masukkan jumlah data : '))
    hasil = []
    for i in range(n) :
        print(f'Data ke-{i+1}')
        v0 = float(input('Masukkan kecepatan awal(m/s) : '))
        a  = float(input('Masukkan percepatan(m/s**2)  : '))
        t  = float(input('Masukkan waktu (s)           : '))
        v = v0 + a*t
        s = v0*t + 0.5*a*t**2
        hasil.append([v0, a, t, v, s])

    print('Hasil Perhitungan : ')
    output_tabel(hasil)

main()

