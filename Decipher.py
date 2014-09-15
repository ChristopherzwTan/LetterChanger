#! /usr/bin/python

from sys import argv

script, filename = argv

cipherText = open(filename, 'r')
decipher = open("decipher.txt", 'w')

for line in cipherText:
   for letter in line:
      if letter == "A":
         print("X")
         decipher.write("X")
      elif letter == "B":
         print("W")
         decipher.write("W")
      elif letter == "C":
         print("T")
         decipher.write("T")
      elif letter == "D":
         print("C")
         decipher.write("C")
      elif letter == "E":
         print("Q")
         decipher.write("Q")
      elif letter == "F":
         print("O")
         decipher.write("O")
      elif letter == "G":
         print("P")
         decipher.write("P")
      elif letter == "H":
         print("N")
         decipher.write("N")
      elif letter == "I":
         print("F")
         decipher.write("F")
      elif letter == "J":
         print("V")
         decipher.write("V")
      elif letter == "K":
         print("J")
         decipher.write("J")
      elif letter == "L":
         print("G")
         decipher.write("G")
      elif letter == "M":
         print("B")
         decipher.write("B")
      elif letter == "N":
         print("M")
         decipher.write("M")
      elif letter == "O":
         print("S")
         decipher.write("S")
      elif letter == "P":
         print("A")
         decipher.write("A")
      elif letter == "Q":
         print("U")
         decipher.write("U")
      elif letter == "R":
         print("Y")
         decipher.write("Y")
      elif letter == "X":
         print("H")
         decipher.write("H")
      elif letter == "T":
         print("D")
         decipher.write("D")
      elif letter == "U":
         print("I")
         decipher.write("I")
      elif letter == "V":
         print("E")
         decipher.write("E")
      elif letter == "W":
         print("L")
         decipher.write("L")
      elif letter == "X":
         print("K")
         decipher.write("K")
      elif letter == "Y":
         print("Z")
         decipher.write("Z")
      elif letter == "Z":
         print("R")
         decipher.write("R")







