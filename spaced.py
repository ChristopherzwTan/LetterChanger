#! /usr/bin/python

from sys import argv

script, filename = argv

cipherText = open(filename, 'r')
decipher = open("spacedcipher2.txt", 'w')

count = 0
for line in cipherText:
   for letter in line:
      count = count + 1
      decipher.write(letter)
      if ((count % 2) == 0):
         decipher.write(" ")

decipher.write("\n")






