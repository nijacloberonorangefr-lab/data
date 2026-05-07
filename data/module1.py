# Créé par sknx, le 16/04/2026 en Python 3.7
import csv

pays = []

with open('C:/Users/sknx/OneDrive/Bureau/esteban leberon travail snt/data/countries.csv', newline='') as csvfile:
    pays_csv = csv.reader(csvfile, delimiter=';')
    for row in pays_csv:
        pays.append(row)
print(pays[0])
print(pays[1])
import csv
pays = []

with open('C:/Users/sknx/OneDrive/Bureau/esteban leberon travail snt/data/countries.csv', newline='') as csvfile: 
    pays_csv = csv.DictReader(csvfile, delimiter=';')
    for row in pays_csv:
        pays.append(dict(row))
print(pays[0])
print(pays[1])
print([p['name'] for p in pays if p['currency_code'] == 'EUR'])
print([p['currency_code'] for p in pays if p['currency_name'] == 'Dollar'])
def clé_superficie(p):
    return float(p['area'])
pays.sort(key=clé_superficie, reverse=True)
print([(p['name'], p['area']) for p in sorted(pays, key=clé_superficie, reverse=True)[:5]])