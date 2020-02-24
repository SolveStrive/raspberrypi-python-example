# raspberrypi-python-example
Example Application of a Cloudstorage for a Measurement Application using a Raspberry Pi

In this tutorial we setup a raspberry pi to measure the ambient temperature and the humidity and store it in a cloud storage.

## Bill of Material
For this tutorial you need the following hardware:
- a Raspberry Pi
- a DHT11 or DHT22 Sensor
- a 10k Resistor
- a Breadboard
- The wires for wiring

## Setup your measurement realm at SolveStrive
Open your browser and got to https://app.solvestrive.com
Login to the application or create a account.
Add a new measurement realm by clicking the create measurement realm button at the start page. 
![Logo](/images/SolveStrive_add_realm.png)

Type in the name of the realm and press create.
Now the realm should be shown at the measurement realm list. If not reload the page.
Click at the realm. Now the detail data of the measurement realm are shown.
Here you can find the realm id. This we will ned a bit later.

The next step is to create a API Token.
Go to the administration -> user data.
If the Field API token is empty press the button "Generate API Key"

## Connect the Sensor to the Raspberry Pi

![Logo](/images/DHT11_connect.png)

The left pin of the sensor is connected to 3V3 of Pi (pin1), 
the second sensor pin via a pull-up resistor (4.7k – 10kΩ) with a free GPIO of the raspberry (GPIO4, pin7) and the right senior pin comes at GND (Pin6) from the Pi.
The second pin from the right of the sensor remains free.

The structure is identical for DHT11 or DHT22 since the pins are assigned the same way.

## Setup the raspberry pi
Before we start we have to setup the raspberry pi. Therefore follow the instruction at the link: https://www.raspberrypi.org/documentation/installation/installing-images/README.md

When the raspberry pi is setup and connected to the internet install git.
Use the following commands to install all needed software
```
sudo apt-get update
sudo apt-get install build-essential python-dev python3-dev python3-openssl python3-smbus python3-pip i2c-tools git
```
Clone the needed git repository's and install the software
```
cd ~/Desktop/
git clone https://github.com/adafruit/Adafruit_Python_DHT.git && cd Adafruit_Python_DHT
sudo python3 setup.py install
cd ..
git clone https://github.com/SolveStrive/raspberrypi-python-example.git
```

Before we can start the script we have to enter your measurement realm and your API key to the main.py.

![Logo](/images/api-setup.png)

Copy the measurement realm id and the API key from the measurement realm detail view and the user view like describe at the section before.

The measurement realm id need to be entered at the main.py at line 44 and 45.

The API key you need to insert in line 41.

To run the script and start one measurement circle run the following command.
```
cd ~/Desktop/raspberrypi-python-example
python3 main.py
```
This will measure the temperature and humidity and store the values at the SolveStrive platform in your measurement realm.

## Setup a cronjob
Now we have to setup a cronjob to repeat this script at defined time.

Run ``` crontab -e ``` to edit the cron table.

Insert the command ``` */15 * * * * python3 /home/pi/Desktop/raspberrypi-python-example/main.py``` ath the end of the file and save and close it.