import requests
import json


######  To get the Country code from API ########
response = requests.get('https://www.travel-advisory.info/api')

response_json = json.loads(response.text)
country_code = input("Enter country code: ")
print ((response_json['data'][country_code]['name']))




