#sonu kumar cs20mtech11011
#create client 
# read vehical.txt  using readline function in python
#publish the data which is nearest location

import paho.mqtt.client as mqtt
import time

import sys
import re
import ast
import random
import math

def on_connect(client, userdata, flags, rc):
    print("CLIENT-name"+str(list)+' Connected to broker.\n\nTarget vehicle id:')



def on_message(client, userdata, message):
#Sort the vehicles in descending order of their distance. Then send ur preferences to HQ.
	uav_location = re.match('\d+',file.readline())
	x = int(uav_location.group(1))
	y = int(uav_location.group(2))
	vehical_location = re.match('\d+',message.payload)
	#create vehical_corr python list for distance calculation
	vehical_corr = []
	for i in range(1,vehical_location.lastindex+1):
		vehical_corr.append(int(vehical_location.group(i)))
	uav_corr = []
	while j in range(0,vehical_location.lastindex): 
		uav_corr.append(distance(x,vehical_corr[j],y,vehical_corr[j+1]))
		j+=2
	uav_corrs = uav_corr
	uav_corrs.sort()
	dist = []
	for j in uav_corrs:
		dist.append(uav_corr.index(j)+1)
	client.publish('Priority/CLIENT' + list,dist)
	

def traking(client, userdata, message):
	p = re.match('\d+',message.payload)
	p_id = ''
	if p.group(1) == list:
		p_id = p.group(2)
		print(p_id)
		#traking vehicle with id p_id


def distance(xi,xj,yi,yj):
	return (xi-xj)**2 + (yi-yj)**2
#getting the client name from cmd argument	
list = sys.argv[1]	

client = mqtt.Client(list)
	
client.on_connect = on_connect
client.on_message = on_message
client.message_callback_add('HQ/Target_allocation',traking)
# Broker address initalize
broker_address = "127.0.0.1"  
# Broker port initiazile
port = 1883  

client.connect(broker_address, port=port)
#loop starts	
client.loop_start()  
# subscribe the hq 
client.subscribe('location/HQ',2)	

file = open('client'+list+'.txt','r')

file.close()

time.sleep(20)

#sonu kumar cs20mtech11011 