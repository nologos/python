from bs4 import BeautifulSoup as bs 
import os
import re
import time
import pathlib


#dont need soup here at all

ts = time.time()
time.ctime(int(ts))

result = os.popen("curl 192.168.0.1").read()
attached = re.findall(r'dev\ \=\ \'(.*)\'\;', str(result), re.M)

list = str(attached).replace("['","").replace("']","").split("<lf>")

os.getcwd()

logs = "/home/admin/Documents/GIT/python/routerpage automation/logfile"
header = "name,macaddress,connectiontype,time"
open(logs, "w").write(str(header)+ "\n")
for item in list:
    array = (item +','+ str(ts))    
    open(logs, "a").write(str(array)+ "\n")



# class device:
#     def __init__(self,name,macaddress,connectiontype,time):
#         self.name = name
#         self.macaddress = macaddress
#         self.connectiontype = connectiontype
#         self.time = time


# device1 = device(array[0],array[1],array[2],array[3])
