# End-to-End Data Analysis and Power BI Dashboard

## Project Objective

In this project, the goal is to analyze raw sales data, clean and transform it, store it in a MySQL database, analyze it in Python, and then create an interactive Power BI dashboard. The dashboard will provide real-time insights into sales performance, customer demographics, product trends, and more, enabling better decision-making and proactive management.

## Project Structure

This project follows a structured approach with the following key steps:

### 1. Data Preprocessing
- Load raw sales data from an `.xlsx` file and convert it into SQL tables using Python and SQLAlchemy.
- There are 7 sheets in the file, each of which is converted into a separate table in the database.

### 2. Data Processing
- The dataset is processed directly in a Jupyter Notebook using Python.
- Perform data cleaning, handle missing values, normalize formats, and ensure data consistency before further analysis.
- After cleaning the data, store it in MySQL using SQLAlchemy for database management.

### 3. Data Analysis
- Perform data analysis using Python libraries (e.g., Pandas, NumPy).
- Generate insights on sales trends, customer behavior, and product performance.
- Convert the analysis results into CSV format for use in Power BI.

### 4. Power BI Dashboard
- Connect Power BI to the CSV files generated in the previous steps.
- Design an interactive dashboard that reflects key sales metrics and updates in real-time.

## Project Steps

### 1. Dataset Processing
- **Python Script**: `Data_cleaning.py`
  - This script loads, cleans, and preprocesses the dataset.
  - It handles missing data, outliers, and transforms the dataset into a clean format.
  - The script also configures a connection to MySQL using SQLAlchemy to load cleaned data into the database.

### 2. SQL Database Integration
- The **`Data_cleaning.py`** script connects to a MySQL database and loads cleaned data directly into the database.
- This is done using the SQLAlchemy engine and the `pandas.read_sql()` function in Jupyter Notebook.
  
#### Example of MySQL connection setup in Python:
```python
from sqlalchemy import create_engine
import pandas as pd
import time
from pymysql import OperationalError

# MySQL Connection Configuration
engine = create_engine(
    'mysql+pymysql://python_user@localhost/sales_database',
    pool_size=10,
    max_overflow=20,
    pool_recycle=1800,  # Recycle connection every 1800 seconds
    pool_pre_ping=True  # Check connection before use
)

retry_attempts = 5
retry_delay = 5  # Delay in seconds between retry attempts

for attempt in range(retry_attempts):
    try:
        # Run SQL query
        query = "SELECT * FROM clean_sales_data_table"
        df = pd.read_sql(query, engine)  # Load data from MySQL into DataFrame
        print(df.head())
        break
    except OperationalError as e:
        print(f"Attempt {attempt + 1} failed: {e}")
        time.sleep(retry_delay)
else:
    print("Failed to connect after multiple attempts.")
```

### 3. Power BI Dashboard
- **Power BI File**: `sales-retail-dashboard.pbix`
  - This Power BI file contains the interactive, real-time dashboard built using the cleaned dataset.
  - The dashboard includes key visualizations such as:
    - **Month-wise Sales**: A bar chart that shows sales of products by month.
    - **Sales by Product Category**: A pie chart representing the sales distribution across different product categories (e.g., Bikes, Components, Clothing, and Accessories).
    - **Sales Trends**: Trendlines showing sales growth over time.
    - **Customer Demographics Insights**: Data visualizations showing how sales vary based on customer demographics (e.g., gender, income, etc.).

## Folder Structure

```
Project/
│
├── Data/
│   ├── salesdata.xlsx            # Raw sales data in Excel format
│   ├── df.csv                    # Processed and cleaned data for Power BI
│
├── Scripts/
│   ├── End-to-End.py             # Python script for data cleaning and preprocessing
│   ├── export_to_sql.py          # Python script to export cleaned data to SQL
│
├── SQL/
│   ├── queries/                 # SQL scripts for data preprocessing and transformation
│   │   ├── create_tables.sql    # SQL script to create necessary tables in MySQL
│   │   ├── data_transformation.sql  # SQL script for transforming raw data
│   │   └── data_inserts.sql     # SQL script for inserting data into tables
│   └── sales_database.sql       # SQL dump of the cleaned database
│
├── PowerBI/
│   ├── sales-retail-dashboard.pbix  # Power BI dashboard file
│
└── Output/
    ├── clean_sales_data_table.sql   # SQL file for cleaned sales data
    └── multiple_tables.sql          # SQL file for multiple tables
```

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/retail-sales-dashboard.git
   cd retail-sales-dashboard
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Load the raw dataset into MySQL using the SQL dump file (`sales_database.sql`).

4. Run the Python script `Data_cleaning.py` to clean and preprocess the dataset. This script will connect to MySQL and load the cleaned data.

5. Export the cleaned data to CSV files using the script or manually save the necessary data for Power BI.

6. Open the Power BI file `sales-retail-dashboard.pbix` and connect it to the CSV files.

## Future Enhancements

- **Data Quality Improvements**: Enhance data cleaning steps to handle more edge cases and complex data anomalies.
- **Advanced Analytics**: Implement machine learning models for predictive analytics (e.g., forecasting future sales).
- **Dashboard Features**: Add more advanced interactivity to the Power BI dashboard, such as filters for specific products, regions, or time periods.

```

### Penjelasan:

1. **Data Preprocessing**: Langkah ini menggunakan Python dan SQLAlchemy untuk memuat data dari file `.xlsx` dan mengkonversinya ke dalam database MySQL secara langsung, bukan ekspor SQL manual. Koneksi ke MySQL dilakukan dengan SQLAlchemy dan data dibaca langsung ke dalam notebook Jupyter menggunakan `pandas.read_sql()`.

2. **MySQL Connection**: Saya telah menambahkan kode Python untuk mengonfigurasi koneksi MySQL menggunakan SQLAlchemy, serta cara membaca data dari database MySQL ke dalam DataFrame Pandas.

3. **Power BI Dashboard**: File Power BI (sales-retail-dashboard.pbix) berisi visualisasi interaktif, termasuk tren penjualan bulanan, distribusi kategori produk, demografi pelanggan, dan perubahan penjualan dari waktu ke waktu.

4. **Project Steps dan Folder Structure**: Data dibersihkan menggunakan Python dan SQL, disimpan di MySQL, lalu divisualisasikan dalam dashboard Power BI yang interaktif.
```
