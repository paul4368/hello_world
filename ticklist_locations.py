#!/usr/bin/env python
# -*- coding: utf-8 -*-




import pandas as pd
import numpy as np
import io
import xlrd
import xlsxwriter
import matplotlib.pyplot as plt
import csv
import plotly.express as px
from pick import pick
import os


cmd = 'mode 180,60' # To set the size of the Terminal Window
os.system(cmd)

df = pd.read_excel(r'Z:\Docs\DailyOperationalProcedures\Password Tick Sheets\Password Change Tick Sheet Master.xlsx', sheet_name='Server List', skiprows=3, usecols='B,C,D,E,H,I')


df.columns = df.iloc[0]
df = df[1:]

#df.columns


df = df[pd.notnull(df['Customer'])]


unique_cust = df["Customer"].unique()



title = 'Which Customer to Query? '
options = ['Fujitsu', 'NI WATER', 'eHR Connect', 'Libraries NI', 'CAFOS', 'EA', 'IMS', 'SSCL', 'Whitbread BART']
option, index = pick(options, title)
x = option
y = index
print(x)


print(df[df['Customer'].str.match(x) | (df.index == 0)])


input('\nPress Enter to Exit Screen...')

