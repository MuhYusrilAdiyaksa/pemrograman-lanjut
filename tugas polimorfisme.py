class BilanganBulat(object):
   def __init__(self, nilai):
      if not isinstance(nilai, int):
         raise TypeError("Nilai harus bertipe bilangan bulat")
      self.nilai = nilai

   
   def __pow__(self, objek):
      if isinstance(objek, int):
         return self.nilai ** objek
      elif isinstance(objek, float):
         return float(self.nilai ** objek)
      elif isinstance(objek, BilanganBulat):
         return self.nilai ** objek.nilai
      else:
         raise TypeError("Objek harus bertipe numerik")
    
	
   def __mod__(self, objek):
      if isinstance(objek, int):
         return self.nilai % objek
      elif isinstance(objek, float):
         return float(self.nilai) % objek
      elif isinstance(objek, BilanganBulat):
         return self.nilai % objek.nilai
      else:
         raise TypeError("Objek harus bertipe numerik")


def main():
   a = BilanganBulat(12)
   b = BilanganBulat(5)
   c = 15
   d = 1.5

   print("DATA:")
   print("a = 12 \nb = 5" "\nc =", c, "\nd =", d)
   print("\nmenampilkan hasil dari operator pow(pangkat)")
   print("a pangkat b: ", a ** b)
   print("b pangkat b: ", b ** b)
   print("b pangkat d: ", b ** d)

   
   print("\nmenampilkan hasil dari operator mod(modulus)")
   print("a mod b: ", a % b)
   print("a mod c: ", a % c)
   print("b mod d: ", b % d)
   
   
if __name__ == "__main__":
   main()
