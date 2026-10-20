#Buatlah GUI dengan Tkinter yang berisi:
#   –1 label judul Aplikasi prediksi Prodi Pilihan
#   –10 input nilai mata pelajaran
#   –1 button bertuliskan Hasil Prediksi
#   –1 label luaran hasil prediksi
#Atur posisi GUI sebaik mungkin!
#Fungsi Hasil Prediksi menuliskan prodi TeknologiInformasi apapun input yang diberikan!
import tkinter as tk

def hasil_prediksi():
    label_hasil.config(text="Teknologi Informasi")

root = tk.Tk()
root.title("Prediksi Prodi Pilihan")

tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan",
         font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

entries = []
for i in range(10):
    tk.Label(root, text=f"Nilai Mapel {i+1}").grid(row=i+1, column=0, padx=10, pady=2, sticky="e")
    e = tk.Entry(root)
    e.grid(row=i+1, column=1, padx=10, pady=2)
    entries.append(e)

tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi).grid(row=11, column=0, columnspan=2, pady=10)

label_hasil = tk.Label(root, text="", font=("Arial", 12))
label_hasil.grid(row=12, column=0, columnspan=2, pady=10)

root.mainloop()