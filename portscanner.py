#!/usr/bin/python3
import socket
target = input("Enter a target IP: ")
port = int(input("Enter a port number: "))
def portscanner(port):
	try:	
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((target, port))
		print("port is open")
	except:
		print("port is closed")

portscanner(port)
