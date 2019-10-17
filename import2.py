import gerbanglogika

def main():
	
	print("Gerbang AND")
	a = int(input("Masukkan Nilai a: "))
	b = int(input("Masukkan Nilai b: "))
	
	hasil = gerbanglogika.gerbangAnd (a, b)
	print("hasil dari gerbang logika a AND b: ", hasil)
	
	print("\nGerbang OR")
	c = int(input("Masukkan Nilai c: "))
	d = int(input("Masukkan Nilai d: "))
	
	hasil1 = gerbanglogika.gerbangOr (c, d)
	print("hasil dari gerbang logika c OR d: ", hasil1)
	
	print("\nGerbang XOR")
	e = int(input("Masukkan Nilai a: "))
	f = int(input("Masukkan Nilai b: "))
	
	hasil2 = gerbanglogika.gerbangXor(e, f)
	print("hasil dari gerbang logika e XOR f: ", hasil2)


	
if __name__ == "__main__":
	main()
	

