pin = '123456'
saldo = 0
print("***************************************")
print('*  Selamat Datang di ATM BANK SAHAJA  *')
print("***************************************")


for i in range(3):
    print()

    inPin = input("Silakan masukkan 6 digit pin anda : ")

    if inPin == pin:
        print()
        print("PIN yang Anda masukkan benar")
        print()

        break
    else :
        print("PIN salah")
        if i == 2 :
            print("==============================================")
            print("Akun Anda kami tangguhkan selama 24 jam")
            print("==============================================")
            quit()



pilihan = 'y'

while (pilihan == 'y'):
    print('1. Informasi saldo')
    print('2. Penarikan uang tunai')
    print('3. Setor tabungan')
    print('4. Keluar')


    menu = input('Silahkan pilih menu yang Anda inginkan: ')
    print("===================================================")


    if menu == '1' :
        print(f"Sisa saldo anda : {saldo}")
    elif menu == '2' :
        if saldo < 50000:
            print("Maaf, saldo anda tidak mencukupi.")
            print("Silahkan isi saldo terlebih dahulu.")
        else:
            print("Jumlah nominal penarikan sebesar 50000, 100000, 250000, 500000, 1000000")
            tunai = int(input("Jumlah penarikan anda : "))
            if (tunai == 50000) or (tunai == 100000) or (tunai == 250000) or (tunai == 500000) or (tunai == 1000000):
                saldo == saldo - tunai
                print()
                print(f"Saldo ditarik : {tunai}")
                print(f"Sisa saldo anda : {saldo}")
            else:
                print('Nominal tidak diketahui')
    elif menu == '3':
        setor = int(input("Silahkan masukkan nominal yang ingin disetor : "))
        saldo = saldo + setor
        print()
        print(f"Sisa saldo anda : {saldo}")

    elif menu == '4':
        print("Kartu anda akan keluar dari mesin ATM")
        print()
        print("Terima kasih telah menggunakan layanan BANK SAHAJA")
        quit()
    
    pilihan == input("Apakah anda ingin melanjutkan program? (y/n) : ")
    print("==============================================================")




