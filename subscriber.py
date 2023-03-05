import paho.mqtt.client as mqtt
import mysql.connector
from datetime import datetime
import sys

# ----------------------------------------------------------------------------------------------------------------
# command line syntax:
#  C:/Users/User/anaconda3/python.exe d:/work/2-2022/CPE314/project_mqtt/subscriber.py [topic1] [topic2]
# ----------------------------------------------------------------------------------------------------------------

topic = ''
topic1 = ''
topic2 = ''

# This architecture have 1 available subscriber
# Subscriber can subscribe topic up to 2 topic
# User can input 1 or 2 topic to subscribe
# If user do not input any topic or subscriber more than 2 topic, this program will terminate itself
if(len(sys.argv) == 3): 
    topic = [(sys.argv[1],0),(sys.argv[2],0)]
elif(len(sys.argv) == 2):
    topic = sys.argv[1]
else:
    print("Please enter topic 1-2 topics.")
    sys.exit()

# Connect to MySQL database from localhost
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mqtt_subscriber_db")

count = 0
id = ''
date_time = ''
humid = 0
temp = 0
therm = ''
sql = '' 

# Function to subscribe topic after connect to mqtt broker
def on_connect(self, client, userdata, rc):
    print("MQTT Connected.")
    self.subscribe(topic)

# Function to receive packets from publisher
def on_message(client, userdata,msg):     
    global count, date_time, humid, temp, therm, sql, id

    # Print out current time that subscriber receive packets
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")   

    # Because the publisher send multiple packet per data row,
    # subscriber have to gather data from each packet to insert a row to database
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

# Create client from mqtt which name is "Subscriber"
client = mqtt.Client("Subscriber")
client.on_connect = on_connect
client.on_message = on_message
# Connect this client to mqtt broker, that already install in the computer we run code
client.connect("localhost", 8883, 300)
client.loop_forever()