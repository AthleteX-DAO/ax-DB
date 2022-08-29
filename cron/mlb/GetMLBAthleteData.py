#!/usr/bin/env python

import requests                  

# Constants
API_URL = 'ax-api-athletex-api/mlb/players/update'

def syncLatestStats():
        httpResponse = requests.get(API_URL)

try:
  syncLatestStats()
except:
  print("Error occurred ")
