import numpy as np
import matplotlib.pyplot as plt
import numpy as np

# kopplar filen till variabeln path
path = "datapoints.txt"
test_path = "testpoints.txt"

# =================================
# Bearbeta data (datapoints.txt) 
# =================================

# Funktion för att bearbeta datan och returnera både arrayen och kolumner
def fix_data(path):
    fix_data_list = []
    with open(path, 'r') as f:
        next(f)  # hoppa över första raden (rubriker)
        for line in f:
            # Tar bort onödiga radbrytningar och mellanslag, delar upp raderna utifrån kommatecken.
            parts = line.strip().split(",")          # delar raden i 3 delar
            w = float(parts[0])                      # width
            h = float(parts[1])                      # hight
            l = int(parts[2])                        # label (0/1)
            fix_data_list.append((w, h, l))

    data = np.array(fix_data_list)                   # shape: (N, 3)
    return data

# =================================
# Bearbeta testdata 
# =================================

def fix_test_data(test_path):
    fix_test_list = []
    with open(test_path, 'r') as ft:      # ft = test_data
        next(ft)                          # hoppa över första raden (rubriker)
        for line in ft:
            line = line.strip()
            if not line:
                continue
            left, right = line.split(".", 1)     # Dela upp utifrån "." först
            start = right.find("(")
            end   = right.find(")", start + 1)
            inner = right[start+1:end]           # "25, 32" / "24.2, 31.5"
            parts = [p.strip() for p in inner.split(",")]
            wt = float(parts[0].replace(",", "."))   # width
            ht = float(parts[1].replace(",", "."))   # hight
            fix_test_list.append((wt, ht))

    data = np.array(fix_test_list)   # (M, 2)
    return data
                         
# =================================
# Plotta graf utifrån datapoints (test_data)
# =================================

data = fix_data(path)
width = data[:, 0]
hight = data[:, 1]
label = data[:, 2].astype(int)

pichu   = (label == 0)
pikachu = (label == 1)

plt.scatter(width[pichu],   hight[pichu],   marker="o", color="#EADB6A", label="Pichu")
plt.scatter(width[pikachu], hight[pikachu], marker="x", color="#E9C400", label="Pikachu")
plt.xlabel("Width")
plt.ylabel("Hight")
plt.title("Datapoints (based on individual height and length of Pichu and Pikachu)")
plt.legend()
plt.show()

# =================================
# Uppgift 1: Låter användaren mata in testpunkt och låter algoritmen avgöra om Pichu eller Pikachu.
# =================================

def ask_user():
    while True:
        user_input = input("\nAnge testpunkt (width,height), t.ex. 24.2,31.5: ").strip()
        user_input = user_input.replace(";", ",").replace(" ", ",")
        parts = [p for p in user_input.split(",") if p]

        if len(parts) != 2:
            print(" Ange exakt två tal separerade med komma (eller heltal). Exempel: 24.2,31")
            continue

        try:
            w = float(parts[0].replace(",", "."))
            h = float(parts[1].replace(",", "."))
        except ValueError:
            print("Kunde inte tolka ett av värdena som tal. Försök igen (t.ex. 24.2,31.5).")
            continue

        if w < 0 or h < 0:
            print("Värden måste vara 0 eller större.")
            continue

        return w, h
