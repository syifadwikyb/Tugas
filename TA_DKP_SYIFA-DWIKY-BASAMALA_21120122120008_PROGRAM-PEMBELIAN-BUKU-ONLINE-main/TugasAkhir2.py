import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
import sys

class Tampilan:
    def __init__(self):
        self.window = tk.Tk()
        self.window.configure(bg="#79E0EE")
        self.window.geometry("500x700")
        self.window.resizable(False, False)
        self.window.title("Tugas Akhir Syifa Dwiky Basamala")
        
        self.frame = ttk.Style()
        self.frame.configure("Custom.TFrame", background="#98EECC")

        self.input_frame = ttk.Frame(self.window, style="Custom.TFrame")
        self.input_frame.pack(padx=10, pady=10, fill="x", expand=True)
        self.input_frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

        judul = ttk.Label(self.input_frame, text="Pemesanan Buku", font=("Times New Roman", 14))
        judul.pack(pady=18)
        judul.configure(background="#98EECC")
        
        # Menampilkan objek
        self.biodata_objek = Biodata(self.input_frame)
        self.pilihan_objek = Pilihan(self.input_frame)
        self.jumlah_objek = Jumlah(self.input_frame)
        self.pembayaran_objek = Pembayaran(self.input_frame)
        self.total_objek = Pentotalan(self.input_frame)
        self.oke_button = ButtonOke(self.input_frame, self.jumlah_objek, self.pilihan_objek, self.total_objek,self.pembayaran_objek,self.biodata_objek)
        self.lagi_button = ButtonLagi(self.input_frame, self.jumlah_objek, self.pilihan_objek, self.total_objek)
        self.sub_button = ButtonEx (self.input_frame, self.biodata_objek)
    


        # Menjalankan loop tkinter
        self.window.mainloop()
        
    def isi_pemesanan(self):
        while self.jumlah_pembelian < 3:  # Perulangan berdasarkan jumlah_pembelian
            # Menunggu sampai pengguna menekan tombol "Beli Lagi" atau "Submit"
            self.window.wait_window(self.lagi_button.top)  # Menunggu jendela "Beli Lagi" ditutup

            if self.lagi_button.clicked:  # Jika tombol "Beli Lagi" ditekan
                self.jumlah_pembelian += 1
                if self.jumlah_pembelian == 3:
                    messagebox.showinfo("Batas Maksimal Pembelian", "Anda telah mencapai batas maksimal pembelian (3 kali).")
                    break  # Keluar dari perulangan jika mencapai batas maksimal

                # Menghapus objek yang digunakan dalam pemesanan sebelumnya
                self.biodata_objek.input_frame.destroy()
                self.pilihan_objek.input_frame.destroy()
                self.jumlah_objek.input_frame.destroy()
                self.pembayaran_objek.input_frame.destroy()
                self.oke_button.ingin.destroy()
                self.lagi_button.okey.destroy()
                self.sub_button.submit.destroy()
                self.total_objek.total_label.destroy()

                self.total_objek = Pentotalan(self.input_frame)  # Membuat objek total harga baru

            else:  # Jika tombol "Submit" ditekan
                break  # Keluar dari perulangan dan selesai

class Biodata:
    def __init__(self, input_frame):
        self.input_frame = input_frame

        nama1 = ttk.Label(self.input_frame, text="Nama", font=("Times New Roman", 14))
        nama1.place(x=13, rely=0.1, y=5)
        nama1.configure(background="#98EECC")

        alamat1 = ttk.Label(self.input_frame, text="Alamat", font=("Times New Roman", 14))
        alamat1.place(x=13, rely=0.1, y=45)
        alamat1.configure(background="#98EECC")

        no = ttk.Label(self.input_frame, text="No.Hp ", font=("Times New Roman", 14))
        no.place(x=13, rely=0.1, y=85)
        no.configure(background="#98EECC")

        self._nama_label = ttk.Entry(self.input_frame, font=("Times New Roman", 12))
        self._nama_label.pack(padx=10, pady=10, fill="x", expand=True)
        self._nama_label.place(relx=0.05, rely=0.1, y=5, relwidth=0.65, relheight=0.05, x=100)

        self._alamat_label = ttk.Entry(self.input_frame, font=("Times New Roman", 12))
        self._alamat_label.pack(padx=10, pady=10, fill="x", expand=True)
        self._alamat_label.place(relx=0.05, rely=0.175, relwidth=0.65, relheight=0.05, x=100)

        def validate_input(text):
            if text.isdigit() or text == "":
                return True
            else:
                return False

        validation = (self.input_frame.register(validate_input), '%P')

        self._no_label = ttk.Entry(self.input_frame, validate="key", validatecommand=validation, font=("Times New Roman", 12))
        self._no_label.pack(padx=10, pady=10, fill="x", expand=True)
        self._no_label.place(relx=0.05, rely=0.25, relwidth=0.65, relheight=0.05, x=100)

    def get_nama_label(self):
        return self._nama_label.get()

    def set_nama_label(self, value):
        self._nama_label.delete(0, tk.END)
        self._nama_label.insert(0, value)

    def get_alamat_label(self):
        return self._alamat_label.get()

    def set_alamat_label(self, value):
        self._alamat_label.delete(0, tk.END)
        self._alamat_label.insert(0, value)

    def get_no_label(self):
        return self._no_label.get()

    def set_no_label(self, value):
        self._no_label.delete(0, tk.END)
        self._no_label.insert(0, value)


