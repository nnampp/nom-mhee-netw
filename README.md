# nom-mhee-netw
**CPE314: Computer Networks (2/65)**
Project I

# Title
**Implementing MQTT-based IoT application**

# Description
  This is a group project about MQTT-based IoT application that sends sensor reading from an IoT node to a remote database. The system consists of 3 entities - Client (IoT node, Publisher), Broker and Server (Subscriber). Using Python, online broker from MQTT and SQL database to complete this project.
  
# ✅Completed GOALS
1. Client only send at most 250 bytes in 1 message.
2. Multiple IoT nodes can be deployed in the system.
3. Broker prints IP address when there is a new connection.
4. Broker prints published messages.
5. Server prints received messages from broker.
6. Subscriber can subscribe more than 1 topic.
7. Server can query the database.

# Files
* **mqtt_subscriber_db** - SQL file for setting up database including sensor_read table
* **publisher.py** - Python file for starting publisher, connecting to broker and publishing data from IoT nodes
* **subscriber.py** - Python file for starting subscriber, connecting to broker, subscribing topic and insert data to database

# Getting Started
1. Download MQTT broker from https://mosquitto.org/
2. Start MQTT broker in port 8883
```
cd C:\Program Files\mosquitto
mosquitto -v -p 8883
```
2. Start publisher.py with publisher number (there are 2 available publishers)
```
python publisher.py [publisher no.]
```
3. Start subscriber.py with topics (there are just 1 available subscribers which can subscribe 1-2 topics)    
```
python subscriber.py [topic1] [topic2]
```
Note:   
  1. The command for compiling python file is depends on user machine (ex. somes have to use 'python3')
  2. The publisher must be placed in the same folder with sample input files
  3. About publisher and subscriber connection,
      * Publisher will disconnect broker if no data flows over an open connection for 5 minutes or finish sending all data from the input file
      * Subscriber will disconnect broker if no data flows over an open connection for 5 minutes 

# Team members
1. Kanyapak     Sodpo               63070501003
2. Kunanya      Khuntiptong         63070501010
3. Nattanit     Nookwan             63070501022
4. Nirosesofia  Phamonpol           63070501041
5. Monthida     Arnuphapsamosorn    63070501056
6. Sarunwarin   Wongudomtanakol     63070501058
  
See more details in the report.💖
