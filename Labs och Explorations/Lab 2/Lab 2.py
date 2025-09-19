import csv 

# funktion som läser CSV-filen och skriver ut första kolumnen av varje rad
def display_csv_content(): 
    # öppnar CSV-filen och namnger den f1
    with open("datapoints.csv") as f1: 
        # skapar en CSV-läsare
        reader = csv.reader(f1) 
        # itererar genom varje rad i vald kolumn (row[0]) i CSV-filen
        for row in reader: 
            print(row[0]) 

# kör funktionen när skriptet körs direkt
if __name__ == "__main__": 
    display_csv_content() 