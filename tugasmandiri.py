import pandas as pd

# a. Baca dataset menggunakan Pandas
try:
    df = pd.read_csv('Churn_Modelling.csv')
    print("Dataset berhasil dibaca.")
except FileNotFoundError:
    print("File 'Churn_Modelling.csv' tidak ditemukan. Pastikan file berada di direktori yang sama.")
    exit()

# Menampilkan 5 baris pertama untuk memastikan data terbaca dengan benar
print("\n5 baris pertama dari dataset:")
print(df.head())

# b. Ubah salah satu kolom tanggal ke format datetime
# Catatan: Setelah memeriksa dataset, tidak ada kolom yang berisi tanggal.
# Jika ada kolom tanggal, Anda bisa menggunakan kode di bawah ini.
# Misalnya, jika ada kolom bernama 'Date', kodenya adalah:
# df['Date'] = pd.to_datetime(df['Date'])
print("\nTidak ada kolom tanggal dalam dataset ini untuk diubah ke format datetime.")

# c. Hitung nilai rata-rata, median, modus untuk salah satu kolom numerik.
# Kita akan menggunakan kolom 'CreditScore' sebagai contoh.
credit_score_mean = df['CreditScore'].mean()
credit_score_median = df['CreditScore'].median()
credit_score_mode = df['CreditScore'].mode()[0] # mode() bisa mengembalikan lebih dari satu nilai

print("\nStatistik untuk kolom 'CreditScore':")
print(f"Rata-rata: {credit_score_mean}")
print(f"Median: {credit_score_median}")
print(f"Modus: {credit_score_mode}")

# d. Kelompokkan data berdasarkan kolom kategorikal, lalu hitung total salah satu kolom numerik.
# Kita akan mengelompokkan berdasarkan 'Geography' dan menghitung total 'Balance'.
balance_by_geography = df.groupby('Geography')['Balance'].sum()

print("\nTotal saldo berdasarkan Geografi:")
print(balance_by_geography)

# e. Simpan hasil pengolahan ke file baru (hasil_praktik_mandiri.xlsx).
# Kita akan menyimpan statistik dan hasil pengelompokan ke dalam file Excel yang sama, tetapi di sheet yang berbeda.
with pd.ExcelWriter('hasil_praktik_mandiri.xlsx') as writer:
    # Simpan statistik CreditScore
    statistik_df = pd.DataFrame({
        'Statistik': ['Rata-rata', 'Median', 'Modus'],
        'Nilai': [credit_score_mean, credit_score_median, credit_score_mode]
    })
    statistik_df.to_excel(writer, sheet_name='Statistik_CreditScore', index=False)

    # Simpan total Balance per Geografi
    balance_by_geography.to_excel(writer, sheet_name='Total_Saldo_per_Geografi')

print("\nHasil pengolahan telah disimpan ke 'hasil_praktik_mandiri.xlsx'")