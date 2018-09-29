# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 09:59:40 2018

@author: tfishbeck
"""
#This opens a file, reads it line by line, and counts the number of categories that appear and updates the dictionary


counterDict = {}

with open('C:\\Users\\tfishbeck\\Documents\\GitHub\\python\\Practice Problems from PracticePython.org\\21sample.txt','r') as f:
    line = f.readline()
    while line:
        line = line[3:-26]
        if line in counterDict:
            counterDict[line] +=1
        else:
            counterDict[line] = 1
        line = f.readline()
        
print(counterDict)

print(line)

    