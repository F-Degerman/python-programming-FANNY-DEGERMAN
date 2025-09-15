import csv
import math

with open('datapoints.csv', mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row
    data = [float(row[0]) for row in reader]
    print(data)
