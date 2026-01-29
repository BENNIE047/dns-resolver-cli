import socket

web=input("enter the name of the website..eg google.com: ")
ip=socket.gethostbyname(web)
print(f"IP ADDRESS IS : {ip}")