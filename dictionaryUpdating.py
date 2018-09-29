# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 10:18:35 2018

@author: tfishbeck
"""

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
    

def get_Student_Name(studentDict):
    print('Which student score would you like to see? Enter the student number: ')        
    keys = studentDict.keys()
    counter = 1
    testList = []
    for i in keys:
        print(str(counter) + '. ' + i )
        counter +=1
        testList.append(i)
    x = int(input())
    print(testList[x-1]+ ' scored a ' + str(studentDict[testList[x-1]]) + ' on the test.')



def get_Test_Continuation():
    return int(input('Would you like another test score? Select 1 = Yes; 2 = No: '))


get_Student_Name(studentDict)
y = get_Test_Continuation()

while  y == 1:
    get_Student_Name(studentDict)
    y = get_Test_Continuation()
    
print('Thanks')
    
    
    
    
    









    
    
    
    
    
