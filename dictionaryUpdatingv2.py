# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 10:18:35 2018

@author: tfishbeck
"""
import pandas as pd



#This functions returns a dictionary of names and grades for the class
def get_student_dictionary():
    studList = []
    studGrade = []
    studentDict = {}
    x = input('What is the student name? Leave blank and press enter if no more. ')
    while len(x) > 1: 
            studList.append(x)
            x = input('What is the student name? Leave blank and press enter if no more. ')
    for i in range(len(studList)):
        score = int(input('What did ' + studList[i] + ' score on the test: '))
        studGrade.append(score)
    studentDict = {'Students':studList,'Grades':studGrade}
    return studentDict


raw_data = get_student_dictionary()

df = pd.DataFrame(raw_data,columns = ['Students','Grades'])

print(df)






