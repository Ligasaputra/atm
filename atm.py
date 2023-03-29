import getpass
class ATM :
    def transfer_saldo(): #Method/Function Tranfer Saldo ATM
            print("\n=============================\n")
            print("Transfer Saldo ATM")
            print("[1] Transfer Antar Bank")
            print("[2] Transfer Sesama Bank")
            print("[3] Kembali")
            pilihan2 = int(input("Masukkan pilihan anda[1/2/3]\t: "))
            if(pilihan2 == 1):
                ATM.transfer_antar_bank()
                        
            elif(pilihan2 == 2):
                ATM.transfer_sesama_bank()
                
            elif(pilihan2 == 3):
                ATM.menu_atm()
            else:
                print("Pilihan tidak valid.. anda kembali ke menu utama")
                ATM.menu_atm()
                
    def transfer_antar_bank():
            print("\n=============================\n")
            print("Transfer Saldo Antar Bank")
            print("[1] Rp.500.000,00")
            print("[2] Rp.100.000,00")
            print("[3] Rp.50.000,00")
            print("[4] Kembali")
            pilihan3 = int(input("Masukkan saldo yang ingin di transfer[1/2/3/4]\t: "))
            if(pilihan3 == 1):
                print("\n=============================\n")
                print("Berhasil Mentransfer Rp.500.000,00 ke Bank Lain!")
                print("\n=============================\n")
                ATM.menu_atm()
            elif(pilihan3 == 2):
                print("\n=============================\n")
                print("Berhasil Mentransfer Rp.100.000,00 ke Bank Lain!")
                print("\n=============================\n")
                ATM.menu_atm()
            elif(pilihan3 == 3):
                print("\n=============================\n")
                print("Berhasil Mentransfer Rp.50.000,00 ke Bank Lain!")
                print("\n=============================\n")
                ATM.menu_atm()
            elif(pilihan3 == 4):
                ATM.transfer_saldo()
            else:
                print("Pilihan tidak valid.. anda kembali ke menu utama")
                ATM.menu_atm()
    
    def transfer_sesama_bank():
            print("\n=============================\n")
            print("Transfer Saldo Sesama Bank")
            print("[1] Rp.500.000,00")
            print("[2] Rp.100.000,00")
            print("[3] Rp.50.000,00")
            print("[4] Kembali")
            pilihan4 = int(input("Masukkan saldo yang ingin di transfer[1/2/3/4]\t: "))
            if(pilihan4 == 1):
                print("\n=============================\n")
                print("Berhasil Mentransfer Rp.500.000,00 ke Sesama Bank!")
                print("\n=============================\n")
                ATM.menu_atm()
            elif(pilihan4 == 2):
                print("\n=============================\n")
                print("Berhasil Mentransfer Rp.100.000,00 ke Sesama Bank!")
                print("\n=============================\n")
                ATM.menu_atm()
            elif(pilihan4 == 3):
                print("\n=============================\n")
                print("Berhasil Mentransfer Rp.50.000,00 ke Sesama Bank!")
                print("\n=============================\n")
                ATM.menu_atm()
            elif(pilihan4 == 4):
                ATM.transfer_saldo()
            else:
                print("Pilihan tidak valid.. anda kembali ke menu utama")
                ATM.menu_atm()
                        
    
    def tarik_saldo(): #Method/Function Menarik Saldo ATM
            print("\n=============================\n")
            print("Menarik Saldo ATM")
            print("[1] Rp.500.000,00")
            print("[2] Rp.100.000,00")
            print("[3] Rp.50.000,00")
            print("[4] Kembali")
            pilihan5 = int(input("Masukkan pilihan anda[1/2/3/4]\t: "))
            if(pilihan5 == 1):
                print("\n=============================\n")
                print("Berhasil Menarik Saldo Rp.500.000,00!")
                print("\n=============================\n")
                ATM.menu_atm()
            elif(pilihan5 == 2):
                print("\n=============================\n")
                print("Berhasil Menarik Saldo Rp.100.000,00!")
                print("\n=============================\n")
                ATM.menu_atm()
            elif(pilihan5 == 3):
                print("\n=============================\n")
                print("Berhasil Menarik Saldo Rp.50.000,00!")
                print("\n=============================\n")
                ATM.menu_atm()
            elif(pilihan5 == 4):
                ATM.menu_atm()
            else:
                print("Pilihan tidak valid.. anda kembali ke menu utama")
                ATM.menu_atm()
        
    def menu_atm():
        print("\n=============================\n")
        print("Selamat datang di ATM")
        print("[1] Transfer Saldo")
        print("[2] Tarik Saldo")
        print("[3] Selesai")

        pilihan = int(input("Masukkan pilihan anda[1/2/3]\t:"))

        if(pilihan == 1):
            ATM.transfer_saldo()
        elif(pilihan == 2):
            ATM.tarik_saldo()
        elif(pilihan == 3):
            exit()
        else:
            print("Pilihan tidak valid.. anda keluar dari ATM")
            ATM.menu_atm()
            
def menu_awal():
    pin = "12345"
    print("\n=============================\n")
    for i in range(3) :
        sandi = getpass.getpass("Masukkan PIN\t: ")
        if (sandi == pin):
            ATM.menu_atm()
        else:
            print("PIN anda salah!")
            if i == 2:
                print("Anda telah melakukan 3x percobaan")
                print("Kartu ATM anda terblokir selama 24 jam")
                print("Keluar dari system...")
                exit()    
menu_awal()