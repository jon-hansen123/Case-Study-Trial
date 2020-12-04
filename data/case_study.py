import pandas as pd
import numpy as np
import json as json
import tabula
import csv

# Opening all files for extraction
j = open('data\country_codes.json')
c = open('data\World - Real GDP Levels, Annual, Billion 2015 US Dollars.csv')
p = 'data\Population_and_migration.pdf'        # Assigning PDF filepath to variable

# Creating data frames for extraction
gdp_levels = []
population = []
codes = {}
codes = json.load(j)
gdp_levels = pd.read_csv(c).fillna(0)
tabula.convert_into(p, "Population.csv", output_format= "csv", pages= 3)
population = pd.read_csv("Population.csv")

# Clean converted file output
def clean_output():
    for column in population.loc[:, population.columns != 'Unnamed: 0']:
        population[column] = population[column].str.replace(" ", "")
        population[column] = population[column].replace("..", "0")
    return population
