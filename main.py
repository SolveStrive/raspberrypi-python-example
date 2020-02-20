# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import Adafruit_DHT
import time
import requests
from datetime import datetime

# constants
DHT_PIN = 4  # GPIO nr
DHT_SENSOR = Adafruit_DHT.DHT22

temperature = None
humidity = None

# read the data from the sensor
while temperature == None:
    _, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if temperature == None:
        time.sleep(1.5)

while humidity == None:
    humidity, _ = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity == None:
        time.sleep(1.5)

# get actual time
now = datetime.now()
current_time = now.strftime("%Y-%m-%dT%H:%M:%S")

# create the payload
temperaturePayload = {'classification': 'Temperature',
                      'value': temperature,
                      'unit': '°C',
                      'logTime': current_time}
humidityPayload = {'classification': 'Humidity',
                   'value': humidity,
                   'unit': '%',
                   'logTime': current_time}

# setup the header for the https API Request
headers = {'Content-Type': 'application/json', 'ApiKey': 'add your API Key here'}

# send one post request for the temperature data and one for the humidity data
requests.post('https://api.solvestrive.com/measurement-data/realm/## add your Realm Id here ##/data', headers=headers, json=temperaturePayload)
requests.post('https://api.solvestrive.com/measurement-data/realm/## add your Realm Id here ##/data', headers=headers, json=humidityPayload)
