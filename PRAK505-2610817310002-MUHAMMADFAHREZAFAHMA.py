def Biodata(tahunLahir, nama, asal):
    tahun_sekarang = 2020
    umur = tahun_sekarang - tahunLahir
    angkatan = tahunLahir + umur

    print("Perkenalkan Nama Saya :", nama)
    print("Umur Saya :", umur)
    print("Saya Adalah Angkatan :", angkatan)
    print("Asal Saya dari :", asal)


def main():
    tahunLahir = int(input())
    A = input()
    B = input()
    Biodata(tahunLahir, A, B)

main()