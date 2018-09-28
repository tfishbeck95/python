# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd

df = pd.read_csv('C:\\Users\\tfishbeck\\Documents\\TableauRepoSP2\\SP2_AP_V2\\sp2_cost\\201807_incremental.csv')
df1 = pd.read_csv('C:\\Users\\tfishbeck\\Documents\\TableauRepoSP2\\SP2_AP_V2\\sp2_cost\\201806_incremental.csv')

df2 = df1.append(df)

dfHead = df.head(1)
dfHardware = df[['Hardware ID','Modified POD Code']]
dfFirewall = df2[df2['Hardware Type'] =='Server']

print(dfFirewall)



