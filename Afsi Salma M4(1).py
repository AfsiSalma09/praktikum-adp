#cetak output X O
baris = int(input("Masukkan banyak baris: "))
kolom = int(input("Masukkan banyak kolom: "))

for i in range(baris):
    for j in range (kolom):
        if (i+j)%2==0 :
            print("X" , end="  ")
        else :
            print("O", end="  ")
    print( )
