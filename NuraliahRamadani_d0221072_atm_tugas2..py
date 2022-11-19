#membuat atm
saldo = 5000000

def ulang():
    while True:
        tanya = str(input("apakah masihada transaksi lain (y/t) :"))
        if tanya == "y":
            menu()
        elif tanya == "t" :
            print("terimakasih telah menggunakan layanan kami")
            break
        else :
            print("masukkan jawaban dengan benar !")

def masukkan_pin():
    while True :
        masukkan = int(input("masukkan pin anda :"))
        if masukkan == buat_akun.a:
            break
        else :
            print("pin salah")

def buat_akun():
    while True :
        pin_baru = int(input("buat pin anda :"))
        if len(str(pin_baru)) != 6 :
            print("masukkan pin sebanyak 6 digit")
        else :
            buat_akun.a = pin_baru
            return pin_baru

def setoran():
    masukkan_pin()
    setor = int(input("masukkan jumlah uang yang anda setor :"))
    global saldo
    saldo = saldo + setor
    print("setoran berhasil!, saldo anda sekarang",saldo)
    ulang()

def penarikan():
    masukkan_pin()
    tarik = int(input("masukkan jumlah penarikan :"))
    global saldo
    if tarik > saldo :
        print("maaf, saldo anda tidak mencukupi")
    else :
        saldo = saldo - tarik
        print("penarikan berhasil, sisa saldo anda adalah :",saldo)
        ulang()

def ganti_pin():
    masukkan_pin()
    while True :
        pin_baru = int(input("masukkan pin baru :"))
        if len(str(pin_baru)) != 6 :
            print("masukkan pin sebanyak 6 digit")
        else :
            buat_akun.a = pin_baru
            print("pin berhasil diganti")
            ulang()
def cek():
    masukkan_pin()
    print("saldo anda sekarang adalah",saldo)
    ulang()

def menu():
    while True :
        print(" SELAMAT DATANG ",username,)
        pilihan_menu = int(input('''1. setoran
2. penarikan
3. cek
4. ganti pin
5. keluar
pilih menu diatas : '''))
        if pilihan_menu == 1 :
            setoran()
        elif pilihan_menu == 2 :
            penarikan()
        elif pilihan_menu == 3 :
            cek()
        elif pilihan_menu == 4 :
            ganti_pin()
        elif pilihan_menu == 5 :
            print("terimakasih",username,"telah menggunakan layanan kami")
            break
        else:
            print("masukkan pilihan dengan benar")

print(" SELAMAT DATANG, SILAHKAN BUAT AKUN TERLEBIH DAHULU:)")
username = str(input("masukkan nama anda:"))
buat_akun()
menu()
