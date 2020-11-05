import pandas as pd
import json as json
import tabula

# Opening all files for extraction
j = open('data\country_codes.json')
c = open('data\World - Real GDP Levels, Annual, Billion 2015 US Dollars.csv')
p = 'data\Population_and_migration.pdf'        # Assigning PDF filepath to variable

# Creating data frames for extraction
gdp_levels = []
population = []
codes = json.load(j)
gdp_levels = pd.read_csv(c)
population = tabula.convert_into(p, "Population.csv", output_format= "csv", pages= 3)


# Clean file outputs

