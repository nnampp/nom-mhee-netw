import paho.mqtt.client as mqtt
import mysql.connector
from datetime import datetime
import sys
import socket

# hostname = socket.gethostname()
# IPAddr = socket.gethostbyname(hostname)
# print("IP address: "+IPAddr)

# ----------------------------------------------------------------------------------------------------------------
# command line syntax:
#  C:/Users/User/anaconda3/python.exe d:/work/2-2022/CPE314/project_mqtt/subscriber.py [topic1] [topic2]
# ----------------------------------------------------------------------------------------------------------------

topic = ''
topic1 = ''
topic2 = ''

if(len(sys.argv) == 3): 
    topic = [(sys.argv[1],0),(sys.argv[2],0)]
elif(len(sys.argv) == 2):
    topic = sys.argv[1]
else:
    print("Please enter topic 1-2 topics.")
    sys.exit()

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mqtt_subscriber_1")

count = 0
id = ''
date_time = ''
humid = 0
temp = 0
therm = ''
sql = '' 

def on_connect(self, client, userdata, rc):
    print("MQTT Connected.")
    self.subscribe(topic)

def on_message(client, userdata,msg):     
    global count, date_time, humid, temp, therm, sql, id

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")   

    txt = msg.payload.decode("utf-8") 
    if(txt == "start"):
        count += 1
    elif(count == 1):
        count += 1
        id = txt
    elif(count == 2):
        count += 1
        date_time, humid, temp = txt.split(',')
    elif(count == 3 or count == 4):
        count += 1
        therm += txt
    elif(txt == "end"):
        sql = "INSERT INTO `sensor_read`(`NodeID`,`Time`, `Humidity`, `Temperature`, `ThermalArray`) VALUES ('"+id+"','"+date_time+"',"+humid+","+temp+",'"+therm+"')"
        print(id)
        print(current_time)
        print(date_time+'\n'+str(humid)+'\n'+str(temp)+'\n'+therm)
        print("----------------------------------------------------------------")
        count = 0
        id = ''
        humid = 0
        temp = 0
        date_time = ''
        therm = ''
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        mydb.commit()


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("mqtt.eclipseprojects.io", 1883, 60)
client.loop_forever()