#1.
# x = set((input("Masukkan 5 film kesukaan Anda:").split(",")))
# y = set((input("Masukkan 5 film kesukaan teman Anda:").split(",")))

# gabungan = x.intersection(y)
# persen = (len(gabungan) / 5) * 100
# print(f"Kesukaan film kalian yang sama sebesar: {persen}%")

#2.
from tabulate import tabulate

buah = [
    ["Apel", 20, 10000],
    ["Jeruk", 15, 15000],
    ["Anggur", 25, 20000]
]

cart = []

def daftar():
    print("\nDaftar Buah yang Tersedia:")
    print(tabulate([[i] + buah for i, buah in enumerate(buah)], headers=["Index", "Nama", "Stock", "Harga"], showindex=False))

def nambah():
    nama = input("Masukkan nama buah yang ingin ditambahkan: ").capitalize()
    stock = int(input("Masukkan jumlah stock: "))
    harga = int(input("Masukkan harga buah: "))
    buah.append([nama, stock, harga])
    print(f"{nama} telah ditambahkan!\n")

def hapus():
    daftar()
    index = int(input("Masukkan index buah yang ingin dihapus: "))
    if 0 <= index < len(buah):
        hapus = buah.pop(index)
        print(f"{hapus[0]} telah dihapus.\n")
    else:
        print("Index tidak valid!\n")
        hapus()

def beli():
    cart.clear()

    daftar()
    i = int(input("Masukkan index buah yang ingin dibeli: "))
    if 0 <= i < len(buah):
        jumlah = int(input(f"Masukkan jumlah {buah[i][0]} yang ingin dibeli: "))
        if jumlah <= buah[i][1]:
            total = jumlah * buah[i][2]
            cart.append([buah[i][0], jumlah, total])
            print("\nCart:")
            print(tabulate(cart, headers=["Nama", "Jumlah", "Total Harga"]))
            print(f"Total harga: {total}")
            uang = int(input("Masukkan jumlah uang: "))
            s = uang - total
            if uang < total :
                print(f"Transaksi Anda dibatalkan, uangnya kurang sebesar {abs(s)}")
                lain = input("Mau beli yang lain? (ya/tidak): ").lower()
                if lain == "ya":
                    beli()
            elif uang >= total:
                print(f"Uang kembalian Anda {s}")
                buah[i][1] -= jumlah
                lain = input("Mau beli yang lain? (ya/tidak): ").lower()
                if lain == "ya":
                    beli()
        else:
            print(f"Stock tidak mencukupi! {buah[i][0]} tinggal {buah[i][1]}!")
            lain = input("Mau beli yang lain? (ya/tidak): ").lower()
            if lain == "ya":
                    beli()
    else:
        print("Index tidak valid!")
        beli()


def menu():
    print("Selamat Datang di Pasar Buah")
    print("1. Menampilkan Daftar Buah")
    print("2. Menambah Buah")
    print("3. Menghapus Buah")
    print("4. Membeli Buah")
    print("5. Exit Program")
    menu = int(input("Masukkan angka menu yang ingin dijalankan: "))
    
    if menu == 1:
        daftar()
    elif menu == 2:
        nambah()
    elif menu == 3:
        hapus()
    elif menu == 4:
        beli()
    elif menu == 5:
        exit
    else:
        print("coba lagi")
menu()



