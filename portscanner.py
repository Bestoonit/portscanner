import argparse
import socket
import time
import concurrent.futures

parser = argparse.ArgumentParser(description='Port scanner')

parser.add_argument('-t', '--target', type=str)
parser.add_argument('-p', '--number_of_ports', type=int)
args = parser.parse_args()
start = time.time()
range_of_ports = list(range(1, args.number_of_ports))

def portscanner(*range_of_ports):
    for port in range_of_ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        result = s.connect_ex((args.target, port))
        if result == 0:
            print(f' port {port} is open')
        else:
            pass

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(portscanner, range_of_ports)

end = time.time()

print(f'Total scan time in second: {int(end - start)}')
