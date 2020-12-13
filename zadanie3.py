hodowla = [
    {
    	'zwierze': 'kot brytyjski',
    	'ilosc': 2,
    	'cena': 2500,
    	'kolor': 'niebieski',
    	'samiec': 2,
    	'samica': 0,
    	'data_urodzenia': '10.11.2020'
    },
    {
    	'zwierze': 'ragdoll',
    	'ilosc': 4,
    	'cena': 3500,
    	'kolor': 'szylkret',
    	'samiec': 0,
    	'samica': 4,
    	'data_urodzenia': '20.10.2020'
    }, 
    {
    	'zwierze': 'maine coon',
    	'ilosc': 8,
    	'cena': 2700,
    	'kolor': 'rudy',
    	'samiec': 4,
    	'samica': 4,
    	'data_urodzenia': '17.09.2020'
    }
]

suma = 0
ilosc_kotow = 0
ilosc_samcow = 0
ilosc_samic = 0

for rasa in hodowla:
    cena = rasa['cena']
    ilosc = rasa['ilosc']
    samce = rasa['samiec']
    samice = rasa['samica']

    suma = suma + (cena * ilosc)
    ilosc_kotow = ilosc_kotow + ilosc
    ilosc_samcow = ilosc_samcow + samce
    ilosc_samic = ilosc_samic + samice

print("suma:{0}".format(suma))
print("ilosc_kotow:{0}".format(ilosc_kotow))
print("ilosc_samcow:{0}".format(ilosc_samcow))
print("ilosc_samic:{0}".format(ilosc_samic))
