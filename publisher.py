import paho.mqtt.client as mqtt
import pandas as pd
import sys
import time

# ----------------------------------------------------------------------------------------------------------------
# Command line syntax:
#  C:/Users/User/anaconda3/python.exe d:/work/2-2022/CPE314/project_mqtt/publisher.py [publisher no.]
# ----------------------------------------------------------------------------------------------------------------

pub = sys.argv[1]
data = pd.DataFrame({'A' : []})
topic = ''

# This architecture have 2 available publishers (publisher 1 and publisher 2) which have different topic and different input data
# If user input unavailable publisher number or doesn't input publisher number, this program will terminate itself
if pub == '1':
    data = pd.read_excel("D:/work/2-2022/CPE314/project_mqtt/SampleInput.xlsx")
    topic = "MQTT/TOPIC1"
elif pub == '2':
    data = pd.read_excel("D:/work/2-2022/CPE314/project_mqtt/SampleInput2.xlsx")
    topic = "MQTT/TOPIC2"
else:
    print("Publisher number is not available (available just 1 and 2). Please try again.")
    sys.exit()

# Create client from mqtt which name is "Publisher" and its number
client = mqtt.Client("Publisher "+pub)
# Connect this client to mqtt broker, that already install in the computer we run code
client.connect("localhost", 8883, 60)

# Loop for publish each row
for x in data.values:
    # Print out size of each chunks to ensure that size is not more than 250 bytes
    # We will partition a row to reduce size per packet
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(sys.getsizeof(str(x[0])+","+str(x[1])+","+str(x[2])))
    print(sys.getsizeof(str(x[3][0:163])))
    print(sys.getsizeof(str(x[3][163:])))
 
    # Start publish each packet 
    client.publish(topic,"start")
    client.publish(topic,str(pub).zfill(4)) # Node ID
    client.publish(topic,str(x[0])+","+str(x[1])+","+str(x[2])) # Time, Humidity and Temperature
    client.publish(topic,str(x[3][0:165])) # Thermal Array part 1
    client.publish(topic,str(x[3][165:])) # Thermal Array part 2
    client.publish(topic,"end")
    # Finish publish value in one row
    time.sleep(15)