class Pilihan:
    def __init__(self, input_frame):
        self.input_frame = input_frame
        self.option_var = tk.StringVar()

        #  Label Nama Buku
        buku_label = ttk.Label(self.input_frame, text="Buku", font=("Times New Roman", 14))
        buku_label.place(x=13, rely=0.1, y=130)
        buku_label.configure(background="#98EECC")

        #  Opsi Buku
        self.option_menu = ttk.OptionMenu(self.input_frame, self.option_var, "Pilih Buku", "Laskar Pelangi", "Negeri 5 Menara", "Pulang", "Bumi Manusia")
        self.option_menu.pack(padx=10, pady=10, fill="x", expand=True )
        self.option_menu.place(relx=0.05, rely=0.1, y=130, relwidth=0.35, relheight=0.05, x=100)
        
        # Keterangan
        self.select_button = ttk.Button(self.input_frame, text="Keterangan", command=self.select_option)
        self.select_button.pack(padx=10, pady=10, fill="x", expand=True)
        self.select_button.place(relx=0.7, rely=0.1, y=130, relwidth=0.2, relheight=0.05)

    def select_option(self):
        selected_option = self.option_var.get()
        if selected_option == "Laskar Pelangi":
            penulis = "Andrea Hirata"
            penerbit = "Bentang Pustaka"
            sinopsis = "Buku yang mengisahkan perjuangan sekelompok anak di sebuah desa kecil di Belitung dalam mengejar impian mereka melalui pendidikan."
            harga = 100000
            messagebox.showinfo("Keterangan", f"{selected_option} \nPenulis \t: {penulis}\nPenerbit \t: {penerbit}\nHarga \t: Rp {harga}\nSinopsis \t: {sinopsis}")
        elif selected_option == "Negeri 5 Menara":
            penulis = "Ahmad Fuadi"
            penerbit = "Gramedia Pustaka Utama"
            sinopsis = "Buku yang menceritakan kisah perjalanan seorang remaja asal Garut bernama Alif yang berjuang untuk meraih pendidikan di pesantren terkenal di Jawa Barat."
            harga = 120000
            messagebox.showinfo("Keterangan", f"{selected_option} \nPenulis \t: {penulis}\nPenerbit \t: {penerbit}\nHarga \t: Rp {harga}\nSinopsis \t: {sinopsis}")
        elif selected_option == "Pulang":
            penulis = "Leila S. Chudori"
            penerbit = "Kepustakaan Populer Gramedia"
            sinopsis = "Buku yang mengisahkan tentang sejarah keluarga dan kehidupan politik Indonesia dari tahun 1965 hingga 1998, melalui sudut pandang seorang jurnalis yang hidup dalam pengasingan."
            harga = 75000
            messagebox.showinfo("Keterangan", f"{selected_option} \nPenulis \t: {penulis}\nPenerbit \t: {penerbit}\nHarga \t: Rp {harga}\nSinopsis \t: {sinopsis}")
        elif selected_option == "Bumi Manusia":
            penulis = "Pramoedya Ananta Toer"
            penerbit = "Lentera Dipantara"
            sinopsis = "Buku yang menggambarkan kehidupan masyarakat Indonesia pada masa penjajahan Belanda."
            harga = 50000
            messagebox.showinfo("Keterangan", f"{selected_option} \nPenulis \t: {penulis}\nPenerbit \t: {penerbit}\nHarga \t: Rp {harga}\nSinopsis \t: {sinopsis}")
        else:
            messagebox.showerror("Error", "Harap pilih buku terlebih dahulu.")

