# Proxy Server
#Your server should:
#- listen on a port of your own choice for incoming connections
#- parse the request to get the destination server IP address
#- print a message describing this request with the IP and exact time of the request
#- send the client's request to the destination server
#- print a message with exact time of the actual request
#- receive the response from the destination server
#- print a message that the response was received with the exact time
#- send the response back to the client
#- print a message that the response was sent with the exact time
#- If there was any error from the client side or from the server side, the proxy server
#should display a message and return an error message to the client 

from socket import * #python socket library
import time as t #we need to get the time of request
s = socket(AF_INET,SOCK_STREAM) # create the server socket 

#used examples on slides and pdf 

port = 4269 # ports 0-1023 are reserved, so i can use any port from 1024-49151, 49152-65535 are private 
host = gethostname() # used to get the hostname of the current system
addIP = gethostbyname(host) # This function takes a string argument that specifies the domain name that you want to resolve,
# and it returns the corresponding IP address as a string. (basically getting the IP adress from client)
s.bind((host,port)) # bind socket to IP and port
s.listen(1) # server awaiting TCP requests
while True:
    cc,addr = s.accept() # server waits on accept for incoming requests
    # then we create a new socket on return
    r = cc.recv(1024).decode() # reading bytes 
    temp = r # burner variable
    IP = temp.split()[4]  # getting IP address form  message its the fifth word 
    print("Received client's request, Your IP address is:",IP,"time:",t.ctime())   
    # For the exact time method I used geeksforgeeks
    d = socket(AF_INET,SOCK_STREAM) # creating the destination server
    try:
        d.connect((IP,80)) # port 80 is standard port for HTTP 
        print("Sending the client's request to the destination server at time:",t.ctime())#message
        d.send(r.encode()) # sending to the destination server

    except socket.error:
        err = "Error! unable to connect" #need to put error message in variable to send it to client and print it on server
        cc.send(err.encode()) #sending encoded message
        print(err)
         

    x = d.recv(1024).decode() #receiving response from site
    print("The response was received at time:",t.ctime())#the response
    cc.send(x.encode()) # sending encoded response to client
    print("The response is sent to the client at time:",t.ctime())#The response
    d.close() 
    s.close()  # closing sockets
