# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 16:56:22 2018

@author: Owner
"""

import os

for folderName,subfolders,filenames in os.walk('c:\\users\\owner\\box\\sp2_developer_documentation\\tableaureposp2\\sp2_ap_v2'):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
        for filename in filenames:
            print('FILE INSIDE ' + folderName + ': ' + filename)
            
        