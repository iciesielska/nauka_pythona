hodowla = [
	{
		'rasa': 'brytyjski',
		'ilosc': 2,
		'cena': 2500,
		'kolor': 'niebieski',
		'samiec': 2,
		'samica': 0,
		'data_urodzenia': '10.11.2020'
	},
	{
		'rasa': 'ragdoll',
		'ilosc': 4,
		'cena': 3500,
		'kolor': 'szylkret',
		'samiec': 0,
		'samica': 4,
		'data_urodzenia': '20.10.2020'
	}, 
	{
		'rasa': 'maine coon',
		'ilosc': 8,
		'cena': 2700,
		'kolor': 'rudy',
		'samiec': 4,
		'samica': 4,
		'data_urodzenia': '17.09.2020'
	}
]

def pokaz_dane_kota(rasa):
	rasa_kota = rasa['rasa']
	ilosc = rasa['ilosc']
	cena = rasa['cena']
	kolor = rasa['kolor']
	samce = rasa['samiec']
	samice = rasa['samica']
	data_urodzenia = rasa['data_urodzenia']

	print("RASA:{0}, ILOŚĆ:{1}, CENA:{2}, KOLOR:{3}, SAMCE:{4}, SAMICE:{5}, DATA URODZENIA:{6}".format(rasa_kota, ilosc, cena, kolor, samce, samice, data_urodzenia))

for rasa in hodowla:
	pokaz_dane_kota(rasa)


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
