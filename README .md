# Iot
## Sub task
* Get and store the client name from command line argument.
* Set this as client name for client object.
* Subscribe to the “location/uav” topics where "uav" are given in python list called all_clients and do not subscribe to location topic of a client itself.
 
* Write code to publish your current location on topic “location/<client_name>” where client_name is current client name, sleep for 10 seconds and repeat.
* Complete on_message() method 
* * Extract location data from the received message.
* * Extract client name from received message.
 * in this method calculate distance using vehical.txt and uav.txt

 *  Calculate Distance from your current location.(Distance function is provided).
* Store the client location if distance is minimum and track the nearest vehicle

* HQ code publish the velical.data nad subscribe uav to get location of nearest and store in the output.txt
* uavstater are use command line argument and pass in the uav.py
* code subscribe hq to get the vehicle location and calculate distance and track nearest location vehicle and publish the location 

* To test your code run activity.sh

