import csv
import numpy as np


tupler = []
with open("datapoints.csv", newline="", encoding="utf-8") as fil:
    läsare = csv.reader(fil)
    next(läsare)
    for rad in läsare:
        width = float(rad[0])
        height = float(rad[1])
        typ = rad[2]
        tupler.append((width, height, typ))

print(tupler)

