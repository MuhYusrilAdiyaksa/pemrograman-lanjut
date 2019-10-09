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
	except ZeroDivisionError:
		print ("\nERROR: Nilai b tidak boleh nol")
	
	# mengantisipasi variabel a atu b belum diisi
	except ValueError:
		print("\nERROR: a dan b harus berupa angka")
		
	# mengantisipsi variabel a atau b belum diisi
	except KeyboardInterrupt:
		print ("\nERROR: Jangan tekan Ctrl+C!")
		
	else:
		print("\na : ", a)
		print ("b : ", b)
		print ("a / b = ", hasil)
	
if __name__ == "__main__":
	main () 


