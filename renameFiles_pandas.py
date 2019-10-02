#This module renames files into an output folder in the same directory based on their date value

import pandas as pd
import os, os.path
import shutil




def renameFiles():
    files = []
    dirPath = 'C:\\Users\\TylerFishbeck\\Box\\FBIT_TeamFolder\\Reporting and Processing\\Shared Data\\Hardware Operating System\\'
    outputPath = os.path.join(dirPath,'output')
    newFileName = input('What will the new file prefix be: ')
    for i in os.listdir(dirPath):
        fileName = os.path.join(dirPath,i)
        if os.path.isfile(fileName):
            files.append(fileName)
            fileDate = pd.read_csv(fileName,sep=',',usecols=['Year and Month'],nrows = 5,low_memory = False).at[0,'Year and Month']
            print(fileDate)
            shutil.copyfile(fileName,os.path.join(outputPath,str(fileDate)+str(newFileName)+'.txt'))










