import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from hamming import hata_denetim_bitleri_hesapla, hata_tespit_ve_düzelt

class HammingSimulator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hamming Kodu Simülatörü")
        self.geometry("500x450")
        self.configure(bg="#2C3E50")

        style = ttk.Style(self)
        style.configure('TButton', font=('Arial', 12), padding=10, relief="flat", background="#BDC3C7", foreground="black", borderwidth=2)
        style.map('TButton', background=[('active', '#A6ACAF')], relief=[('pressed', 'sunken')])

        self.etiket = tk.Label(self, text="Veri Bitlerini Girin (4, 8, 16, 32 bit):", font=("Arial", 12), bg="#2C3E50", fg="white")
        self.etiket.pack(pady=10)

        self.giris = tk.Entry(self, width=50, font=("Arial", 12))
        self.giris.pack(pady=10)

        self.hesapla_buton = ttk.Button(self, text="Hamming Kodu Hesapla", command=self.hamming_kodu_hesapla, style='TButton')
        self.hesapla_buton.pack(pady=10)

        self.memory_etiket = tk.Label(self, text="Memory: ", font=("Arial", 12), bg="#2C3E50", fg="white")
        self.memory_etiket.pack(pady=10)

        self.hata_giris = tk.Entry(self, width=50, font=("Arial", 12))
        self.hata_giris.pack(pady=10)
        self.hata_giris.config(state=tk.DISABLED)

        self.hata_buton = ttk.Button(self, text="Hatalı Kodu Düzelt", command=self.hata_duzelt, style='TButton')
        self.hata_buton.pack(pady=10)
        self.hata_buton.state(["disabled"])

        self.duzeltme_sonuc_etiket = tk.Label(self, text="", font=("Arial", 12), bg="#2C3E50", fg="white")
        self.duzeltme_sonuc_etiket.pack(pady=10)

        self.memory = {}  # Bellek saklama

    def hamming_kodu_hesapla(self):
        veri_bitleri = self.giris.get()
        if len(veri_bitleri) not in [4, 8, 16, 32]:
            messagebox.showerror("Hata", "Lütfen 4, 8, 16 veya 32 bit uzunluğunda veri girin.")
            return
        hamming_kodu = hata_denetim_bitleri_hesapla(veri_bitleri)
        self.memory[veri_bitleri] = hamming_kodu  # Bellekte sakla
        self.memory_etiket.config(text=f"Memory: {self.memory}")
        self.hata_giris.config(state=tk.NORMAL)
        self.hata_giris.delete(0, tk.END)
        self.hata_giris.insert(0, hamming_kodu)
        self.hata_buton.state(["!disabled"])

    def hata_duzelt(self):
        hatali_kod = self.hata_giris.get()
        if not hatali_kod:
            messagebox.showerror("Hata", "Önce hatalı Hamming Kodunu girin.")
            return
        duzeltilmis_kod, tespit_edilen_hata_pozisyonu = hata_tespit_ve_düzelt(hatali_kod)
        if tespit_edilen_hata_pozisyonu:
            self.duzeltme_sonuc_etiket.config(text=f"Düzeltilmiş Kodu: {duzeltilmis_kod}\nHata {tespit_edilen_hata_pozisyonu}. pozisyonda düzeltildi.")
        else:
            self.duzeltme_sonuc_etiket.config(text="Hata tespit edilmedi veya kod zaten doğru.")

if __name__ == "__main__":
    uygulama = HammingSimulator()
    uygulama.mainloop()
