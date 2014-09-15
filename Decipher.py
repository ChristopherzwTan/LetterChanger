#! /usr/bin/python

from sys import argv

script, filename = argv

cipherText = open(filename, 'r')
decipher = open("decipher.txt", 'w')

for line in cipherText:
   for letter in line:
      if letter == "A":
         decipher.write("X")
      elif letter == "B":
         decipher.write("W")
      elif letter == "C":
         decipher.write("T")
      elif letter == "D":
         decipher.write("C")
      elif letter == "E":
         decipher.write("Q")
      elif letter == "F":
         decipher.write("O")
      elif letter == "G":
         decipher.write("P")
      elif letter == "H":
         decipher.write("N")
      elif letter == "I":
         decipher.write("F")
      elif letter == "J":
         decipher.write("V")
      elif letter == "K":
         decipher.write("J")
      elif letter == "L":
         decipher.write("G")
      elif letter == "M":
         decipher.write("B")
      elif letter == "N":
         decipher.write("M")
      elif letter == "O":
         decipher.write("S")
      elif letter == "P":
         decipher.write("A")
      elif letter == "Q":
         decipher.write("U")
      elif letter == "R":
         decipher.write("Y")
      elif letter == "X":
         decipher.write("H")
      elif letter == "T":
         decipher.write("D")
      elif letter == "U":
         decipher.write("I")
      elif letter == "V":
         decipher.write("E")
      elif letter == "W":
         decipher.write("L")
      elif letter == "X":
         decipher.write("K")
      elif letter == "Y":
         decipher.write("Z")
      elif letter == "Z":
         decipher.write("R")
      elif letter == " ":
         decipher.write( ")
decipher.write("\n")






