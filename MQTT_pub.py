import paho.mqtt.client as mqtt
import time
import logging
broker = "192.168.1.76"
port =1883
logging.basicConfig(level=logging.INFO)
def on_log(client, userdata, level, buf):
    logging.info(buf)
def on_connect(cllient, userdata , flags, rc):
    if rc ==0:
        client.connect_flag =True #set flag
        logging.info("connected OK")
    else:
        logging.info("Bad connection retured code"+str(rc))
        client.loop_stop()
def on_disconnect(client, userdata,rc):
    logging.info("client disconnect ok")

def on_publish(client, userdata,mid):
    logging.info("In on_pub callback mid"+str(mid))
def reset():
    ret = client.publish("humidity","",0,True)
def on_subscribe(client,userdata,mid,granted_qos):
    logging.info("subscribe")
def on_message(client,userdata,message):
    topic=message.topic
    msgr =str(message.payload.decode("utf-8"))
    msgr ="message received"+msgr
    logging.info(msgr)

mqtt.Client.connect_flag =False      #set retain =False
client = mqtt.Client("python 1") #creat new instance
client.on_log =on_log
client.on_connect =on_connect#bind call back function
client.on_disconnect =on_disconnect
client.on_publish=on_publish
client.on_subscribe=on_subscribe
client.connect(broker,port)       #establish connection
client.loop_start()
while not client.connect_flag: #wait in loop
    logging.info("in wait loop")
    time.sleep(1)
time.sleep(3)
logging.info("publishing")
ret =client.publish("humidity","80",0) #publish
logging.info("publish return"+str(ret))
time.sleep(3)
#client.loop()
ret =client.publish("humidity","90",1) #publish
logging.info("publish return"+str(ret))
time.sleep(3)
#client.loop()
ret =client.publish("humidity","85",2) #publish
logging.info("publish return"+str(ret))
time.sleep(3)
#client.loop()Unique
time.sleep(3)
client.subscribe("Lamp",2)
#reset()
time.sleep(10)
client.loop_stop()
client.disconnect()


