# APD - Algoritma dan Struktur Data

Repository ini berisi kumpulan tugas, UTS, dan UAS untuk mata kuliah **Algoritma dan Struktur Data (APD)**.

## 📚 Deskripsi Repository

Repository ini digunakan untuk menyimpan dan mengelola semua file tugas, ujian tengah semester (UTS), dan ujian akhir semester (UAS) dari kuliah Algoritma dan Struktur Data. Setiap folder berisi solusi dan implementasi berbagai konsep algoritma dan struktur data dengan Python.

## 📁 Struktur Folder

- **tugas 1** - Tugas pertama mata kuliah
- **tugas 2** - Tugas kedua mata kuliah
- **UTS** - File dan solusi Ujian Tengah Semester
- **UAS** - File dan solusi Ujian Akhir Semester

## 🛠️ Tech Stack

- **Language**: Python 🐍
- **Editor**: Visual Studio Code 💻
- **Version Control**: Git & GitHub

### Libraries:
- **pandas** - Data manipulation & analysis
- **matplotlib** - Data visualization
- **seaborn** - Advanced data visualization
- **numpy** - Numerical computing

## 📦 Install Dependencies

Untuk menginstall semua required libraries, jalankan:

```bash
pip install pandas matplotlib seaborn numpy
```


## 📝 Materi yang Dicakup

### Data Analysis & Visualization
- Data manipulation dengan pandas
- Visualisasi dengan matplotlib & seaborn
- Statistical analysis

## 📚 Resources

- [Python Official Docs](https://docs.python.org/3/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Seaborn Documentation](https://seaborn.pydata.org/)
- [NumPy Documentation](https://numpy.org/doc/)

## 📊 Contoh Penggunaan Library

### Pandas - Data Manipulation
```python
import pandas as pd

# Membaca CSV file
df = pd.read_csv('data.csv')

# Menampilkan 5 baris pertama
print(df.head())

# Statistik deskriptif
print(df.describe())

# Filter data
filtered_df = df[df['column'] > 10]
```

### Matplotlib & Seaborn - Visualization
```python
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_style("darkgrid")

# Scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='x_col', y='y_col')
plt.title('Scatter Plot')
plt.show()

# Bar plot
sns.barplot(data=df, x='category', y='value')
plt.show()
```

### NumPy - Numerical Computing
```python
import numpy as np

# Create array
arr = np.array([1, 2, 3, 4, 5])

# Mathematical operations
print(np.mean(arr))
print(np.std(arr))
print(np.sum(arr))
```



**Dibuat oleh:** Alfauzi-S  
**Tahun:** 2025