class Jumlah:
    def __init__(self, input_frame):
        self.input_frame = input_frame
        self.jumlah = tk.StringVar()

        namajumlah = ttk.Label(self.input_frame, text="Jumlah", font=("Times New Roman", 14))
        namajumlah.place(x=13, rely=0.38, y=5)
        namajumlah.configure(background="#98EECC")

        def validate_input(text):
            if text.isdigit() and 1 <= int(text) <= 3 or text == "":
                return True
            else:
                return False

        validation = (self.input_frame.register(validate_input), '%P')

        jumlah_entry = ttk.Spinbox(self.input_frame, validate="key", validatecommand=validation, textvariable=self.jumlah, font=("Times New Roman", 12), from_=1, to=3)
        jumlah_entry.pack(padx=10, pady=10, fill="x", expand=True)
        jumlah_entry.place(relx=0.05, rely=0.37, y=5, relwidth=0.65, relheight=0.05, x=100)

    def get_jumlah(self):
        return self.jumlah.get()

class Pembayaran:
    def __init__(self, input_frame):
        self.input_frame = input_frame

        metode_label = ttk.Label(self.input_frame, text="Metode Pembayaran", font=("Times New Roman", 14))
        metode_label.place(x=13, rely=0.1, y=220)
        metode_label.configure(background="#98EECC")

        style = ttk.Style()
        style.configure("Custom.TRadiobutton", background="#98EECC")

        self.metode_var = tk.StringVar()
        self.metode_radio1 = ttk.Radiobutton(self.input_frame, text="Transfer Bank", variable=self.metode_var, value="Transfer Bank",style="Custom.TRadiobutton")
        self.metode_radio1.pack(padx=10, pady=10, fill="x", expand=True)
        self.metode_radio1.place(relx=0.18, rely=0.1, y=218, relwidth=0.52, relheight=0.05, x=100)

        self.metode_radio2 = ttk.Radiobutton(self.input_frame, text="Bayar di Kasir", variable=self.metode_var, value="Bayar di Kasir",style="Custom.TRadiobutton")
        self.metode_radio2.pack(padx=10, pady=10, fill="x", expand=True)
        self.metode_radio2.place(relx=0.18, rely=0.175, y=210, relwidth=0.52, relheight=0.05, x=100)

class Pentotalan:
    def __init__(self, input_frame):
        self.input_frame = input_frame

        self.total_label = ttk.Label(self.input_frame, text="Total Harga: Rp 0", font=("Times New Roman", 14))
        self.total_label.pack(pady=10)
        self.total_label.place(x=150, rely=0.1, y=310)
        self.total_label.configure(background="#98EECC")

class ButtonLagi:
    def __init__(self, input_frame, jumlah_objek, pilihan_objek, total_objek):
        self.input_frame = input_frame
        self.pilihan_objek = pilihan_objek
        self.jumlah_objek = jumlah_objek
        self.total_objek = total_objek
        self.total_harga = 0  # Variabel untuk mengakumulasi total harga

        self.okey = ttk.Button(self.input_frame, text="Beli Lagi", command=self.add_item)
        self.okey.pack(padx=10, pady=10, fill="x", expand=True)
        self.okey.place(relx=0.09, rely=0.25, y=270, relwidth=0.2, relheight=0.07)
    
    def add_item(self):
        self.pilihan_objek.option_var.set("Pilih Buku")
        self.jumlah_objek.jumlah.set("")
        self.total_harga = 0  # Mengatur ulang total harga ke 0
        self.total_objek.total_label.config(text=f"Total Harga: Rp {self.total_harga}")
        self.total_objek.total_label.config(text=f"Total yang harus dibayar adalah Rp {self.total_harga}")

        self.total_objek.total_harga = self.total_harga  # Mengupdate total harga pada objek total

