import math
TP = 2
FP = 2
FN = 11
TN = 985
accuracy = (TP + TN) / (TP + TN + FN + FP)
print(f"accuracy {accuracy*100:.1f}%")