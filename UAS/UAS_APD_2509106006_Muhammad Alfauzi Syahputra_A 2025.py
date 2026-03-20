import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('diabetes.csv')

fig, axes = plt.subplots(2, 3, figsize=(18, 12))
fig.suptitle('Visualisasi Dataset Diabetes', fontsize=16, fontweight='bold')

# 1. BAR PLOT
ax = plt.subplot(2, 3, 1)
databar = df['Outcome'].value_counts().reset_index()
databar.columns = ['Outcome', 'Counts']
sns.barplot(data=databar, x='Outcome', y='Counts', palette=['#FF2929', '#3D3BF3'], ax=ax)
ax.set_title('BAR - Jumlah Pasien per Outcome')
ax.set_xlabel('Status')
ax.set_ylabel('Jumlah Pasien')
ax.set_xticklabels(['Tidak Diabetes', 'Diabetes'])

# 2. HISTOGRAM PLOT
ax = plt.subplot(2, 3, 2)
sns.histplot(data=df, x='Glucose', hue='Outcome', kde=True, bins=50, palette=['#3D3BF3', '#FF2929'], ax=ax)
ax.set_title('HIST - Distribusi Kadar Glukosa')
ax.set_xlabel('Kadar Glukosa (mg/dL)')
ax.set_ylabel('Frekuensi')
ax.legend(title='Outcome', labels=['Tidak Diabetes', 'Diabetes'])

# 3. SCATTER PLOT
ax = plt.subplot(2, 3, 3)
sns.scatterplot(data=df, x='Glucose', y='BMI', hue='Outcome', palette=['#3D3BF3', '#FF2929'], alpha=0.7, ax=ax)
ax.set_title('Scatter - Glukosa vs BMI')
ax.set_xlabel('Kadar Glukosa (mg/dL)')
ax.set_ylabel('Indeks Massa Tubuh (BMI)')
ax.legend(title='Outcome', labels=['Tidak Diabetes', 'Diabetes'])

# 4. HEATMAP
ax = plt.subplot(2, 3, 4)
sns.heatmap(df.corr(), annot=True, center=0, fmt='.2f', cmap='coolwarm', ax=ax)
ax.set_title('Heatmap - Matriks Korelasi')

# 5. BOXPLOT
ax = plt.subplot(2, 3, 6)
sns.boxplot(data=df, x='Outcome', y='DiabetesPedigreeFunction', palette=['#FF2929', '#3D3BF3'], ax=ax)
ax.set_title('Boxplot - Diabetes Pedigree Function per Outcome')
ax.set_xlabel('Status')
ax.set_ylabel('Diabetes Pedigree Function')
ax.set_xticklabels(['Tidak Diabetes', 'Diabetes'])

# 6. LINEPLOT
ax = plt.subplot(2, 3, 5)
data = df.groupby(['Age', 'Outcome']).size().reset_index(name='Count')
df0 = data[data['Outcome'] == 0]
df1 = data[data['Outcome'] == 1]

ax.plot(df0['Age'], df0['Count'], label='Tidak Diabetes', color ='#FF2929')
ax.plot(df1['Age'], df1['Count'], label='Diabetes', color ='#3D3BF3')
ax.set_title('Line - Jumlah Pasien vs Usia, per Outcome')
ax.set_xlabel('Usia')
ax.set_ylabel('Jumlah Pasien')
ax.legend(title='Outcome')
ax.grid(True)

plt.tight_layout()
plt.show()