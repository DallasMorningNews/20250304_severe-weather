import pandas as pd
import requests
import json

r = requests.get('https://poweroutage.us/api/web/counties?key=9818916638&countryid=us&statename=Texas')
print(r.json())

df = pd.DataFrame(r.json()['WebCountyRecord'])
df['outage_percentage'] = (df['OutageCount']/df['CustomerCount'])*100

df.to_csv('data/latest.csv', index=False)