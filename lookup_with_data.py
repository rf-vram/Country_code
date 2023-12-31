import json
import argparse

######  To get the country code from Data.json #######

with open('data.json', 'r') as file:
    data = json.load(file)
    country_code = input("Enter country code: ")
    countries = ['data'][country_code]['name']
    print (countries)

    
parser = argparse.ArgumentParser(description="Country Code Lookup")
parser.add_argument("--countryCodes", nargs='+', help="List of country codes separated by space")
args = parser.parse_args()