from abc import ABCMeta, abstractmethod
import math


class Bangun3D(metaclass=ABCMeta):
   
   @abstractmethod
   def cetakData(self):
      pass
   @abstractmethod
   def hitungVolume(self):
      pass
   @abstractmethod
   def cetakVolume(self):
      pass


class Kotak(Bangun3D):
   def __init__(self, p, l=None, t=None):
      if l == None and t == None:
         
         self.panjang = self.lebar = \
         self.tinggi = p
      else:
         
         self.panjang = p
         self.lebar = l
         self.tinggi = t
   
   def cetakData(self):
      print("panjang\t: ", self.panjang)
      print("lebar\t: ", self.lebar)
      print("tinggi\t: ", self.tinggi)

   
   def hitungVolume(self):
      return self.panjang * self.lebar * \
             self.tinggi

   
   def cetakVolume(self):
      print("Volume Kotak \t= ",
            self.hitungVolume())

class Tabung(Bangun3D):
   def __init__(self, r, t):
      self.jarijari = r
      self.tinggi = t

   
   def cetakData(self):
      print("jari-jari alas \t: ",
            self.jarijari)
      print("tinggi tabung \t: ", self.tinggi)

   
   def hitungVolume(self):
      return math.pi * pow(self.jarijari, 2) * \
             self.tinggi

   
   def cetakVolume(self):
      print("Volume Tabung \t= ",
            self.hitungVolume())

def main():
   obj1 = Kotak(6, 5, 4)  
   print("BALOK")
   obj1.cetakData()
   obj1.cetakVolume()

   obj2 = Kotak(5)  
   print("\nKUBUS")
   obj2.cetakData()
   obj2.cetakVolume()

   obj3 = Tabung(3, 4)  
   print("\nTABUNG")
   obj3.cetakData()
   obj3.cetakVolume()

if __name__ == "__main__":
   main()
