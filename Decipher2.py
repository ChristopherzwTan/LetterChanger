#! /usr/bin/python

from sys import argv

script, filename = argv

cipherText = open(filename, 'r')
decipher = open("2decipher.txt", 'w')

for line in cipherText:
   for letter in line:
      if letter == "A":
         decipher.write("K")
      elif letter == "B":
         decipher.write("G")
      elif letter == "C":
         decipher.write("O")
      elif letter == "D":
         decipher.write("D")
      elif letter == "E":
         decipher.write(" ")
      elif letter == "F":
         decipher.write("I")
      elif letter == "G":
         decipher.write("W")
      elif letter == "H":
         decipher.write("T")
      elif letter == "I":
         decipher.write("F")
      elif letter == "J":
         decipher.write("Y")
      elif letter == "K":
         decipher.write("X")
      elif letter == "L":
         decipher.write("V")
      elif letter == "M":
         decipher.write("Z")
      elif letter == "N":
         decipher.write("P")
      elif letter == "O":
         decipher.write("R")
      elif letter == "P":
         decipher.write("N")
      elif letter == "Q":
         decipher.write("U")
      elif letter == "R":
         decipher.write("L")
      elif letter == "S":
         decipher.write("A")
      elif letter == "T":
         decipher.write("C")
      elif letter == "U":
         decipher.write("S")
      elif letter == "V":
         decipher.write("E")
      elif letter == "W":
         decipher.write("M")
      elif letter == "X":
         decipher.write("B")
      elif letter == "Y":
         decipher.write(" ")
      elif letter == "Z":
         decipher.write("H")
      elif letter == " ":
         decipher.write(" ")
decipher.write("\n")






