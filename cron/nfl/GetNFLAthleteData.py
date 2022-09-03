import requests                  

# Constants
API_URL = 'ax-api-athletex-api/nfl/players/update'

def syncLatestStats():
        httpResponse = requests.get(API_URL)

try:
  syncLatestStats()
except:
  print("Error occurred ")