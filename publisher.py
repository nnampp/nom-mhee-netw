import paho.mqtt.client as mqtt
import pandas as pd
import numpy as np
import sys
import time

# ----------------------------------------------------------------------------------------------------------------
# command line syntax:
#  C:/Users/User/anaconda3/python.exe d:/work/2-2022/CPE314/project_mqtt/publisher.py [publisher no.]
# ----------------------------------------------------------------------------------------------------------------

pub = sys.argv[1]
data = pd.DataFrame({'A' : []})
topic = ''

host = "broker.mqttdashboard.com"
port = 1883

if pub == '1':
    data = pd.read_excel("D:/work/2-2022/CPE314/project_mqtt/SampleInput.xlsx")
    topic = "MQTT/TOPIC1"
elif pub == '2':
    data = pd.read_excel("D:/work/2-2022/CPE314/project_mqtt/SampleInput2.xlsx")
    topic = "MQTT/TOPIC2"
else:
    print("Publisher number is not available (available just 1 and 2). Please try again.")
    sys.exit()

client = mqtt.Client(pub)
# print("Subscriber IP address: " + client._host)
client.connect("mqtt.eclipseprojects.io", 1883, 60)
for x in data.values:
    
    print(sys.getsizeof(str(x[0])+","+str(x[1])+","+str(x[2])))
    print(sys.getsizeof(str(x[3][0:163])))
    print(sys.getsizeof(str(x[3][163:])))
 
    client.publish(topic,"start")
    client.publish(topic,str(pub).zfill(4))
    client.publish(topic,str(x[0])+","+str(x[1])+","+str(x[2]))
    client.publish(topic,str(x[3][0:165]))
    client.publish(topic,str(x[3][165:]))
    client.publish(topic,"end")
    time.sleep(15)