import requests                  

# Constants
API_URL = 'http://ax-api-athletex-api:8080/nfl/players/update'

def syncLatestStats():
        httpResponse = requests.get(API_URL)

try:
  syncLatestStats()
except:
  print("Error occurred ")