import os 
import threading
import requests, random
from dhooks import Webhook
import ctypes
from colorama import init 

init()

ctypes.windll.kernel32.SetConsoleTitleW("Synax Group Finder")


def groupfinder():
    id = random.randint(1000000, 151000000)
    r = requests.get(f"https://www.roblox.com/groups/group.aspx?gid={id}") 
    if 'owned' not in r.text:
        re = requests.get(f"https://groups.roblox.com/v1/groups/{id}")
        if 'isLocked' not in re.text and 'owner' in re.text:
            if re.json()['publicEntryAllowed'] == True and re.json()['owner'] == None:
                hook.send(f'Hit: https://www.roblox.com/groups/group.aspx?gid={id}')
                print(f"[+] Hit: {id}")
            else:
                print(f"[-] No Entry Allowed: {id}")
        else:
            print(f"[-] Group Locked: {id}")
    else:
        print(f"[-] Group Already Owned: {id}")


print("""
                           (                            
 (                         )\ )           (             
 )\ )   (         (       (()/( (         )\ )  (  (    
(()/(   )(   (   ))\ `  )  /(_)))\  (    (()/( ))\ )(   
 /(_))_(()\  )\ /((_)/(/( (_))_((_) )\ )  ((_))((_|()\  
(_)) __|((_)((_|_))(((_)_\| |_  (_)_(_/(  _| (_))  ((_) 
  | (_ | '_/ _ \ || | '_ \) __| | | ' \)) _` / -_)| '_| 
   \___|_| \___/\_,_| .__/|_|   |_|_||_|\__,_\___||_|   
                    |_|                                 
        
        by : Synax
        github : synaxhelper
        telegram : synaxYYY
        telegram2 : synaxXXX
""")

#your webhook
hook = input("[-] Enter your webhook: ")
#number of threads
threads = int(input("[-] How many threads: "))

while True:
    if threading.active_count() <= threads:
        threading.Thread(target=groupfinder).start()
