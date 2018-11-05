# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

fNames = ['Tyler','Ethan','Troy','Ashlyn','Heather']

favSports= {}

for names in fNames:
    x = input(names + ', what is your favorite sport?')
    x = {names : x}
    favSports.update(x)
    
print(favSports)
    
    
            



