
class Induk1(object):
   def __init__(self, a):
      self.a = a
   def cetakA(self):
      print("Nilai a = ", self.a)


class Induk2(object):
   def __init__(self, b):
      self.b = b
   def cetakB(self):
      print("Nilai b = ", self.b)


class Anak(Induk1, Induk2):
   def __init__(self, a, b, c):
      
      Induk1.__init__(self, a)
     
      Induk2.__init__(self, b)
      self.c = c
   def cetakC(self):
      print("Nilai c = ", self.c)

def main():
   
   obj = Anak(111, 222, 333)

   
   obj.cetakA()

   
   obj.cetakB()

   
   obj.cetakC()

if __name__ == "__main__":
   main()
