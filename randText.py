# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 10:18:35 2018

@author: tfishbeck
"""
import pandas as pd, random as r

studentList = []
studentDict = {}

student = True

while student:
    x = input('What is the student name? Leave blank and press enter if no more. ')
    studentList.append(x)
    student = x


for i in range(len(studentList)-1):
    score = int(input('What did ' + studentList[i] + ' score on the test: '))
    update = {studentList[i]:score}
    studentDict.update(update)
    
print(studentDict)
    
    
    
    
    
    
    
    
