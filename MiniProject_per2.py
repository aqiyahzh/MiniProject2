class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

        if self.tail is None:
            self.tail = new_node

    def add_last(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def add_after(self, prev_node, data):
        if not prev_node:
            print("Node sebelumnya tidak kami temukan")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

        if prev_node == self.tail:
            self.tail = new_node

    def delete_first(self):
        if self.head is None:
            print("Linked list masih kosong/tidak ada")
            return

        self.head = self.head.next
        if self.head is None:
            self.tail = None

    def delete_last(self):
        if self.head is None:
            print("Linked list masih kosong/tidak ada")
            return

        prev_node = self.head
        while prev_node.next != self.tail:
            prev_node = prev_node.next

        prev_node.next = None
        self.tail = prev_node

        if self.tail is None:
            self.head = None

    def delete_after(self, prev_node):
        if not prev_node:
            print("Node sebelumnya tidak kami temukan")
            return

        if prev_node.next is None:
            print("Node setelah node sebelumnya tidak kami temukan")
            return

        next_node = prev_node.next
        prev_node.next = next_node.next

        if next_node == self.tail:
            self.tail = prev_node

    def print_list(self):
        if self.head is None:
            print("Linked list masih kosong nih :(")
            return

        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next

        print()

class TokoATK:
    def __init__(self):
        self.barang = LinkedList()

    def tambah(self, produk):
        self.barang.add_last(produk)
        print(f"Produk '{produk['Nama Produk']}' sudah ditambahkan nihh")

    def tampil(self):
        if self.barang.head is None:
            print("Belum ada produk yang ditambahkan.")
        else:
            print("Daftar produk yang tersedia:")
            idx = 1
            temp = self.barang.head
            while temp is not None:
                print(f"{idx}. {temp.data['Nama Produk']} | Harga: {temp.data['Harga']} | Stok: {temp.data['Stok']} | Kategori: {temp.data['Kategori']} | ID: {temp.data['ID']}")
                idx += 1
                temp = temp.next

    def perbaharui(self, index, updated):
        idx = 1
        temp = self.barang.head
        while temp is not None:
            if idx == index:
                temp.data = updated
                print(f"Produk '{updated['Nama Produk']}' sudah diperbaharui.")
                return
            idx += 1
            temp = temp.next

        print("Index produk yang anda masukkan salah.")

    def hapus(self, index):
        idx = 1
        prev = None
        temp = self.barang.head
        while temp is not None:
            if idx == index:
                if prev is None:
                    self.barang.delete_first()
                else:             
                    print("Index produk yang anda masukkan salah.")

def menu():
    print('''
        Program Pendataan Barang Toko Alat Tulis 
        by: Aqiyah Zulqiyah (2309116075)
        ''')
    print('[1] Tampil Data')
    print('[2] Tambah Data')
    print('[3] Edit Data')
    print('[4] Hapus Data')
    print('[5] Keluar')
    print('')

toko = TokoATK()

while True:
    menu()
    kode = input('Masukkan Pilihan Anda: ')

    if kode == '1':
        toko.tampil()

    elif kode == '2':
        nama_barang = input("Masukkan nama produk: ")
        harga_barang = float(input("Masukkan harga produk: Rp. "))
        stok_barang = int(input("Masukkan stok produk: "))
        kategori_barang = input("Masukkan kategori produk: ")
        id_barang = input("Masukkan ID produk: ")
        
        barang_baru = {'Nama Produk': nama_barang, 'Harga': harga_barang, 'Stok': stok_barang, 'Kategori': kategori_barang, 'ID': id_barang}
        toko.tambah(barang_baru)

    elif kode == '3':
        toko.tampil()
        index = int(input("Masukkan index produk yang ingin diedit: "))
        nama_baru = input("Masukkan nama produk yang baru: ")
        harga_baru = float(input("Masukkan harga produk yang baru: Rp. "))
        stok_baru = int(input("Masukkan stok produk yang terbaru: "))
        edit_kategori = input("Masukkan kategori produk yang baru: ")
        id_baru = input("Masukkan ID Produk yang baru: ")
        barang_baru = {'Nama Produk': nama_baru, 'Harga': harga_baru, 'Stok': stok_baru, 'Kategori': edit_kategori, 'ID': id_baru}
        toko.perbaharui(index, barang_baru)

    elif kode == '4':
        toko.tampil()
        index = int(input("Masukkan index produk yang ingin dihapus: "))
        toko.hapus(index)

    elif kode == '5':
        print("Terima kasih! Anda telah keluar dari program.")
        break

    else:
        print('Kode yang anda masukkan tidak jelas. Tolong masukkan angka 1-5 saja jangan aneh-aneh :)')
