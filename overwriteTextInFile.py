# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 10:47:33 2018

@author: tfishbeck
"""

import os

with open('c:\\users\\tfishbeck\\documents\\QuerySourcePractice\\AccountProfitSources.txt') as file:
    data = file.readlines()

print('The current root drive is: ' + data[0][0])     

print(data)

#This is the new target drive
newSourceDrive = input('What is the new drive: ')

x = 0
newList = []

#This assigns the target drive into the list variable
for i in data:
    newList.append(newSourceDrive + data[x][1:])
    x += 1



with open('c:\\users\\tfishbeck\\documents\\QuerySourcePractice\\AccountProfitSources.txt', 'w') as file:
    file.writelines(newList)

