import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

class KasirApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Kasir Sederhana")

        self.items = []

        # Membuat menu
        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)

        # Menu File
        self.file_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Input Manual", command=self.input_manual)
        self.file_menu.add_command(label="Impor dari File", command=self.impor_dari_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Keluar", command=root.quit)

        # Frame untuk memasukkan item
        self.frame_input = tk.Frame(root)
        self.frame_input.pack()

        tk.Label(self.frame_input, text="Nama Barang:").grid(row=0, column=0)
        self.entry_nama = tk.Entry(self.frame_input)
        self.entry_nama.grid(row=0, column=1)

        tk.Label(self.frame_input, text="Harga:").grid(row=1, column=0)
        self.entry_harga = tk.Entry(self.frame_input)
        self.entry_harga.grid(row=1, column=1)

        tk.Button(self.frame_input, text="Tambah Item", command=self.tambah_item).grid(row=2, columnspan=2)

        # Frame untuk daftar item
        self.frame_list = tk.Frame(root)
        self.frame_list.pack()

        self.listbox_items = tk.Listbox(self.frame_list, width=50)
        self.listbox_items.pack()

        # Frame untuk total dan tombol cetak
        self.frame_total = tk.Frame(root)
        self.frame_total.pack()

        self.label_total = tk.Label(self.frame_total, text="Total: 0")
        self.label_total.pack()

        tk.Button(self.frame_total, text="Cetak Struk", command=self.cetak_struk).pack()

    def tambah_item(self):
        nama_barang = self.entry_nama.get()
        harga = self.entry_harga.get()

        if not nama_barang or not harga:
            messagebox.showerror("Error", "Nama barang dan harga harus diisi")
            return

        try:
            harga = float(harga)
        except ValueError:
            messagebox.showerror("Error", "Harga harus berupa angka")
            return

        self.items.append((nama_barang, harga))
        self.listbox_items.insert(tk.END, f"{nama_barang} - {harga:.2f}")

        total = sum(item[1] for item in self.items)
        self.label_total.config(text=f"Total: {total:.2f}")

        self.entry_nama.delete(0, tk.END)
        self.entry_harga.delete(0, tk.END)

    def cetak_struk(self):
        if not self.items:
            messagebox.showerror("Error", "Tidak ada item untuk dicetak")
            return

        struk = "\n".join([f"{item[0]} - {item[1]:.2f}" for item in self.items])
        total = sum(item[1] for item in self.items)
        struk += f"\n\nTotal: {total:.2f}"

        with open("struk.txt", "w") as f:
            f.write(struk)

        messagebox.showinfo("Info", "Struk telah dicetak ke struk.txt")

        self.items.clear()
        self.listbox_items.delete(0, tk.END)
        self.label_total.config(text="Total: 0")

    def input_manual(self):
        # Membuat dialog input manual
        dialog = tk.Toplevel()
        dialog.title("Input Manual")

        tk.Label(dialog, text="Nama Barang:").grid(row=0, column=0)
        entry_nama = tk.Entry(dialog)
        entry_nama.grid(row=0, column=1)

        tk.Label(dialog, text="Harga:").grid(row=1, column=0)
        entry_harga = tk.Entry(dialog)
        entry_harga.grid(row=1, column=1)

        tk.Button(dialog, text="Save", command=lambda: self.simpan_input_manual(entry_nama.get(), entry_harga.get(), dialog)).grid(row=2, columnspan=2)

    def simpan_input_manual(self, nama_barang, harga, dialog):
        if not nama_barang or not harga:
            messagebox.showerror("Error", "Nama barang dan harga harus diisi")
            return

        try:
            harga = float(harga)
        except ValueError:
            messagebox.showerror("Error", "Harga harus berupa angka")
            return

        self.items.append((nama_barang, harga))
        self.listbox_items.insert(tk.END, f"{nama_barang} - {harga:.2f}")

        total = sum(item[1] for item in self.items)
        self.label_total.config(text=f"Total: {total:.2f}")

        dialog.destroy()

    def impor_dari_file(self):
        # Fungsi untuk mengimpor item dari file
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "r") as f:
                for line in f:
                    nama, harga = line.strip().split(',')
                    harga = float(harga)
