# Créé par sknx, le 16/04/2026 en Python 3.7
import csv

pays = []

with open('C:/Users/sknx/OneDrive/Bureau/data/csv/usd.csv', newline='') as csvfile: 
    usd_csv = csv.reader(csvfile, delimiter=',')
    for row in usd_csv:
        pays.append(row)
print(pays[0])
print(pays[1])
import csv
pays = []

with open('C:/Users/sknx/OneDrive/Bureau/data/csv/usd.csv', newline='') as csvfile:
    usd_csv_csv = csv.DictReader(csvfile, delimiter=',')
    for row in usd_csv_csv:
        pays.append(dict(row))
print(pays[0])
print(pays[1])
def clé_superficie(p):
    return float(p['High (kg)'])
pays.sort(key=clé_superficie, reverse=True)
print([(p['Date'], p['High (kg)'],p['Close (kg)']) for p in sorted(pays, key=clé_superficie, reverse=True)[:5]])

def clé_superficie(p):
    return float(p['Low (kg)'])
pays.sort(key=clé_superficie, reverse=True)
print([(p['Date'], p['Low (kg)'],p['Close (kg)']) for p in sorted(pays, key=clé_superficie, reverse=True)[:5]])
