from collections import deque
def simulasi_antrian():
    queue = deque()
    while True:
        print("\n1. Tambah pelanggan ke antrian")
        print("2. Layani pelanggan")
        print("3. Tampilkan antrian")
        print("4. keluar")
        pilihan = input("pilih opsi:")

        if pilihan == "1":
            nama = input("masukkan nama pelanggan:")
            queue.append(nama)
            print(f"Pelanggan {nama} ditambahkan antrian.")
        elif pilihan == "2":
            if queue:
                dilayani = queue.popleft()
                print(f"pelanggan {dilayani} sedang dilayani.")
            else:
                print("antrian kosong!")
        elif pilihan == "3":
            print("antrian saat ini", list(queue))
        elif pilihan == "4":
            print("keluar dari program.")
            break
        else:
            print("Opsi tidak valid!")

#menjalankan simulasi
simulasi_antrian()
