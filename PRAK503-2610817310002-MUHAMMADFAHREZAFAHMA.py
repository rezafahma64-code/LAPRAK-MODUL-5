def maximum(a, b):
    maks = a
    if b > maks:
        maks = b
    return maks

def minimum(a, b):
    kecil = a
    if b < kecil:  
        kecil = b
    return kecil

def main():
    n = int(input())

    nilai_list = list(map(int, input().split()))
    
    # Inisialisasi awal max dan minim dengan elemen pertama
    maks = nilai_list[0]
    minim = nilai_list[0]
    
    batas = 0
    while batas < n:
        nilai = nilai_list[batas]
        maks = maximum(maks, nilai)
        minim = minimum(minim, nilai)
        batas += 1
        
    # Menampilkan hasil akhir sesuai format soal (Terkecil dan Terbesar)
    print(f"{maks} {minim}")

if __name__ == "__main__":
    main()