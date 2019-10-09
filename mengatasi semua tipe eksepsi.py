def main ():
	# membuat judul program
	print ("PROGRAM PEMBAGIAN BILANGAN")
	
	#mendefinisikan blok try...except
	try:
		#meminta user memasukkan bilangan
		a = float (input("Masukkan a: "))
		b = float (input("Masukkan b: "))
	
		#melakukan pembagian
		hasil = a / b
		
	# mengantisipasi pembgian dengan 0
	except (ZeroDivisionError, ValueError, KeyboardInterrupt):
		print ("\nERROR: Anda telah melakukan " + "kesalahan")

	else:
		print("\na : ", a)
		print ("b : ", b)
		print ("a / b = ", hasil)
	
if __name__ == "__main__":
	main () 



