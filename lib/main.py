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
print(colored(26*" " + "1. Port Scanner -> Socket", "blue"))
print(colored(26*" " + "2. Ping Sweeping", "blue"))
print(colored(26*" " + "3. Port Scanner -> TCP Scan", "blue"))
print(colored(26*" " + "4. Port Scanner -> Threaded -> efficiency", "blue"))

def port_scanner_socket():
    startTime = time.time()
    target = input("Enter the host: ::")
    t_IP = gethostbyname(target)
    print(colored(f"Scanning Host on: {t_IP}", "blue"))
    for i in range(50, 500):
        s = socket(AF_INET, SOCK_STREAM)
        conn = s.connect_ex((t_IP, i))
        if conn == 0:
            print('Port %d: OPEN' % (i,))
        print('Port %d: CLOSED' % (i,))
        s.close()
    print('Time: ', time.time() - startTime)

def ping_sweep():
    net = input("Enter the Network Address: ")
    net1 = net.split('.')
    a = '.'
    
    net2 = net1[0] + a + net1[1] + a + net1[2] + a
    st1 = int(input("Enter the Starting Number: "))
    en1 = int(input("Enter the Last Number: "))
    en1 = en1 + 1
    if os.name == "nt":
        ping1 = "ping -n 1 "
    else:
        ping1 = "ping -c 1 "
    t1 = datetime.now()
    print("Scanning in Progress")
    
    for ip in range(st1, en1):
        addr = net2 + str(ip)
        comm = ping1 + addr
        response = os.popen(comm)
   
        for line in response.readlines():
            if line.count( "TTL"):
                break
            if line.count("TTL"):
                print(addr, "--> Live")
    
    t2 = datetime.now()
    total = t2 - t1
    print("Scanning completed in: ", total)

input_ = int(input("::Expect::"))

if input_ == 1:
    port_scanner_socket()
    
elif input_ == 2:
   ping_sweep()
   
elif input_ == 3:
    os.system("python3 lib/tcp_scan.py")
    
elif input_ == 4:
    os.system("python3 lib/ef_scanner.py")
   
else:
    exit()
    








