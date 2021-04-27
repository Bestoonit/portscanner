import argparse
import socket

parser = argparse.ArgumentParser(description='Port scanner')
parser.add_argument('-t', '--target', type=str, help='target ip')

arge = parser.parse_args()

for port in range(1, 1000):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(0.1)
	result = s.connect_ex((arge.target, port))
	if result == 0:
		print(f' port {port} is open')
	else:
		pass


