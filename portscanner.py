
import argparse
import socket
import time, datetime
import concurrent.futures
import pyfiglet

print(pyfiglet.figlet_format("Port scanner"))
print('-'*70)

parser = argparse.ArgumentParser(description='Port scanner')

parser.add_argument('-t', '--target', type=str)
parser.add_argument('-p', '--number_of_ports', type=int)
args = parser.parse_args()

fqdn = socket.getfqdn(args.target)
print(f' FQDN > {fqdn}  :  IP > {args.target}')
print('-'*70)
print('Open Ports')
print('- '* 7)
start = time.time()
range_of_ports = list(range(1, args.number_of_ports))
def portscanner(*range_of_ports):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for port in range_of_ports:
        s.settimeout(0.1)
        result = s.connect_ex((args.target, port))
        try:
            if result == 0:
                print(port, socket.getservbyport(port))
        except socket.error:
            print(port)
            continue
      
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(portscanner, range_of_ports)

end = time.time()
time_took = str(end-start)
x = slice(0, 4)

print(f'\nTime took in second: {time_took[x]}')
print('-'*70)
print('<', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), '>\n')