class ButtonOke:
    def __init__(self, input_frame, jumlah_objek, pilihan_objek, total_objek, biodata_objek, pembayaran_objek):
        self.input_frame = input_frame
        self.pilihan_objek = pilihan_objek
        self.jumlah_objek = jumlah_objek
        self.biodata_objek = biodata_objek
        self.pembayaran_objek = pembayaran_objek
        self.total_objek = total_objek
        self.total_harga = 0  # Variabel untuk mengakumulasi total harga
        self.book_label_text = ""  # Variabel untuk menyimpan teks total harga per buku
        self.counter = 0  # Variabel untuk melacak berapa kali tombol "Beli Lagi" ditekan

        self.ingin = ttk.Button(self.input_frame, text="Okey", command=self.calculate_total)
        self.ingin.pack(padx=10, pady=10, fill="x", expand=True)
        self.ingin.place(relx=0.7, rely=0.25, y=270, relwidth=0.2, relheight=0.07)

        self.total_label = ttk.Label(self.input_frame, text="Total Harga: Rp 0", font=("Times New Roman", 12))
        self.total_label.pack(pady=5)
        self.total_label.place(relx=0.12, rely=0.8)
        self.total_label.configure(background="#98EECC")

    def calculate_total(self):
        pilihan_buku = self.pilihan_objek.option_var.get()
        jumlah = self.jumlah_objek.jumlah.get()
        selected_option = self.pilihan_objek.option_var.get()
        book_name = ""

        if not jumlah:
            messagebox.showwarning("Peringatan", "Harap memasukkan jumlah buku.")
            return
        elif pilihan_buku == "Pilih Buku":
            messagebox.showwarning("Error", "Harap pilih buku terlebih dahulu.")
            return

        if self.counter < 3:
            if selected_option == "Laskar Pelangi":
                harga = 100000
                book_name = "Laskar Pelangi"
            elif selected_option == "Negeri 5 Menara":
                harga = 120000
                book_name = "Negeri 5 Menara"
            elif selected_option == "Pulang":
                harga = 75000
                book_name = "Pulang"
            elif selected_option == "Bumi Manusia":
                harga = 50000
                book_name = "Bumi Manusia"

            total_harga = int(jumlah) * harga
            self.total_harga += total_harga  # Mengakumulasi total harga
            self.total_objek.total_harga = self.total_harga  # Mengupdate total harga pada objek total
            self.total_objek.total_label.config(text=f"Total Harga: Rp {total_harga}")
            self.book_label_text += f"{book_name}: Rp {total_harga}\n"  # Menyimpan teks total harga per buku
            self.total_label.config(text=self.book_label_text + f"\nTotal yang harus dibayar adalah Rp {self.total_harga}")

            self.counter += 1
            if self.counter == 3:
                self.pilihan_objek.option_var.set("")  # Mengosongkan pilihan buku
                self.pilihan_objek.configure(state="disabled")
        else:
            messagebox.showinfo("Pemberitahuan", "Anda telah mencapai batas maksimal pembelian.")


class ButtonLagi:
    def __init__(self, input_frame, jumlah_objek, pilihan_objek, total_objek):
        self.input_frame = input_frame
        self.pilihan_objek = pilihan_objek
        self.jumlah_objek = jumlah_objek
        self.total_objek = total_objek
        self.counter = 0  # Variabel penghitung

        self.okey = ttk.Button(self.input_frame, text="Beli Lagi", command=self.add_item)
        self.okey.pack(padx=10, pady=10, fill="x", expand=True)
        self.okey.place(relx=0.09, rely=0.25, y=270, relwidth=0.2, relheight=0.07)
    
    def add_item(self):
        while self.counter < 2:  # Batasan pembelian lagi (2 kali)
            self.pilihan_objek.option_var.set("Pilih Buku")
            self.jumlah_objek.jumlah.set("")
            self.total_objek.total_label.config(text="Total Harga: Rp 0")
            self.counter += 1
            break

        if self.counter >= 2:
            messagebox.showinfo("Batas Maksimum", "Anda telah mencapai batas maksimum pembelian lagi.")

class ButtonEx:
    def __init__(self, input_frame,biodata_objek):
        self.input_frame = input_frame
        self.biodata_objek = biodata_objek
        self.biodata_objek = Biodata(input_frame)
        
        self.submit = ttk.Button(self.input_frame, text="Exit", command=self.show_info)
        self.submit.pack(padx=10, pady=10, fill="x", expand=True)
        self.submit.place(relx=0.4, rely=0.25, y=270, relwidth=0.2, relheight=0.07)
        
    def show_info(self):
        nama = self.biodata_objek.get_nama_label()
        alamat = self.biodata_objek.get_alamat_label()
        no_hp = self.biodata_objek.get_no_label()
        
        if not nama:
            messagebox.showwarning("Peringatan", "Harap isi nama.")
        elif not alamat:
            messagebox.showwarning("Peringatan", "Harap isi alamat.")
            return
        elif not no_hp:
            messagebox.showwarning("Peringatan", "Harap isi nomor hp.")
            return
        else:
            info_text = f"Terimakasih banyak-banyak {nama}"
            messagebox.showinfo("Terimakasih", info_text)
            sys.exit(0)

    
        
        

# Membuat objek Tampilan
tampilan = Tampilan()