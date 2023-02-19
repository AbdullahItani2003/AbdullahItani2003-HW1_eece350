#Your client should:
#- take as input the website IP you want to access
#- send the request to the proxy server
#- print a message with the request details and the exact time sent
#- receive the reply back from the proxy server and display it to the user with the exact
#time received
#- Calculate and display the total round-trip time and your physical (not VM) MAC address.
#Assignment will not be accepted without the MAC displayed. 

# Client
from socket import *
import time as t
import uuid 

x = str(input("Enter website IP: ")) # user input IP adress
c = socket(AF_INET,SOCK_STREAM) # creating the socket
port = 4269 # the port that server is on
host=gethostname() #used to get the hostname of the current system
IP = gethostbyname(host) # This function takes a string argument that specifies the domain name that you want to resolve,
# and it returns the corresponding IP address as a string. (basically getting the IP adress from client)
c.connect((IP,port)) # connect to server
send = "GET / HTTP/1.1\r\nHost: "+x+"\r\n\r\n" #sending request
# similar to the request in the powerpoint on moodle, but instead of yahoo, i put the IP adress
start = t.time() # starting time to measure later on the RTT
print(x," ",send,"time sent to server:",t.ctime()) #request details
c.send(send.encode()) # sending request
sr = c.recv(1024).decode() # reply from server, 1024 is number of bytes limiting amount of memory sent to server
print("The response from server is:",sr+" Received at:",t.ctime()) #request replies
end = t.time() 
RTT = round(end-start,4) # calculating tound trip time
c.close() # closing socket
print("RTT:",RTT,"seconds.")
print(uuid.getnode())#used geeksforgeeks for macadress method
