#!/usr/bin/env python3
"""Daily AI/ML Tutorial Generator for CS Students"""

import json
import os
from datetime import datetime, timezone, timedelta

WIB = timezone(timedelta(hours=7))

TUTORIALS = [
    # ==================== PYTHON BASICS ====================
    {
        "category": "Python Fundamentals",
        "title": "NumPy: Array Operations untuk Data Science",
        "python_version": "3.8+",
        "difficulty": "Beginner",
        "content": """
## Apa itu NumPy?

NumPy (Numerical Python) adalah library fundamental untuk computational programming di Python. Library ini menyediakan objek **ndarray** (N-dimensional array) yang jauh lebih cepat dan efisien dibanding Python list biasa.

## Kenapa Harus Pakai NumPy?

| Fitur | Python List | NumPy Array |
|-------|-------------|-------------|
| Kecepatan | Lambat | 10-100x lebih cepat |
| Memori | Lebih banyak | Lebih hemat |
| Operasi | Harus manual | Vectorized (otomatis) |
| Matematika | Import math dulu | Built-in |

## Install

```bash
pip install numpy
```

## Membuat Array

```python
import numpy as np

# Dari Python list
arr1 = np.array([1, 2, 3, 4, 5])
print(type(arr1))       # <class 'numpy.ndarray'>
print(arr1.shape)       # (5,)
print(arr1.dtype)       # int64

# Array 2D (matrix)
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(matrix.shape)     # (2, 3) -> 2 baris, 3 kolom

# Array kosong dengan dtype tertentu
zeros = np.zeros((3, 3))        # Matrix 3x3 berisi 0
ones = np.ones((2, 4))          # Matrix 2x4 berisi 1
identity = np.eye(3)            # Matrix identitas 3x3
random_arr = np.random.rand(5)  # 5 angka random 0-1
```

## Operasi Dasar

```python
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

# Aritmatika (vectorized - tanpa loop!)
print(a + b)        # [ 6  8 10 12]
print(a * b)        # [ 5 12 21 32]
print(a ** 2)       # [ 1  4  9 16]

# Aggregasi
print(a.sum())      # 10
print(a.mean())     # 2.5
print(a.std())      # 1.118...
print(a.min())      # 1
print(a.max())      # 4

# Indexing dan Slicing
arr = np.array([10, 20, 30, 40, 50])
print(arr[0])       # 10
print(arr[1:4])     # [20 30 40]
print(arr[arr > 25]) # [30 40 50] -> Boolean indexing!

# Reshape
flat = np.arange(12)
matrix_3x4 = flat.reshape(3, 4)
print(matrix_3x4)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
```

## Broadcasting

Broadcasting adalah fitur NumPy yang memungkinkan operasi antara array dengan ukuran berbeda:

```python
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

# Tambahkan vektor ke setiap baris
vector = np.array([10, 20, 30])
result = matrix + vector
print(result)
# [[11 22 33]
#  [14 25 36]]

# Kalikan setiap elemen dengan scalar
print(matrix * 2)
# [[ 2  4  6]
#  [ 8 10 12]]
```

## Kesalahan Umum

```python
# ❌ Salah: Menggunakan Python loop untuk operasi array
result = []
for x in arr:
    result.append(x * 2)

# ✅ Benar: Gunakan vectorized operation
result = arr * 2

# ❌ Salah: Shape mismatch tanpa sadar
a = np.array([1, 2, 3])
b = np.array([1, 2])
# print(a + b)  # Error! Shapes tidak cocok

# ✅ Benar: Cek shape dulu
print(a.shape)  # (3,)
print(b.shape)  # (2,)
```

## Latihan

1. Buat array 10 angka dari 0-99 yang berurutan
2. Hitung rata-rata, median, dan standar deviasi
3. Filter semua angka genap
4. Reshape menjadi matrix 2x5

## Sumber Belajar

- [NumPy Official Documentation](https://numpy.org/doc/)
- [NumPy Tutorial](https://numpy.org/doc/stable/user/quickstart.html)
"""
    },
    {
        "category": "Python Fundamentals",
        "title": "Pandas: Data Manipulation untuk Analysis",
        "python_version": "3.8+",
        "difficulty": "Beginner",
        "content": """
## Apa itu Pandas?

Pandas adalah library Python untuk **data manipulation** dan **analysis**. Library ini menyediakan struktur data seperti DataFrame yang mirip dengan spreadsheet/Excel.

## DataFrame vs Series

```python
import pandas as pd

# Series = 1D array dengan label
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s)
# a    10
# b    20
# c    30

# DataFrame = 2D table (kumpulan Series)
df = pd.DataFrame({
    'nama': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'umur': [25, 30, 35, 28],
    'ipk': [3.8, 3.5, 3.9, 3.7],
    'jurusan': ['TI', 'SI', 'TI', 'SK']
})
print(df)
#       nama  umur  ipk jurusan
# 0    Alice    25  3.8      TI
# 1      Bob    30  3.5      SI
# 2  Charlie    35  3.9      TI
# 3    Diana    28  3.7      SK
```

## Import Data

```python
# Dari CSV
df = pd.read_csv('data.csv')

# Dari Excel
df = pd.read_excel('data.xlsx')

# Dari JSON
df = pd.read_json('data.json')

# Dari database
import sqlite3
conn = sqlite3.connect('db.sqlite')
df = pd.read_sql('SELECT * FROM users', conn)
```

## Exploring Data

```python
# Info dasar
print(df.head())        # 5 baris pertama
print(df.tail())        # 5 baris terakhir
print(df.shape)         # (jumlah_baris, jumlah_kolom)
print(df.info())        # Info tipe data
print(df.describe())    # Statistik deskriptif

# Cek missing values
print(df.isnull().sum())

# Unique values
print(df['jurusan'].unique())
print(df['jurusan'].value_counts())
```

## Filtering Data

```python
# Satu kondisi
mahasiswa_ti = df[df['jurusan'] == 'TI']

# Multiple kondisi (AND)
 senior_ti = df[(df['jurusan'] == 'TI') & (df['umur'] > 30)]

# Multiple kondisi (OR)
 filterOR = df[(df['jurusan'] == 'TI') | (df['ipk'] > 3.8)]

# Menggunakan query()
 filterQuery = df.query('jurusan == "TI" and umur > 30')
```

## Manipulasi Kolom

```python
# Tambah kolom baru
df['status'] = df['ipk'].apply(lambda x: 'Cum Laude' if x >= 3.8 else 'Normal')

# Rename kolom
df = df.rename(columns={'nama': 'name', 'umur': 'age'})

# Hapus kolom
df = df.drop(columns=['status'])

# Reorder kolom
df = df[['jurusan', 'nama', 'ipk', 'umur']]
```

## Grouping

```python
# Group by satu kolom
by_jurusan = df.groupby('jurusan').agg({
    'ipk': ['mean', 'max', 'count'],
    'umur': 'mean'
})
print(by_jurusan)

# Group by multiple kolom
df.groupby(['jurusan', 'status']).size()
```

## Merge Data

```python
# Buat dua dataframe
df1 = pd.DataFrame({'id': [1, 2, 3], 'nama': ['A', 'B', 'C']})
df2 = pd.DataFrame({'id': [2, 3, 4], 'nilai': [80, 90, 85]})

# Inner join (hanya yang cocok)
inner = pd.merge(df1, df2, on='id', how='inner')

# Left join (semua dari df1)
left = pd.merge(df1, df2, on='id', how='left')

# Outer join (semua)
outer = pd.merge(df1, df2, on='id', how='outer')
```

## Export Data

```python
# Ke CSV
df.to_csv('output.csv', index=False)

# Ke Excel
df.to_excel('output.xlsx', index=False)

# Ke JSON
df.to_json('output.json', orient='records')
```

## Latihan

1. Buat DataFrame dari dict dengan minimal 10 data
2. Filter data dengan 2 kondisi
3. Buat kolom baru dengan apply()
4. Group by dan hitung aggregasi

## Sumber Belajar

- [Pandas Official](https://pandas.pydata.org/docs/)
- [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
"""
    },
    {
        "category": "Python Fundamentals",
        "title": "Matplotlib: Visualisasi Data",
        "python_version": "3.8+",
        "difficulty": "Beginner",
        "content": """
## Apa itu Matplotlib?

Matplotlib adalah library untuk membuat **visualisasi data** di Python. Library ini bisa membuat berbagai jenis chart: line, bar, scatter, heatmap, dan banyak lagi.

## Line Chart

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(12, 6))
plt.plot(x, y1, label='sin(x)', color='blue', linewidth=2)
plt.plot(x, y2, label='cos(x)', color='red', linewidth=2, linestyle='--')
plt.title('Sinus vs Cosinus', fontsize=16)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('line_chart.png', dpi=150, bbox_inches='tight')
plt.show()
```

## Bar Chart

```python
languages = ['Python', 'JavaScript', 'Java', 'C++', 'Go']
popularity = [28.1, 17.5, 15.5, 10.2, 8.7]
colors = ['#3776AB', '#F7DF1E', '#ED8B00', '#00599C', '#00ADD8']

plt.figure(figsize=(10, 6))
bars = plt.bar(languages, popularity, color=colors)
plt.title('Popularity Programming Language 2024')
plt.ylabel('Market Share (%)')

# Tambah label di atas bar
for bar, val in zip(bars, popularity):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
             f'{val}%', ha='center', fontweight='bold')

plt.savefig('bar_chart.png')
plt.show()
```

## Scatter Plot

```python
np.random.seed(42)
x = np.random.randn(100)
y = x * 2 + np.random.randn(100) * 0.5
colors = np.random.rand(100)
sizes = np.abs(np.random.randn(100)) * 100

plt.figure(figsize=(10, 8))
scatter = plt.scatter(x, y, c=colors, s=sizes, alpha=0.6, cmap='viridis')
plt.colorbar(scatter)
plt.title('Scatter Plot with Color Mapping')
plt.xlabel('X Value')
plt.ylabel('Y Value')
plt.savefig('scatter_plot.png')
plt.show()
```

## Subplots

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Plot 1: Line
axes[0, 0].plot(np.random.rand(50))
axes[0, 0].set_title('Line Chart')

# Plot 2: Bar
axes[0, 1].bar(['A', 'B', 'C'], [3, 7, 5])
axes[0, 1].set_title('Bar Chart')

# Plot 3: Scatter
axes[1, 0].scatter(np.random.rand(30), np.random.rand(30))
axes[1, 0].set_title('Scatter Plot')

# Plot 4: Pie
axes[1, 1].pie([30, 40, 30], labels=['A', 'B', 'C'], autopct='%1.1f%%')
axes[1, 1].set_title('Pie Chart')

plt.tight_layout()
plt.savefig('subplots.png')
plt.show()
```

## Heatmap

```python
import seaborn as sns

data = np.random.rand(10, 10)
plt.figure(figsize=(10, 8))
sns.heatmap(data, annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Heatmap')
plt.savefig('heatmap.png')
plt.show()
```

## Tips dan Best Practice

```python
# 1. Selalu save sebelum show
plt.savefig('output.png', dpi=300, bbox_inches='tight')
plt.show()

# 2. Gunakan figsize untuk kontrol ukuran
plt.figure(figsize=(12, 8))  # width=12, height=8

# 3. Tambahkan grid untuk readability
plt.grid(True, alpha=0.3)

# 4. Gunakan tight_layout() untuk subplots
plt.tight_layout()

# 5. Set style
plt.style.use('seaborn-v0_8')  # Atau 'ggplot', 'fivethirtyeight'
```

## Latihan

1. Buat line chart pertumbuhan populasi Indonesia dari tahun 2000-2024
2. Buat bar chart perbandingan nilai 5 mata kuliah
3. Buat scatter plot hubungan waktu belajar vs nilai ujian
4. Gabungkan 4 chart berbeda dalam 1 figure dengan subplots

## Sumber Belajar

- [Matplotlib Official](https://matplotlib.org/)
- [Matplotlib Tutorial](https://matplotlib.org/stable/tutorials/index.html)
"""
    },

    # ==================== DEEP LEARNING ====================
    {
        "category": "Deep Learning",
        "title": "PyTorch: Tensor Operations untuk Deep Learning",
        "python_version": "3.8+",
        "difficulty": "Intermediate",
        "content": """
## Apa itu Tensor?

Tensor adalah struktur data fundamental dalam deep learning. Tensor adalah **NumPy array dengan GPU support**. Di PyTorch, semua operasi dilakukan pada tensor.

## Install PyTorch

```bash
# CPU only
pip install torch torchvision

# Dengan CUDA (GPU)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

## Membuat Tensor

```python
import torch

# Dari Python list
x = torch.tensor([1, 2, 3, 4, 5])
print(x)          # tensor([1, 2, 3, 4, 5])
print(x.dtype)    # torch.int64
print(x.shape)    # torch.Size([5])

# Float tensor (default untuk deep learning)
x_float = torch.tensor([1.0, 2.0, 3.0])
print(x_float.dtype)  # torch.float32

# Dengan spesifik dtype
x64 = torch.tensor([1.0], dtype=torch.float64)

# Special tensors
zeros = torch.zeros(3, 3)      # Matrix 3x3 berisi 0
ones = torch.ones(2, 4)        # Matrix 2x4 berisi 1
rand = torch.randn(3, 3)       # Random normal distribution
eye = torch.eye(3)             # Identity matrix
arange = torch.arange(0, 10, 2) # [0, 2, 4, 6, 8]
linspace = torch.linspace(0, 1, 5)  # [0, 0.25, 0.5, 0.75, 1]
```

## GPU Acceleration

```python
# Cek apakah GPU tersedia
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f'Using device: {device}')

# Pindahkan tensor ke GPU
x = torch.randn(1000, 1000)
x_gpu = x.to(device)  # atau x.cuda() / x.cpu()

# Operasi di GPU (10-100x lebih cepat!)
y = torch.randn(1000, 1000).to(device)
z = torch.mm(x_gpu, y)  # Matrix multiplication

# Waktu perbandingan
import time

# CPU
start = time.time()
for _ in range(100):
    _ = torch.mm(x, y)
print(f'CPU: {time.time() - start:.2f}s')

# GPU
x_gpu = x.to(device)
y_gpu = y.to(device)
start = time.time()
for _ in range(100):
    _ = torch.mm(x_gpu, y_gpu)
print(f'GPU: {time.time() - start:.2f}s')
```

## Operasi Dasar

```python
a = torch.tensor([1.0, 2.0, 3.0])
b = torch.tensor([4.0, 5.0, 6.0])

# Aritmatika
print(a + b)      # tensor([5., 7., 9.])
print(a - b)      # tensor([-3., -3., -3.])
print(a * b)      # tensor([ 4., 10., 18.])
print(a / b)      # tensor([0.2500, 0.4000, 0.5000])
print(a ** 2)     # tensor([1., 4., 9.])

# Aggregasi
print(a.sum())    # tensor(6.)
print(a.mean())   # tensor(2.)
print(a.std())    # tensor(1.)
print(a.max())    # tensor(3.)

# Matrix operations
m1 = torch.randn(3, 4)
m2 = torch.randn(4, 3)
result = torch.mm(m1, m2)  # Matrix multiply -> (3, 3)
```

## Autograd: Automatic Differentiation

```python
# Autograd adalah jantung dari backpropagation di PyTorch
# require_grad=True memberitahu PyTorch untuk track gradient

x = torch.tensor(2.0, requires_grad=True)

# Forward pass
y = x ** 2 + 3 * x + 1  # y = x^2 + 3x + 1
print(y)  # tensor(11., grad_fn=<AddBackward0>)

# Backward pass (hitung gradient)
y.backward()

# dy/dx = 2x + 3 = 2(2) + 3 = 7
print(x.grad)  # tensor(7.)

# Dalam deep learning:
# 1. Forward pass: hitung prediksi
# 2. Hitung loss (seberapa jauh prediksi dari jawaban)
# 3. Backward pass: hitung gradient semua parameter
# 4. Update parameter berdasarkan gradient
```

## Reshape Operations

```python
x = torch.arange(12)
print(x)  # tensor([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])

# Reshape
y = x.reshape(3, 4)    # 3 baris, 4 kolom
z = x.view(3, 4)       # Sama seperti reshape
w = x.view(4, 3)

# Transpose
m = torch.randn(2, 3)
print(m.shape)          # torch.Size([2, 3])
print(m.T.shape)        # torch.Size([3, 2])

# Flatten
matrix = torch.randn(3, 4)
flat = matrix.flatten()  # 1D tensor
print(flat.shape)        # torch.Size([12])

# Unsqueeze (tambah dimensi)
x = torch.tensor([1, 2, 3])
print(x.shape)           # torch.Size([3])
y = x.unsqueeze(0)       # (1, 3)
z = x.unsqueeze(1)       # (3, 1)
```

## Autograd dengan Neural Network

```python
import torch
import torch.nn as nn

# Buat model sederhana
model = nn.Linear(1, 1)  # 1 input, 1 output

# Forward pass
x = torch.tensor([[2.0]])
y_pred = model(x)
print(y_pred)

# Hitung loss
y_true = torch.tensor([[5.0]])
loss = nn.MSELoss()(y_pred, y_true)
print(f'Loss: {loss.item()}')

# Backward pass
loss.backward()

# Lihat gradient
for name, param in model.named_parameters():
    print(f'{name}: {param.grad}')
```

## Kesalahan Umum

```python
# ❌ Lupa detach() saat plotting
x = torch.tensor(2.0, requires_grad=True)
y = x ** 2
# plt.plot(x, y)  # Error!

# ✅ Benar
plt.plot(x.detach().numpy(), y.detach().numpy())

# ❌ In-place operations memutus computational graph
x = torch.tensor([1.0, 2.0], requires_grad=True)
x += 1  # In-place, bisa error

# ✅ Benar
x = torch.tensor([1.0, 2.0], requires_grad=True)
x = x + 1  # Out-of-place

# ❌ Membandingkan tensor langsung
print(x == y)  # Returns tensor, bukan bool

# ✅ Benar
print(torch.equal(x, y))
```

## Latihan

1. Buat tensor 5x5 dengan angka random dan lakukan operasi reshape
2. Gunakan autograd untuk menghitung gradient f(x) = x^3 + 2x^2 - 5x
3. Bandingkan kecepatan operasi CPU vs GPU (jika tersedia)

## Sumber Belajar

- [PyTorch Official Tutorials](https://pytorch.org/tutorials/)
- [PyTorch Docs](https://pytorch.org/docs/stable/)
"""
    },
    {
        "category": "Deep Learning",
        "title": "Neural Network dari Nol dengan PyTorch",
        "python_version": "3.8+",
        "difficulty": "Intermediate",
        "content": """
## Arsitektur Neural Network

Neural Network terdiri dari:
1. **Input Layer**: Menerima data
2. **Hidden Layer(s)**: Memproses data
3. **Output Layer**: Menghasilkan prediksi

## Simple Neural Network

```python
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 1. Generate dummy data
X, y = make_classification(n_samples=1000, n_features=20,
                           n_informative=15, n_redundant=5,
                           random_state=42)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Scale data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Convert to tensors
X_train = torch.FloatTensor(X_train)
y_train = torch.FloatTensor(y_train).unsqueeze(1)
X_test = torch.FloatTensor(X_test)
y_test = torch.FloatTensor(y_test).unsqueeze(1)
```

## Define Model

```python
class SimpleNet(nn.Module):
    def __init__(self, input_size):
        super(SimpleNet, self).__init__()
        self.layers = nn.Sequential(
            nn.Linear(input_size, 64),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(32, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.layers(x)

# Buat model
model = SimpleNet(input_size=20)
print(model)
```

## Training Loop

```python
# Hyperparameters
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)
num_epochs = 100

# Training
for epoch in range(num_epochs):
    # Forward pass
    model.train()
    y_pred = model(X_train)
    loss = criterion(y_pred, y_train)

    # Backward pass
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    # Evaluation
    if (epoch + 1) % 10 == 0:
        model.eval()
        with torch.no_grad():
            y_test_pred = model(X_test)
            test_loss = criterion(y_test_pred, y_test)
            accuracy = (y_test_pred.round() == y_test).float().mean()

        print(f'Epoch [{epoch+1}/{num_epochs}], '
              f'Loss: {loss.item():.4f}, '
              f'Test Loss: {test_loss.item():.4f}, '
              f'Accuracy: {accuracy.item():.4f}')
```

## Advanced Model Architecture

```python
class AdvancedNet(nn.Module):
    def __init__(self, input_size, hidden_sizes, output_size):
        super(AdvancedNet, self).__init__()

        layers = []
        prev_size = input_size

        for hidden_size in hidden_sizes:
            layers.extend([
                nn.Linear(prev_size, hidden_size),
                nn.BatchNorm1d(hidden_size),
                nn.ReLU(),
                nn.Dropout(0.3)
            ])
            prev_size = hidden_size

        layers.append(nn.Linear(prev_size, output_size))
        self.network = nn.Sequential(*layers)

    def forward(self, x):
        return self.network(x)

# Multi-layer model
model = AdvancedNet(
    input_size=20,
    hidden_sizes=[128, 64, 32],
    output_size=1
)
print(model)
```

## Save and Load Model

```python
# Save model
torch.save(model.state_dict(), 'model.pth')

# Load model
loaded_model = SimpleNet(input_size=20)
loaded_model.load_state_dict(torch.load('model.pth'))
loaded_model.eval()
```

## Kesalahan Umum

```python
# ❌ Lupa model.train() saat training
# ❌ Lupa model.eval() saat inference
# ❌ Lupa torch.no_grad() saat evaluation
# ❌ Lupa optimizer.zero_grad()

# ✅ Benar
model.train()  # Set training mode
for epoch in range(num_epochs):
    optimizer.zero_grad()
    y_pred = model(X_train)
    loss = criterion(y_pred, y_train)
    loss.backward()
    optimizer.step()

model.eval()  # Set evaluation mode
with torch.no_grad():  # Disable gradient computation
    y_pred = model(X_test)
```

## Latihan

1. Buat neural network untuk klasifikasi MNIST dataset
2. Experiment dengan jumlah layer dan neuron
3. Tambahkan Batch Normalization dan Dropout
4. Implement learning rate scheduler

## Sumber Belajar

- [PyTorch Neural Networks Tutorial](https://pytorch.org/tutorials/beginner/blitz/neural_networks_tutorial.html)
- [CS231n: Deep Learning](http://cs231n.stanford.edu/)
"""
    },
    {
        "category": "Deep Learning",
        "title": "Convolutional Neural Network (CNN) untuk Image Classification",
        "python_version": "3.8+",
        "difficulty": "Intermediate",
        "content": """
## Apa itu CNN?

CNN (Convolutional Neural Network) adalah jenis neural network yang dirancang khusus untuk memproses data **grid-like** seperti gambar. CNN menggunakan **convolutional layers** untuk mengekstrak fitur dari gambar.

## Arsitektur CNN

```
Input Image → Conv Layer → Pooling → Conv Layer → Pooling → FC Layer → Output
     ↓              ↓           ↓           ↓          ↓         ↓         ↓
  (32x32x3)    (32x32x32)  (16x16x32)  (16x16x64) (8x8x64)  (256)    (10)
```

## CNN untuk MNIST

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# Data preparation
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

train_dataset = datasets.MNIST('./data', train=True, download=True, transform=transform)
test_dataset = datasets.MNIST('./data', train=False, transform=transform)

train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=1000)

# Define CNN
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.features = nn.Sequential(
            # Conv Layer 1: 1 -> 32 channels
            nn.Conv2d(1, 32, kernel_size=3, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),  # 28x28 -> 14x14

            # Conv Layer 2: 32 -> 64 channels
            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),  # 14x14 -> 7x7

            # Conv Layer 3: 64 -> 128 channels
            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),  # 7x7 -> 3x3
        )

        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(128 * 3 * 3, 256),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(256, 10)
        )

    def forward(self, x):
        x = self.features(x)
        x = self.classifier(x)
        return x

model = CNN()
print(model)
```

## Training

```python
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training loop
for epoch in range(10):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)

        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()

        if batch_idx % 100 == 0:
            print(f'Epoch {epoch}, Batch {batch_idx}, Loss: {loss.item():.4f}')

    # Test
    model.eval()
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            pred = output.argmax(dim=1)
            correct += pred.eq(target).sum().item()

    accuracy = 100. * correct / len(test_dataset)
    print(f'Epoch {epoch}, Accuracy: {accuracy:.2f}%')
```

## Pretrained Model (Transfer Learning)

```python
import torchvision.models as models

# Load pretrained ResNet18
model = models.resnet18(pretrained=True)

# Ganti output layer untuk 10 kelas
num_features = model.fc.in_features
model.fc = nn.Linear(num_features, 10)

# Freeze semua layer kecuali FC
for param in model.parameters():
    param.requires_grad = False
model.fc.weight.requires_grad = True
model.fc.bias.requires_grad = True
```

## Visualisasi Feature Maps

```python
import matplotlib.pyplot as plt

# Ambil feature maps dari layer pertama
def get_feature_maps(model, image):
    features = []
    def hook(module, input, output):
        features.append(output)

    model.features[0].register_forward_hook(hook)
    _ = model(image.unsqueeze(0))
    return features[0].detach()

# Plot feature maps
feature_maps = get_feature_maps(model, test_dataset[0][0])
fig, axes = plt.subplots(4, 8, figsize=(12, 6))
for i, ax in enumerate(axes.flat):
    ax.imshow(feature_maps[0, i].cpu().numpy(), cmap='viridis')
    ax.axis('off')
plt.tight_layout()
plt.savefig('feature_maps.png')
```

## Latihan

1. Implement CNN untuk klasifikasi CIFAR-10
2. Experiment dengan arsitektur berbeda
3. Gunakan transfer learning untuk klasifikasi gambar sendiri
4. Visualisasi confusion matrix

## Sumber Belajar

- [CS231n: CNN for Visual Recognition](http://cs231n.stanford.edu/)
- [PyTorch Vision Models](https://pytorch.org/vision/stable/models.html)
"""
    },

    # ==================== MACHINE LEARNING ====================
    {
        "category": "Machine Learning",
        "title": "Scikit-learn: Machine Learning untuk Pemula",
        "python_version": "3.8+",
        "difficulty": "Beginner",
        "content": """
## Apa itu Scikit-learn?

Scikit-learn adalah library Python untuk **machine learning**. Library ini menyediakan alat untuk:
- Classification (klasifikasi)
- Regression (regresi)
- Clustering (pengelompokan)
- Dimensionality reduction (pengurangan dimensi)

## Install

```bash
pip install scikit-learn
```

## Workflow ML

```
1. Load Data → 2. Preprocess → 3. Split → 4. Train → 5. Evaluate → 6. Tuning
```

## Classification

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. Load data
iris = load_iris()
X, y = iris.data, iris.target

# 2. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 4. Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. Evaluate
y_pred = model.predict(X_test)
print(f'Accuracy: {accuracy_score(y_test, y_pred):.4f}')
print(classification_report(y_test, y_pred))
```

## Regression

```python
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Generate sample data
X, y = make_regression(n_samples=100, n_features=5, noise=0.1)

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print(f'MSE: {mean_squared_error(y_test, y_pred):.4f}')
print(f'R2 Score: {r2_score(y_test, y_pred):.4f}')
```

## Clustering

```python
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Generate data
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.6)

# KMeans clustering
kmeans = KMeans(n_clusters=4, random_state=42)
labels = kmeans.fit_predict(X)
centroids = kmeans.cluster_centers_

# Visualize
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', alpha=0.6)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200)
plt.title('KMeans Clustering')
plt.savefig('clustering.png')
```

## Model Comparison

```python
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

models = {
    'Logistic Regression': LogisticRegression(),
    'SVM': SVC(),
    'Random Forest': RandomForestClassifier(),
    'KNN': KNeighborsClassifier()
}

for name, model in models.items():
    scores = cross_val_score(model, X_train, y_train, cv=5)
    print(f'{name}: {scores.mean():.4f} (+/- {scores.std():.4f})')
```

## Hyperparameter Tuning

```python
from sklearn.model_selection import GridSearchCV

# Define parameter grid
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10]
}

# Grid search
grid_search = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=5,
    n_jobs=-1,
    verbose=1
)
grid_search.fit(X_train, y_train)

print(f'Best params: {grid_search.best_params_}')
print(f'Best score: {grid_search.best_score_:.4f}')
```

## Latihan

1. Klasifikasi dataset MNIST
2. Regresi untuk prediksi harga rumah
3. Clustering customer data
4. Bandingkan minimal 3 model berbeda

## Sumber Belajar

- [Scikit-learn Official](https://scikit-learn.org/)
- [Scikit-learn Tutorials](https://scikit-learn.org/stable/tutorial/index.html)
"""
    },

    # ==================== C++ ====================
    {
        "category": "C++ for ML",
        "title": "C++ Smart Pointers untuk Memory Management",
        "cpp_version": "C++11+",
        "difficulty": "Intermediate",
        "content": """
## Apa itu Smart Pointers?

Smart pointers adalah **RAII (Resource Acquisition Is Initialization)** wrappers untuk raw pointers. Mereka otomatis membebaskan memori saat objek keluar dari scope.

## Kenapa Harus Pakai Smart Pointers?

```cpp
// ❌ Raw pointer - memory leak!
void bad_code() {
    int* ptr = new int(42);
    // Jika terjadi exception, memori tidak terbebas
    delete ptr; // Lupa = memory leak
}

// ✅ Smart pointer - otomatis cleanup
void good_code() {
    auto ptr = std::make_unique<int>(42);
    // Otomatis terbebas saat fungsi selesai
}
```

## std::unique_ptr

```cpp
#include <memory>
#include <iostream>

class MyClass {
public:
    MyClass(int val) : value(val) {
        std::cout << "Created: " << value << std::endl;
    }
    ~MyClass() {
        std::cout << "Destroyed: " << value << std::endl;
    }
    int value;
};

int main() {
    // Unique ownership - hanya 1 yang bisa memiliki
    auto ptr1 = std::make_unique<MyClass>(10);
    std::cout << "Value: " << ptr1->value << std::endl;

    // ❌ Cannot copy unique_ptr
    // auto ptr2 = ptr1;  // Error!

    // ✅ Can move ownership
    auto ptr2 = std::move(ptr1);
    // ptr1 sekarang nullptr
    std::cout << "ptr1 valid: " << (ptr1 != nullptr) << std::endl;
    std::cout << "ptr2 valid: " << (ptr2 != nullptr) << std::endl;

    return 0;
}  // ptr2 otomatis terbebas di sini
```

## std::shared_ptr

```cpp
#include <memory>
#include <iostream>

int main() {
    // Shared ownership - bisa dimiliki banyak
    auto sp1 = std::make_shared<int>(42);
    std::cout << "Use count: " << sp1.use_count() << std::endl;  // 1

    {
        auto sp2 = sp1;  // Copy - increases reference count
        std::cout << "Use count: " << sp1.use_count() << std::endl;  // 2
    }  // sp2 terbebas, use count turun

    std::cout << "Use count: " << sp1.use_count() << std::endl;  // 1
    return 0;
}
```

## Practical Example: Tree Structure

```cpp
#include <memory>
#include <string>
#include <vector>
#include <iostream>

struct TreeNode {
    std::string data;
    std::vector<std::unique_ptr<TreeNode>> children;

    TreeNode(std::string val) : data(std::move(val)) {}

    void add_child(std::string child_data) {
        children.push_back(std::make_unique<TreeNode>(std::move(child_data)));
    }

    void print(int depth = 0) {
        std::cout << std::string(depth * 2, ' ') << data << std::endl;
        for (auto& child : children) {
            child->print(depth + 1);
        }
    }
};

int main() {
    auto root = std::make_unique<TreeNode>("Root");
    root->add_child("Child 1");
    root->add_child("Child 2");
    root->children[0]->add_child("Grandchild 1");

    root->print();
    return 0;
}
```

## Common Pitfalls

```cpp
// ❌ Circular references with shared_ptr
struct Node {
    std::shared_ptr<Node> next;  // Memory leak!
};

// ✅ Use weak_ptr to break cycles
struct Node {
    std::shared_ptr<Node> next;
    std::weak_ptr<Node> prev;  // No cycle!
};

// ❌ Don't use make_shared with arrays
auto arr = std::make_shared<int[]>(10);  // C++20 only

// ✅ Use unique_ptr for arrays
auto arr = std::make_unique<int[]>(10);
```

## Performance Tips

```cpp
// 1. Prefer unique_ptr over shared_ptr
// unique_ptr has zero overhead vs raw pointer
// shared_ptr has reference counting overhead

// 2. Use make_unique/make_shared
auto p1 = std::make_unique<int>(42);  // Single allocation
auto p2 = std::unique_ptr<int>(new int(42));  // Two allocations

// 3. Use weak_ptr for caches/observers
std::weak_ptr<ExpensiveObject> cache;
```

## Latihan

1. Implement binary search tree using smart pointers
2. Create a graph structure with shared_ptr
3. Compare performance: unique_ptr vs shared_ptr vs raw pointer
4. Implement a simple garbage collector simulation

## Sumber Belajar

- [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/)
- [ cppreference.com](https://en.cppreference.com/)
"""
    },
    {
        "category": "C++ for ML",
        "title": "C++ Templates untuk Generic Programming",
        "cpp_version": "C++11+",
        "difficulty": "Intermediate",
        "content": """
## Apa itu Templates?

Templates memungkinkan menulis **kode generic** yang bekerja dengan tipe data apapun. Ini adalah fondasi dari **generic programming** di C++.

## Function Templates

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

// Template function
template <typename T>
T find_max(T a, T b) {
    return (a > b) ? a : b;
}

// Template dengan multiple type parameters
template <typename T, typename U>
auto add(T a, U b) -> decltype(a + b) {
    return a + b;
}

int main() {
    std::cout << find_max(3, 5) << std::endl;        // int
    std::cout << find_max(3.14, 2.71) << std::endl;  // double
    std::cout << find_max('a', 'z') << std::endl;    // char

    auto result = add(3, 2.14);  // int + double = double
    std::cout << result << std::endl;

    return 0;
}
```

## Class Templates

```cpp
template <typename T>
class Stack {
private:
    std::vector<T> elements;

public:
    void push(const T& elem) {
        elements.push_back(elem);
    }

    T pop() {
        T elem = elements.back();
        elements.pop_back();
        return elem;
    }

    T top() const {
        return elements.back();
    }

    bool empty() const {
        return elements.empty();
    }

    size_t size() const {
        return elements.size();
    }
};

int main() {
    Stack<int> intStack;
    intStack.push(1);
    intStack.push(2);
    std::cout << intStack.pop() << std::endl;  // 2

    Stack<std::string> strStack;
    strStack.push("Hello");
    strStack.push("World");
    std::cout << strStack.pop() << std::endl;  // World

    return 0;
}
```

## Template Specialization

```cpp
template <typename T>
class Printer {
public:
    void print(T value) {
        std::cout << "Value: " << value << std::endl;
    }
};

// Specialization for bool
template <>
class Printer<bool> {
public:
    void print(bool value) {
        std::cout << "Boolean: " << (value ? "true" : "false") << std::endl;
    }
};

// Specialization for pointer types
template <typename T>
class Printer<T*> {
public:
    void print(T* value) {
        std::cout << "Pointer to: " << *value << std::endl;
    }
};

int main() {
    Printer<int> intPrinter;
    intPrinter.print(42);  // Value: 42

    Printer<bool> boolPrinter;
    boolPrinter.print(true);  // Boolean: true

    int x = 10;
    Printer<int*> ptrPrinter;
    ptrPrinter.print(&x);  // Pointer to: 10

    return 0;
}
```

## Variadic Templates

```cpp
// Base case
void print() {}

// Variadic template
template <typename T, typename... Args>
void print(T first, Args... rest) {
    std::cout << first;
    if constexpr (sizeof...(rest) > 0) {
        std::cout << ", ";
        print(rest...);
    }
}

// Fold expression (C++17)
template <typename... Args>
auto sum(Args... args) {
    return (args + ...);
}

int main() {
    print(1, "hello", 3.14, 'x');  // 1, hello, 3.14, x

    std::cout << sum(1, 2, 3, 4, 5) << std::endl;  // 15

    return 0;
}
```

## Template Metaprogramming

```cpp
// Compile-time factorial
template <int N>
struct Factorial {
    static constexpr int value = N * Factorial<N-1>::value;
};

template <>
struct Factorial<0> {
    static constexpr int value = 1;
};

// Compile-time fibonacci
template <int N>
struct Fibonacci {
    static constexpr int value = Fibonacci<N-1>::value + Fibonacci<N-2>::value;
};

template <>
struct Fibonacci<0> { static constexpr int value = 0; };
template <>
struct Fibonacci<1> { static constexpr int value = 1; };

int main() {
    // Computed at compile time!
    std::cout << "5! = " << Factorial<5>::value << std::endl;  // 120
    std::cout << "Fib(10) = " << Fibonacci<10>::value << std::endl;  // 55

    return 0;
}
```

## SFINAE and Concepts (C++20)

```cpp
// SFINAE (Substitution Failure Is Not An Error)
template <typename T>
typename std::enable_if<std::is_arithmetic<T>::value, T>::type
safe_divide(T a, T b) {
    return b != 0 ? a / b : 0;
}

// C++20 Concepts (cleaner syntax)
template <typename T>
concept Numeric = std::is_arithmetic_v<T>;

template <Numeric T>
T safe_add(T a, T b) {
    return a + b;
}

int main() {
    std::cout << safe_divide(10, 3) << std::endl;
    std::cout << safe_add(1.5, 2.5) << std::endl;
    // safe_add("hello", "world");  // Error! Not Numeric
    return 0;
}
```

## Latihan

1. Implement generic Matrix class using templates
2. Create a type-safe heterogeneous container
3. Write a compile-time string concatenation
4. Implement a simple variant type using templates

## Sumber Belajar

- [C++ Templates: The Complete Guide](https://www.amazon.com/C-Templates-Complete-Guide-2nd/dp/0321714127)
- [cppreference Templates](https://en.cppreference.com/w/cpp/language/templates)
"""
    },

    # ==================== WEB AI ====================
    {
        "category": "Web AI",
        "title": "TensorFlow.js: Machine Learning di Browser",
        "javascript_version": "ES6+",
        "difficulty": "Intermediate",
        "content": """
## Apa itu TensorFlow.js?

TensorFlow.js adalah library untuk menjalankan **machine learning di browser** dan Node.js. Kamu bisa:
- Train model di browser
- Load model yang sudah di-train (Python)
- Jalankan inference tanpa server

## Install

```bash
# Browser
npm install @tensorflow/tfjs

# Atau via CDN
<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs"></script>
```

## Dasar Tensor

```javascript
// Buat tensor
const t = tf.tensor1d([1, 2, 3, 4, 5]);
console.log(t.shape);  // [5]
console.log(t.dtype);  // float32

// 2D tensor (matrix)
const m = tf.tensor2d([[1, 2], [3, 4]]);
console.log(m.shape);  // [2, 2]

// Operasi
const a = tf.tensor1d([1, 2, 3]);
const b = tf.tensor1d([4, 5, 6]);

const c = a.add(b);      // [5, 7, 9]
const d = a.mul(b);      // [4, 10, 18]
const e = a.mean();      // 2.0

// Cleanup memory
a.dispose();
b.dispose();
c.dispose();

// Atau gunakan tf.tidy()
const result = tf.tidy(() => {
    const a = tf.tensor1d([1, 2, 3]);
    const b = tf.tensor1d([4, 5, 6]);
    return a.add(b);
});  // Auto cleanup
```

## Simple Model

```javascript
// Buat model linear
const model = tf.sequential();
model.add(tf.layers.dense({units: 1, inputShape: [1]}));

// Compile
model.compile({
    optimizer: 'sgd',
    loss: 'meanSquaredError'
});

// Data training
const xs = tf.tensor1d([1, 2, 3, 4, 5]);
const ys = tf.tensor1d([2, 4, 6, 8, 10]);

// Train
async function train() {
    await model.fit(xs, ys, {
        epochs: 100,
        callbacks: {
            onEpochEnd: (epoch, logs) => {
                console.log(`Epoch ${epoch}: loss = ${logs.loss.toFixed(4)}`);
            }
        }
    });

    // Predict
    const result = model.predict(tf.tensor1d([6]));
    console.log('Prediction:', await result.data());
}

train();
```

## Image Classification

```javascript
async function classifyImage() {
    // Load pretrained model
    const model = await tf.loadLayersModel('path/to/model.json');

    // Load and preprocess image
    const img = document.getElementById('image');
    const tensor = tf.browser.fromPixels(img)
        .resizeBilinear([224, 224])
        .div(255.0)
        .expandDims();

    // Predict
    const predictions = await model.predict(tensor).data();

    // Get top 3 predictions
    const classes = ['Cat', 'Dog', 'Bird'];
    const top3 = Array.from(predictions)
        .map((p, i) => ({class: classes[i], probability: p}))
        .sort((a, b) => b.probability - a.probability)
        .slice(0, 3);

    console.log('Top 3 predictions:', top3);
}
```

## Transfer Learning

```javascript
async function transferLearning() {
    // Load MobileNet as base
    const mobilenet = await tf.loadLayersModel(
        'https://storage.googleapis.com/tfjs-models/tfjs/mobilenet_v1_0.25_224/model.json'
    );

    // Freeze base layers
    mobilenet.layers.forEach(layer => {
        layer.trainable = false;
    });

    // Add custom layers
    const model = tf.sequential();
    model.add(mobilenet);
    model.add(tf.layers.dense({units: 10, activation: 'softmax'}));

    // Compile and train
    model.compile({
        optimizer: 'adam',
        loss: 'categoricalCrossentropy',
        metrics: ['accuracy']
    });

    return model;
}
```

## Browser Integration

```html
<!DOCTYPE html>
<html>
<head>
    <title>ML in Browser</title>
    <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs"></script>
</head>
<body>
    <input type="file" id="fileInput" accept="image/*">
    <img id="preview" width="224" height="224">
    <p id="result"></p>

    <script>
        document.getElementById('fileInput').addEventListener('change', async (e) => {
            const file = e.target.files[0];
            const img = document.getElementById('preview');
            img.src = URL.createObjectURL(file);

            img.onload = async () => {
                const model = await tf.loadLayersModel('/model.json');
                const tensor = tf.browser.fromPixels(img)
                    .resizeBilinear([224, 224])
                    .div(255.0)
                    .expandDims();

                const prediction = await model.predict(tensor).data();
                document.getElementById('result').textContent =
                    `Prediction: ${(prediction[0] * 100).toFixed(2)}%`;
            };
        });
    </script>
</body>
</html>
```

## Latihan

1. Build digit recognizer (MNIST) yang jalan di browser
2. Buat real-time object detection dengan webcam
3. Train model custom untuk klasifikasi gambar
4. Implement style transfer di browser

## Sumber Belajar

- [TensorFlow.js Official](https://www.tensorflow.org/js)
- [TensorFlow.js Tutorials](https://www.tensorflow.org/js/tutorials)
"""
    },

    # ==================== COMPUTER VISION ====================
    {
        "category": "Computer Vision",
        "title": "OpenCV: Image Processing dengan Python",
        "python_version": "3.8+",
        "difficulty": "Beginner",
        "content": """
## Apa itu OpenCV?

OpenCV (Open Source Computer Vision Library) adalah library untuk **computer vision** dan **image processing**. Digunakan untuk:
- Image manipulation
- Object detection
- Face recognition
- Video analysis

## Install

```bash
pip install opencv-python
```

## Basic Operations

```python
import cv2
import numpy as np

# Read image
img = cv2.imread('photo.jpg')
print(img.shape)  # (height, width, channels)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Resize
resized = cv2.resize(img, (224, 224))
resized = cv2.resize(img, None, fx=0.5, fy=0.5)  # 50% size

# Save
cv2.imwrite('output.jpg', resized)
```

## Color Spaces

```python
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('photo.jpg')

# BGR to RGB (matplotlib uses RGB)
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# BGR to HSV (useful for color detection)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# BGR to Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Display
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(rgb)
axes[0].set_title('RGB')
axes[1].imshow(hsv)
axes[1].set_title('HSV')
axes[2].imshow(gray, cmap='gray')
axes[2].set_title('Grayscale')
plt.savefig('color_spaces.png')
```

## Image Enhancement

```python
import cv2

img = cv2.imread('photo.jpg')

# Brightness and Contrast
alpha = 1.5  # Contrast (1.0 = original)
beta = 30    # Brightness (0 = original)
enhanced = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

# Blur (Gaussian)
blurred = cv2.GaussianBlur(img, (5, 5), 0)

# Sharpen
kernel = np.array([[-1, -1, -1],
                   [-1,  9, -1],
                   [-1, -1, -1]])
sharpened = cv2.filter2D(img, -1, kernel)

# Edge detection
edges = cv2.Canny(gray, 50, 150)
```

## Drawing on Images

```python
import cv2
import numpy as np

img = np.zeros((500, 500, 3), dtype=np.uint8)

# Line
cv2.line(img, (50, 50), (450, 450), (0, 255, 0), 3)

# Rectangle
cv2.rectangle(img, (100, 100), (300, 300), (255, 0, 0), 2)

# Circle
cv2.circle(img, (250, 250), 80, (0, 0, 255), -1)  # -1 = filled

# Text
cv2.putText(img, 'OpenCV', (150, 280),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

cv2.imwrite('drawing.png', img)
```

## Object Detection (Color-based)

```python
import cv2
import numpy as np

def detect_color(image_path, lower_hsv, upper_hsv):
    img = cv2.imread(image_path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Create mask
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)

    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE,
                                    cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) > 500:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    return img

# Detect red objects
lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])
result = detect_color('image.jpg', lower_red, upper_red)
```

## Face Detection

```python
import cv2

# Load cascade classifier
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

img = cv2.imread('photo.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imwrite('faces_detected.jpg', img)
print(f'Found {len(faces)} faces')
```

## Webcam Capture

```python
import cv2

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Display
    cv2.imshow('Webcam', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

## Latihan

1. Deteksi wajah di video real-time
2. Hitung objek berwarna tertentu
3. Buat aplikasi filter Instagram sederhana
4. Implement edge detection pada video stream

## Sumber Belajar

- [OpenCV Official](https://docs.opencv.org/)
- [OpenCV Python Tutorial](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)
"""
    },
]

def generate_tutorial(day_num):
    """Generate tutorial based on day number"""
    idx = day_num % len(TUTORIALS)
    return TUTORIALS[idx]

def main():
    now = datetime.now(WIB)
    today = now.strftime("%Y-%m-%d")
    day_num = now.timetuple().tm_yday

    tutorial = generate_tutorial(day_num)

    # Create output directory
    os.makedirs("snippets", exist_ok=True)

    # Generate markdown
    filename = f"snippets/{today}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# {tutorial['title']}\n\n")
        f.write(f"**Kategori:** {tutorial['category']} | ")
        f.write(f"**Difficulty:** {tutorial['difficulty']} | ")
        f.write(f"**Date:** {today}\n\n")
        f.write("---\n\n")
        f.write(tutorial['content'])

    print(f"Generated: {filename}")

if __name__ == "__main__":
    main()
