import pandas as pd

# a. Membaca data dari file penjualan.csv
try:
    df = pd.read_csv('penjualan.csv')
    print("Data penjualan.csv berhasil dibaca:")
    print(df)
    print("-" * 30)

    # b. Menghitung total pendapatan untuk setiap baris
    df['Total Pendapatan'] = df['Jumlah'] * df['Harga']
    print("\nData dengan kolom 'Total Pendapatan':")
    print(df)
    print("-" * 30)

    # c. Menghitung dan menampilkan total pendapatan keseluruhan
    total_pendapatan_keseluruhan = df['Total Pendapatan'].sum()
    print(f"\nTotal Pendapatan Keseluruhan: Rp {total_pendapatan_keseluruhan:,.0f}")
    print("-" * 30)

    # d. Menyimpan hasilnya ke file penjualan_bersih.xlsx
    nama_file_output = 'penjualan_bersih.xlsx'
    df.to_excel(nama_file_output, index=False)
    print(f"\nData berhasil disimpan ke dalam file '{nama_file_output}'")

except FileNotFoundError:
    print("Error: File 'penjualan.csv' tidak ditemukan.")
except Exception as e:
    print(f"Terjadi error: {e}")