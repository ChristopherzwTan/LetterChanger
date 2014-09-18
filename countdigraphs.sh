#! /bin/bash

for fl in {A..Z}
do
   for sl in {A..Z}
   do
      #full=$fl$sl
      printf "$fl$sl "
      grep "$fl$sl" -o -w spacedcipher2.txt | wc -l
   done
done

