# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 10:18:35 2018

@author: tfishbeck
"""
import pandas as pd

studentGrade = []
studentDict = {}

print(len(' '))
def get_student_list(studGrade,studDict):
    studList = []
    x = input('What is the student name? Leave blank and press enter if no more. ')
    while len(x) > 1: 
            studList.append(x)
            x = input('What is the student name? Leave blank and press enter if no more. ')
    for i in range(len(studList)):
        score = int(input('What did ' + studList[i] + ' score on the test: '))
        studGrade.append(score)
    studDict = {'Students':studList,'Grades':studGrade}
    return studDict
    

raw_data = get_student_list(studentGrade,studentDict)

print(raw_data)



