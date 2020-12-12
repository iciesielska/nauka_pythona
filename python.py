####ZADANIE 0

#password = "pies"
#dlugoscSrodka = len(password) - 2
#srodek = '*' * dlugoscSrodka

#print(password[0] + srodek + password[-1])



####ZADANIE 1

#def print_dict(d):
 #   for key in samolot:
 #       print("{0}:{1}".format(key, d[key]))

#if __name__ == "__main__":
#    samolot = {'nazwa': 'boeing',
 #          'przebieg': 10000,
 #          'type': 'pasazerski'}
   
 #   print_dict(samolot)

####ZADANIE 2

#def calucate_vat(netto):
#    return 0

#if __name__ == "__main__":
#    vat = calucate_vat(1000)
#    print("{0}".format(vat))


####ZADANIE 3

def print_dict(d):
    for key in produkt:
        print("{0}:{1}".format(key, d[key]))
    print("suma:{0}".format(produkt["ilosc"] * produkt["cena"]))

if __name__ == "__main__":
    produkt = {'produkt': 'mleko',
           'ilosc': 1,
           'cena': 1.5}
    
    print_dict(produkt);

def print_dict(d):
    for key in produkt:
        print("{0}:{1}".format(key, d[key]))
    print("suma:{0}".format(produkt["ilosc"] * produkt["cena"]))

if __name__ == "__main__":
    produkt = {
    	'produkt': 'czekolada',
        'ilosc': 2,
        'cena': 3
    }
    
    print_dict(produkt)	





