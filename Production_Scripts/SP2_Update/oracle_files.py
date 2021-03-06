# -*- coding: utf-8 -*-

import os,time,shutil

#Determines to root drive
dDrive = input('What is the target root drive: ').lower()

#Determines the base path after root drive
if dDrive == 'c':
    rPath = str(':\\users\\tfishbeck\\')
else:
    rPath = str(':\\')    
basePath = dDrive + rPath

cMonth = str(input('What is the new folder month: ') + '\\')

# This returns the full filepath to copy to
if dDrive != 'c':
    cDrive = str(basePath + 'TableauRepoSP2\\sp2_models')
else:
    cDrive = str(basePath + str('documents\\TableauRepoSP2\\sp2_models\\'))

fPath = os.path.join(cDrive, cMonth)

os.mkdir(fPath) #This creates the Year and Month directory

os.mkdir(os.path.join(fPath, 'power_tables\\')) #\\TableauRepoSP2\\sp2_models
os.mkdir(os.path.join(fPath, 'SP_Info\\'))


#This creates the new folder for the SP2 source files
powerTableList = ['bp_dc.csv','proc_ram.csv','gpu_hdd.csv','mobo_nc.csv']
spInfoList = ['Hardware Depreciation.csv','HardwareStatus.csv','IBM Account Merge.csv',
              'LBFW_Allocations.csv','Server Profitability - Actuals Dashboard.csv',
              'Server Profitability - Incremental Dashboard.csv',
              'Server Profitibility - Inventory 2.0 MRB Adjustment.csv',
              'SP2 Analysis Data.csv','StorageDevicePull.csv']


for i in os.listdir(os.path.join(basePath, 'Downloads')):
    iPath = os.path.join(basePath, 'Downloads')
    if i in powerTableList:
        shutil.copy(os.path.join(iPath, str(i)),os.path.join(fPath,'power_tables'))
    elif i in spInfoList:
        shutil.copy(os.path.join(iPath, str(i)),os.path.join(fPath,'SP_Info'))

#This creates a new source file
if input('Do you want to create a new source file? ').lower()[0] == 'y':    
    fullFileList = powerTableList + spInfoList
    newFilePaths = []
    
    for i in fullFileList:
        newFilePaths.append(str(fPath) + i + '\n')
        
    with open(os.path.join(fPath, 'QuerySources.txt'), 'w') as f2:
        f2.writelines(newFilePaths)




    
    
