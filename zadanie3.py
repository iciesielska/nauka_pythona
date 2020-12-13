hodowla = [
    {'zwierze': 'kot brytyjski', 'ilosc': 2, 'cena': 2500, 'kolor': 'niebieski'},
    {'zwierze': 'ragdoll', 'ilosc': 4, 'cena': 3500, 'kolor': 'szylkret'},
    {'zwierze': 'maine coon', 'ilosc': 8, 'cena': 2700, 'kolor': 'rudy'}
]

suma = 0
ilosc_kotow = 0

for poz in hodowla:
    il = poz['ilosc']
    c = poz['cena']
    suma = suma + (c * il)
    ilosc_kotow = ilosc_kotow + il
    

print(suma)
print(ilosc_kotow)
