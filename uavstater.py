#sonu kumar cs20mtech11011
#create uavclient creater 
# command line arrument

import sys
import os

i = int(sys.argv[1])

for j in range(1,i+1):
	os.system('gnome-terminal -- python3 UAVClient.py '+str(j))
