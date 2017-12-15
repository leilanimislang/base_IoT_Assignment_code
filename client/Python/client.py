#Base Python client for MEng in IoT Assignment
#consumes data from IoT Gateway
import urllib3
from xml.etree import ElementTree
import matplotlib.pyplot as plt

#URL to be accessed
url = 'http://localhost:8080/' 

#create a pool manager and get connection to URL
http = urllib3.PoolManager()
response = http.request('GET', url)
resp = response.data.decode('utf-8')

#read response as xml format
tree = ElementTree.fromstring(resp)
#declaration of arrays
timeDataArray = []
tempDataArray = []

#get individual readings and store them into array per iteration
for reading in tree.iter('reading'):
	timeData = reading.find("time").text
	tempData = reading.find("temperature").text
	timeDataArray.append(timeData)
	tempDataArray.append(tempData)

#graph configuration	
plt.title("Temperature over Time Readings")
plt.xlabel('Temperature')
plt.ylabel('Time')
plt.bar(tempDataArray, timeDataArray, color="blue")
plt.show()
	

