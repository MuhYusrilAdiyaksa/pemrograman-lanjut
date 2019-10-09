def main ():
	print ("PROGRAM PEMBAGIAN BILANGAN")
	
	#meminta user memasukkan bilangan
	a = float (input("Masukkan a: "))
	b = float (input("Masukkan b: "))
	
	#mendefinisikan blok try...except
	try:
		hasil =a / b
	except ZeroDivisionError:
		print ("\nERROR: Nilai b tidak boleh nol")

	# menampilkan hasil
	print("\na : ", a)
	print ("b : ", b)
	
	#kode di bawah ini akan menimbulkan kesalahan 
	#dengan tipe NameError
	print ("a / b = ", hasil)
	
if __name__ == "__main__":
	main () 

