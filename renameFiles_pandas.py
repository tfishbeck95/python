#This module renames files into an output folder in the same directory based on their date value

import pandas as pd
import os, os.path
import shutil
import csv
import getpass




def renameFiles(sourceDir):
    files = []
    dirPath = sourceDir
    outputPath = os.path.join(dirPath,'output')
    newFileName = input('What will the new file prefix be: ')
    for i in os.listdir(dirPath):
        fileName = os.path.join(dirPath,i)
        if os.path.isfile(fileName):
            files.append(fileName)
            fileDate = pd.read_csv(fileName,sep=',',usecols=['Year and Month'],nrows = 5,low_memory = False).at[0,'Year and Month']
            print(fileDate)
            if not os.path.exists(outputPath):
                os.mkdir(outputPath)
                shutil.copyfile(fileName,os.path.join(outputPath,str(fileDate)+str(newFileName)+'.txt'))
            else:
                shutil.copyfile(fileName,os.path.join(outputPath,str(fileDate)+str(newFileName)+'.txt'))



userName = getpass.getuser()
#Put the source directory here
dir = 'C:\\Users\\'+ userName+'\\Box\\FBIT_TeamFolder\\Reporting and Processing\\Shared Data\\Oracle Queries\\Server Revenues\\'
renameFiles(dir)






