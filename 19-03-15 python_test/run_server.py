#
# [name] run_server.py
#
# Written by Yoshikazu NAKAJIMA
#

from socket import *
import sys
import subprocess

HOST = ''
PORT = 5008
CLIENTPORT = 5009

s = socket(AF_INET, SOCK_DGRAM)
s.bind((HOST, PORT))

while True:
    msg, address = s.recvfrom(8192)

    print("message:", msg, "from", address)

    if msg == b".":
        print("Server daemon is closed")
        break

    if msg == b"raspi_reboot":
        print("Server is rebooting")
        command = ["reboot"]
        res = subprocess.call(command)
        print(res)
        break

    if msg == b"raspi_shutdown":
        print("Server is getting down")
        command = ['sudo', 'shutdown', '-h', 'now']
        res = subprocess.call(command)
        print(res)
        break

    if msg == b"raspi_resreq":
        print("Response is required")
        clientsocket = socket()
        clientsocket.connect((address, CLIENTPORT))
        clientsocket.send(b'I am alive')

s.close()
sys.exit()
