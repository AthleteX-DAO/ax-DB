#!/usr/bin/env python

import os
import socket
import requests
import json

from dotenv import load_dotenv   
load_dotenv()                    

# Constants
apiKey = os.environ.get("API_KEY")
HEADER = {'Ocp-Apim-Subscription-Key': apiKey }
SDIO_URL = 'https://api.sportsdata.io/v3/nfl/stats/json/PlayerSeasonStats/2021'

#HOST = '3.236.73.223'
PORT = 9009

HOST = os.environ.get("DB_HOST")
#PORT = os.environ.get("DB_PORT")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # define socket

def getTheData():
        httpResponse = requests.get(SDIO_URL, headers=HEADER)
        theData = httpResponse.json()
        return theData

def computePrice(athlete_data):
        
        #Variables
        passingYards = athlete_data['PassingYards'] / 25
        rushingYards = athlete_data['RushingYards'] / 10
        receivingYards = athlete_data['ReceivingYards'] / 10
        rushingTouchdowns = athlete_data['RushingTouchdowns'] * 6
        receivingTouchdowns = athlete_data['ReceivingTouchdowns'] * 6
        passTD = athlete_data['PassingTouchdowns'] * 4
        reception = athlete_data['Receptions'] * 0.5
        passingIntercept = athlete_data['PassingInterceptions'] * 2 * -1
        fumblesLost = athlete_data['FumblesLost'] * 2 * -1

        # Football Athletes
        numerator = passingYards + rushingYards + receivingYards + rushingTouchdowns + receivingTouchdowns + passTD + reception + passingIntercept + fumblesLost
        denominator = athlete_data['OffensiveSnapsPlayed'] or athlete_data['DefensiveSnapsPlayed']
        if denominator == 0.0:
                denominator = 1.0        
        else:
                pass

        computedAmericanFootballPrice = numerator / denominator
        if (computedAmericanFootballPrice < 0):
                computedAmericanFootballPrice = 0
        
        return computedAmericanFootballPrice

# For UDP, change socket.SOCK_STREAM to socket.SOCK_DGRAM
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  sock.connect((HOST, PORT))
  ListOfAthletes = getTheData()
  for athlete in ListOfAthletes:
        price = computePrice(athlete)
        id = athlete['PlayerID']
        name = athlete['Name']
        team = athlete['Team']
        position = athlete['Position']
        passingYards = athlete['PassingYards']
        passingTouch = athlete['PassingTouchdowns']
        reception = athlete['Receptions']
        receiveYards = athlete['ReceivingYards']
        receiveTouch = athlete['ReceivingTouchdowns']
        rushingYards = athlete['RushingYards']
        OffensiveSnapsPlayed = athlete['OffensiveSnapsPlayed']
        DefensiveSnapsPlayed = athlete['DefensiveSnapsPlayed']
        # rushingTouch = athlete['RushingTouch']
        print(name, price)
        sock.sendall((f'nfl,name={name},id={id},team={team},position={position} passingYards={passingYards},passingTouchdowns={passingTouch},reception={reception},receiveYards={receiveYards},receiveTouch={receiveTouch},rushingYards={rushingYards},OffensiveSnapsPlayed={OffensiveSnapsPlayed},DefensiveSnapsPlayed={DefensiveSnapsPlayed},price={price}\n').encode())
except socket.error as e:
  print("Got error: %s" % (e))

sock.close()
