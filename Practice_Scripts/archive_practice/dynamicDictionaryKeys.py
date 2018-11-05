# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 12:51:20 2018

@author: tfishbeck
"""
#This program will create a dynamic number of dictionary keys and values for each key using nested lists
def get_columns():
    c1 = []
    x = input('Please enter column name. Press enter if finished: ')
    while len(x) > 1:
        c1.append(x)
        x = input('Please enter column name. Press enter if finished: ')
    return c1

col = get_columns()

listsNeeded = len(col)

valueCount = int(input('Please enter the number of values in the first column: '))    
        

colCount = 1
masterList = []
newList = []

while colCount <= listsNeeded:
    for i in range(valueCount):
        newList[i-1] = input('What is the value: ')
    masterList.append(newList)
    colCount+=1
    
print(masterList)
            
        





