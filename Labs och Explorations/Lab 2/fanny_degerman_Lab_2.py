
import numpy as np
import matplotlib.pyplot as plt

train_path = "datapoints.txt"
test_path = "testpoints.txt"

# ==============================
# GRUNDUPPGIFT – 1-NN för alla testpunkter
# ==============================

# bearbetar datapoints - returnerar array
def process_data(train_path):
    rows = []
    with open(train_path, "r") as f:
        next(f)  # hoppa rubrik
        for line in f:
            w, h, l = line.strip().split(",")
            rows.append((float(w), float(h), int(l)))
    return np.array(rows)  

train_array = process_data(train_path)          
width = train_array[:, 0]                       
height = train_array[:, 1]                      
label = train_array[:, 2].astype(int)           
train_x = train_array[:, 0:2]                   

# bearbetar testdata - returnerar array
def process_test_data(test_path):
    rows = []
    with open(test_path, "r") as f:
        next(f)  # hoppa "Test points:"
        for line in f:
            line = line.strip()
            if not line:
                continue
            left, right = line.split(".", 1)
            test_id = int(left.strip())
            start = right.find("(")
            end   = right.find(")", start + 1)
            inner = right[start+1:end]
            w_str, h_str = [part.strip() for part in inner.split(",")]
            w = float(w_str.replace(",", "."))
            h = float(h_str.replace(",", "."))
            rows.append((test_id, w, h))
    return np.array(rows, dtype=float)          

test_array   = process_test_data(test_path)     
test_id    = test_array[:, 0].astype(int)       
test_width = test_array[:, 1]                   
test_height = test_array[:, 2]                  
test_x     = test_array[:, 1:3]                 

# plottar graf
plt.scatter(width[label == 0], height[label == 0], marker="o", color="#EADB6A", label="Pichu")
plt.scatter(width[label == 1], height[label == 1], marker="x", color="#E9C400", label="Pikachu")
plt.xlabel("Width")
plt.ylabel("Height")
plt.title("Datapoints (based on individual height and length of Pichu and Pikachu)")
plt.legend()
plt.show()

#  euclidean distance (återanvänds i koden)
def euclidean_distance(A, B):
    diff = A[:, None, :] - B[None, :, :]       
    return np.sqrt(np.sum(diff**2, axis=2))    

# NN 
dist   = euclidean_distance(test_x, train_x)   
nn_idx  = np.argmin(dist, axis=1)              
nn_lab  = label[nn_idx]                        
pred_label_nn1  = np.where(nn_lab == 0, "Pichu", "Pikachu")  

# output "Grunduppgift"
print("\n==============================\nGrunduppgift\n==============================")
for label_te, (tx, ty), label_tr in zip(test_id, test_x, pred_label_nn1):
    print(f"{label_te}. ({tx:g}, {ty:g}) är en {label_tr}.")

# ==============================
# UPPGIFT 2 (kommer innan uppgift 1 pga snyggare output) – 10-NN (majoritetsröstning + tie-break = 1-NN)
# ==============================

# NN utifrån de 10 närmsta punkterna ("röstning")
k = 10
order    = np.argsort(dist, axis=1)[:, :k]     
k_labels = label[order]                        
votes_1   = np.sum(k_labels == 1, axis=1)      
votes_0   = np.sum(k_labels == 0, axis=1)      
pred_label_nn10 = np.where(votes_1 > votes_0, 1, 0)  

# Tie-break: om lika många röster = använd 1-NN-resultatet (nn_lab)
tie = (votes_1 == votes_0)                     
pred_label_nn10[tie] = nn_lab[tie]
pred_label_nn1 = np.where(pred_label_nn10 == 0, "Pichu", "Pikachu")  

# output "uppgift 2"
print("\n==============================\nUppgift 2\n==============================")
print("Utifrån en majoritetsröstning av de närmsta punkterna är testpunkt:")
for label_te, label_tr in zip(test_id, pred_label_nn1):
    print(f"{label_te}. en {label_tr}.")

# ==============================
# UPPGIFT 1 – 1-NN på användarens punkt
# ==============================

# input från användare. felhantering om inte rätt värden.
def ask_user():
    print("\n==============================\nUppgift 1\n==============================")
    while True:
        line = input("Ange egen testpunkt (width,height), t.ex. 24.2,31.5: ").strip()
        line = line.replace(";", ",").replace(" ", ",")
        parts = [p for p in line.split(",") if p]
        if len(parts) != 2:
            print(" Ange exakt två tal separerade med komma. Ex: 24.2,31")
            continue
        try:
            w = float(parts[0].replace(",", "."))
            h = float(parts[1].replace(",", "."))
        except ValueError:
            print(" Ogiltigt tal. Försök igen.")
            continue
        if w < 0 or h < 0:
            print(" Endast icke-negativa tal. Försök igen.")
            continue
        return w, h  

# euclidean dictance mellan användarens input och träningsdatan
user_w, user_h = ask_user()                          
user_x = np.array([[user_w, user_h]], dtype=float)   
dist_user = euclidean_distance(user_x, train_x)[0]   
nn_user = int(np.argmin(dist_user))                  
pred_label_u = "Pichu" if label[nn_user] == 0 else "Pikachu"  

# output "uppgift 1"
print(f"Måtten ({user_w:g}, {user_h:g}) är troligvis en {pred_label_u}.")
