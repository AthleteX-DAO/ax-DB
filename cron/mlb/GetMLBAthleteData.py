#!/usr/bin/env python

import requests                  

# Constants
API_URL = 'http://ax-api-athletex-api:8080/mlb/players/update'

def syncLatestStats():
        httpResponse = requests.get(API_URL)

try:
  syncLatestStats()
except:
  print("Error occurred ")
