import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

try:
    df = pd.read_csv('StudentsPerformance.csv')
    print("Dataset 'StudentsPerformance.csv' berhasil dimuat.\n")
except FileNotFoundError:
    print("Error: File 'StudentsPerformance.csv' tidak ditemukan.")
    print("Pastikan file sudah diunggah dengan benar.")
    exit()

kolom_numerik = 'math score'

print(f"--- b. Statistik Awal untuk Kolom '{kolom_numerik}' ---")
mean_awal = df[kolom_numerik].mean()
median_awal = df[kolom_numerik].median()
modus_awal = df[kolom_numerik].mode()[0]

print(f"Mean (Rata-rata): {mean_awal:.2f}")
print(f"Median (Nilai Tengah): {median_awal}")
print(f"Modus (Nilai Paling Sering Muncul): {modus_awal}\n")

print("--- c. Statistik Setelah Menghapus 5% Data Tertinggi ---")

ambang_batas = df[kolom_numerik].quantile(0.95)
print(f"Ambang batas untuk 5% data tertinggi adalah nilai <= {ambang_batas}")

df_filtered = df[df[kolom_numerik] < ambang_batas]

mean_baru = df_filtered[kolom_numerik].mean()
median_baru = df_filtered[kolom_numerik].median()
modus_baru = df_filtered[kolom_numerik].mode()[0]

print(f"\nMean (Baru): {mean_baru:.2f}")
print(f"Median (Baru): {median_baru}")
print(f"Modus (Baru): {modus_baru}\n")

print("--- d. Analisis Perubahan Statistik ---")
print(f"Perubahan Mean: {mean_awal - mean_baru:.2f} (Sangat terpengaruh)")
print(f"Perubahan Median: {median_awal - median_baru:.2f} (Sedikit terpengaruh)")
print(f"Perubahan Modus: {modus_awal - modus_baru:.2f} (Tidak selalu terpengaruh)\n")

plt.figure(figsize=(12, 7))
plt.hist(df[kolom_numerik], bins=20, color='royalblue', alpha=0.7, edgecolor='black')
plt.axvline(mean_awal, color='red', linestyle='dashed', linewidth=2, label=f'Mean Awal: {mean_awal:.2f}')
plt.axvline(median_awal, color='green', linestyle='dashed', linewidth=2, label=f'Median Awal: {median_awal}')
plt.title('Distribusi Nilai Ujian Matematika (Data Asli)', fontsize=16)
plt.xlabel('Nilai Matematika', fontsize=12)
plt.ylabel('Frekuensi (Jumlah Siswa)', fontsize=12)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.savefig('histogram_nilai_matematika.png')
print("--- e. Visualisasi ---")
print("Histogram berhasil dibuat dan disimpan sebagai 'histogram_nilai_matematika.png'.")