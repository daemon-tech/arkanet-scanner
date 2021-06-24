import os
import nmap3
import time
import platform
import socket
from datetime import datetime
from pyfiglet import Figlet
from termcolor import colored, cprint
from socket import *

os.system("clear")

title = Figlet(font="banner3-D")
print(colored(title.renderText("ARKANET"), "blue"))
print("")
print(27*"*" + 19*"*" + 27*"*")
print(" ")
import socket
import time
import threading

from queue import Queue
socket.setdefaulttimeout(0.25)
print_lock = threading.Lock()

target = input('Enter the host to be scanned: ')
t_IP = socket.gethostbyname(target)
print ('Starting scan on host: ', t_IP)

def portscan(port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      con = s.connect((t_IP, port))
      with print_lock:
         print(port, 'is open')
      con.close()
   except:
      pass

def threader():
   while True:
      worker = q.get()
      portscan(worker)
      q.task_done()
      
q = Queue()
startTime = time.time()
   
for x in range(100):
   t = threading.Thread(target = threader)
   t.daemon = True
   t.start()
   
for worker in range(1, 500):
   q.put(worker)
   
q.join()
print('Time taken:', time.time() - startTime)