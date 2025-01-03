import pandas as pd
from sqlalchemy import create_engine

# Koneksi ke database
engine = create_engine("mysql+pymysql://python_user@localhost/sales_database")
# Koneksi menggunakan root
#engine_root = create_engine("mysql+pymysql://root:your_root_password@localhost/sales_database")

# Membaca dataset
excel_file  = "D:/Portofolio_Project/Portfolio/Data Analysis/end-to-end/salesdata.xlsx"

# Daftar nama sheet
sheets = [
    "fact_InternetSales",
    "dim_ProductCategory",
    "dim_ProductSubcategory",
    "dim_Product",
    "dim_SalesTeritory",
    "dim_Currency",
    "dim_Customer"
]

# Loop untuk membaca sheet dan menyimpannya ke MySQL
for sheet in sheets:
    # Baca setiap sheet dari Excel
    df = pd.read_excel(excel_file, sheet_name=sheet)
    
    # Simpan ke database MySQL
    df.to_sql(name=sheet.lower(), con=engine, if_exists="replace", index=False) 
    print(f"Sheet '{sheet}' berhasil dimasukkan ke database sebagai tabel '{sheet.lower()}'.")
    #df.to_sql(name="test_table", con=engine_root, if_exists="replace", index=False)
    
# Verifikasi tabel di database
with engine.connect() as connection:
    result = connection.execute("SHOW TABLES;")
    print("Daftar tabel dalam database:")
    for row in result:
        print(row[0])
        
"""# Operasi menggunakan root
with engine_root.connect() as connection:
    connection.execute("SHOW TABLES;")
    print("Operasi dengan root berhasil.")"""
