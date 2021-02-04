import pandas as pd
import numpy as np
import json as json
import tabula
import csv
import xlsxwriter


# Assigning countries and codes to universal variables
with open('data/country_codes.json') as f:
    j = json.load(f)
for i in j:
    country = i["Name"]
    country_code = i["Code"]


# c = open('data\World - Real GDP Levels, Annual, Billion 2015 US Dollars.csv')
# p = 'data\Population_and_migration.pdf'        # Assigning PDF filepath to variable



# Creating final output Excel
output_file = xlsxwriter.Workbook('CaseStudyOutput.xlsx')
cpi1 = output_file.add_worksheet("CPI")
gdp2 = output_file.add_worksheet("GDP")
population3 = output_file.add_worksheet("Population")

# https://www.geeksforgeeks.org/python-create-and-write-on-excel-file-using-xlsxwriter-module/

# Updating CPI tab
cpi1.write('A1', 'Country')
cpi1.write('B1', 'Country Code')
cpi1.write('C1', 'CPI')

# Updating GDP tab
gdp2.write('A1', 'Country')
gdp2.write('B1', 'Country Code')
gdp2.write('C1', 'GDP')

# Updating Population tab
population3.write('A1', 'Country')
population3.write('B1', 'Country Code')
population3.write('C1', 'Population')

output_file.close()