import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 20)

try:
    dataset_retail = pd.read_csv('data_retail.csv', sep=';')

    print("================== 5 Baris Pertama (Data Asli) ==================")
    print(dataset_retail.head())

    print("\n================== 5 Baris Terakhir (Data Asli) ===================")
    print(dataset_retail.tail())

    print("\n================== Jumlah Baris dan Kolom ===================")
    print(f"Dataset ini memiliki {dataset_retail.shape[0]} baris dan {dataset_retail.shape[1]} kolom.")

    dataset_retail['First_Transaction'] = pd.to_datetime(dataset_retail['First_Transaction']/1000, unit='s', origin='1970-01-01').dt.date
    dataset_retail['Last_Transaction'] = pd.to_datetime(dataset_retail['Last_Transaction']/1000, unit='s', origin='1970-01-01').dt.date

    dataset_retail.sort_values('First_Transaction', inplace=True)

    print("\n======= Dataset Setelah Format Tanggal Diubah (5 Baris Pertama) =======")
    print(dataset_retail.head())

except FileNotFoundError:
    print("\nError: File 'data_retail.csv' tidak ditemukan.")
    print("Pastikan file tersebut berada di folder yang sama dengan skrip Anda.")