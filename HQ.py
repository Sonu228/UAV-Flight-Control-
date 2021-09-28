#sonu kumar cs20mtech11011
#create client 
# read vehical.txt  using readline function in python
#publish the data to finding distance

import paho.mqtt.client as mqtt

import time
import re
import sys
import random



file1 = open('vehicle_location.txt','r')    #reading the data in vehical.txt 
file2 = open('output.txt','a')             # store the data in output.txt with write function

# initalize the vefical location
vehical_location = [False,False,False,False,False,False]	

#used for uav python list for vehical location
uav_location = [0,0,0,0,0,0]		

def on_connect(client, userdata, flags, rc):
    print("HQ Connected to broker")

def on_message(client, userdata, message):
#write the output file.
	n = int(re.search('\d',message.topic).group(0))
	massage = message.payload
	for i in range(0,6):
		if not (vehical_location[massage[i]-1]): 
			vehical_location[massage[i]-1] = True
			break
	uav_location[n-1] = massage[i]
	client.publish('HQ/Target_allocation',str(n)+' '+str(i+1))
	if uav_location[0]*uav_location[1]*uav_location[2]*uav_location[3]*uav_location[4]*uav_location[5]:
		file2.write(str(uav_location[0])+' '+str(uav_location[1])+' '+str(uav_location[2])+' '+str(uav_location[3])+' '+str(uav_location[4])+' '+str(uav_location[5])+'\n')

client = mqtt.Client('HQ')

#used for callbck on connect 
client.on_connect = on_connect
#used for callback on massage
client.on_message = on_message	

#broker address initalize
broker_address = "127.0.0.1"  
# broker port intialize
port = 1883  

client.connect(broker_address, port=port)  # connect to broker

client.loop_start()  # start the loop

for i in range(1,7):
	client.subscribe('Priority/UAV'+str(i),2)

for data in file1:
	client.publish('HQ/location',file1.readline())
	time.sleep(10)
	vehical_location = [False,False,False,False,False,False]
	uav_location = [0,0,0,0,0,0]

file1.close()
file2.close()
