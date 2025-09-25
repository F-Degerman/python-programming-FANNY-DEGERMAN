import numpy as np
import matplotlib.pyplot as plt

# kopplar filen till variabeln path
path = "datapoints.txt"

# Funktion för att bearbeta datan och returnera både arrayen och kolumnerna
def fix_data(path):
    fix_data_list = []
    with open(path, 'r') as f:
        next(f)  # hoppa över första raden (rubriker)
        for line in f:
            # Tar bort onödiga radbrytningar och mellanslag, delar upp raderna utifrån kommatecken.
            width, hight, label = line.strip().split(",")
            # konverterar strängarna till flyttal och heltal. 
            fix_data_list.append((float(width), float(hight), int(label)))

    # >>> Den här delen låg tidigare utanför – nu flyttad in i funktionen
    data  = np.array(fix_data_list)
    width = data[:, 0]
    hight = data[:, 1]
    label = data[:, 2].astype(int)   # gör labels till int för säkra jämförelser
    # <<<

    return data, width, hight, label

# Använd funktionen (resten av din kod kan fortsätta som tidigare)
data, width, hight, label = fix_data(path)

# Exempel: om du senare gör masker och plot
pichu   = (label == 0)
pikachu = (label == 1)

plt.scatter(width[pichu],   hight[pichu],   marker="o", color="#EADB6A", label="Pichu")
plt.scatter(width[pikachu], hight[pikachu], marker="x", color="#E9C400", label="Pikachu")
plt.xlabel("Width")
plt.ylabel("Hight")
plt.title("Datapoints (based on individual height and length of Pichu and Pikachu)")
plt.legend()
plt.show()
