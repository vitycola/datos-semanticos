import requests


r1 = requests.get("https://data.tfl.gov.uk/tfl/syndication/feeds/stations-facilities.xml?app_id=3a0c4a01&app_key=ea95c6674605181c5dde64c7bb5d883c")
r2 = requests.get("https://tfl.gov.uk/tfl/syndication/feeds/step-free-tube-guide.xml")

with open('stations-facilities.xml', 'wb') as f:
   f.write(r1.content)
with open('step-free-tube-guide.xml', 'wb') as f:
   f.write(r2.content)