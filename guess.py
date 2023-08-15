import random

class Guess:
  def __init__(self):
    self.tebakan = ""
    self.jawaban = random.randint(1, 10)
    self.batas = 3

  def inputData(self):
    self.tebakan = int(input('tebak 1 s.d 10: '))
    return

  def cek(self):
    self.batas = self.batas - 1
    while True:
      if self.batas > 0:
        if self.tebakan == self.jawaban:
          print("jawaban benar!")
          break
        else:
          if self.tebakan > self.jawaban:
            self.batas = self.batas - 1
            print("tebakan kamu terlalu besar!")
            self.tebakan = int(input('coba tebak lagi: '))
          else:
            self.batas = self.batas - 1
            print("tebakan kamu terlalu kecil!")
            self.tebakan = int(input('coba tebak lagi: '))
      else:
        print("batas menjawab sudah habis!")
        break
    return