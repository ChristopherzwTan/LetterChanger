#! /usr/bin/python


##############################################################################################
#
# Please only use for Cipher2.txt
#
#
# Christopher Tan
#
#
##############################################################################################

from sys import argv

script, filename = argv

cipherText = open(filename, 'r')
decipher = open("3decipher.txt", 'w')
bleh = open("derp.txt", 'w')
count = 0

for line in cipherText:
   s = list(line)
   for letter in line:
      digraph = ""
      if (count%2 != 0):
         bleh.write(s[count-1]+s[count] + "\n")
         digraph = s[count-1]+s[count]
         if (digraph == "OT"):
            #s[count-1]="T"
            #s[count]="H"
            digraph="TH"
         elif (digraph == "YO"):
            digraph="OT"
         elif (digraph == "CZ"):
            digraph="EI"
         elif (digraph == "ZC"):
            digraph="IE"
         elif (digraph == "AR"):
            digraph="MA"
         elif (digraph == "UH"):
            digraph="MX"
         elif (digraph == "HZ"):
            digraph="CO"
         elif (digraph == "CT"):
            digraph="HE"
         elif (digraph == "EY"):
            digraph="IT"
#         elif (digraph == "CT"):
#            digraph="HE"
#         elif (digraph == "YO"):
#            digraph="OT"
#         elif (digraph == "YO"):
#            digraph="OT"
      decipher.write(digraph) 
      count=count+1
decipher.write("\n")






