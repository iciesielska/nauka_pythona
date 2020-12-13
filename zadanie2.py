####ZADANIE 2

def calucate_vat(netto):
	return netto * 1.23

if __name__ == "__main__":
	vat = calucate_vat(1000)
	print("{0}".format(vat))
