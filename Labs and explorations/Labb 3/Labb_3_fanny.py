import csv  
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression

path = "unlabelled_data.csv"

# ==================
# a) Läsa data
# ==================
def process_data(path):
    rows = []
    with open(path, "r") as f:
        for line in f:
            a, b = line.strip().split(",")
            rows.append((float(a), float(b)))
    return np.array(rows)  

# ==================
# c) Funktion för att klassificera punkt mot linje. Returnerar True om (x, y) ligger ovanför linjen y = kx + m
# ==================
def is_above_line(x, y, k, m):
    return y > k * x + m

# ==================
# d) Klassificera alla punkter
# ==================
data_array = process_data(path)
a = data_array[:, 0]
b = data_array[:, 1]

# Beräkna skiljelinje
# för att dela datan i två kluster 
# och gör så att samma startpunkt används varje gång (för att kunna återskapa resultatet)
kmeans = KMeans(n_clusters=2, random_state=0)
# Ger etikett 0 eller 1 utifrån vilket kluster datan tillhör
labels_kmeans = kmeans.fit_predict(data_array)

model = LogisticRegression()
model.fit(data_array, labels_kmeans)

# Hämtar modellens koefficienter (vikter) w och intercept (bias) b_
w = model.coef_[0] # "koefficienter (vikter)"
b_ = model.intercept_[0] # "intercept(bias)"

# formeln y = kx + m
k = -w[0] / w[1] # lutningen
m = -b_ / w[1]  # skärningspunkt på y-axeln

# skriver den beräknade linjen med fyra decimaler
print(f"Linjeekvation: y = {k:.4f}x + {m:.4f}")

# Klassificerar varje punkt
classified_labels = []  # 1 = ovanför, 0 = nedanför

for x, y in data_array:
    label = 1 if is_above_line(x, y, k, m) else 0
    classified_labels.append(label)

classified_labels = np.array(classified_labels)

# Plotta klassificerade punkter
plt.scatter(a, b, c=classified_labels, cmap='coolwarm', edgecolor='k', label='Data')

# Ritar skiljelinjen
x_vals = np.array([min(a), max(a)])
y_vals = k * x_vals + m
plt.plot(x_vals, y_vals, 'k--', label=f'y = {k:.2f}x + {m:.2f}')

plt.xlabel("a")
plt.ylabel("b")
plt.title("Klassificerade punkter utifrån linje")
plt.legend()
plt.show()

# Skriv ut antal punkter i varje klass 
print(f"Antal ovanför linjen: {np.sum(classified_labels == 1)}")
print(f"Antal under/på linjen: {np.sum(classified_labels == 0)}")

# Lägger klassificerade punkter i ny fil
output_path = "labelled_data.csv"

with open(output_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["a", "b", "label"])  # header
    for i in range(len(data_array)):
        x = data_array[i, 0]
        y = data_array[i, 1]
        label = classified_labels[i]
        writer.writerow([x, y, label])

print(f"Klassificerad data sparad i {output_path}")
