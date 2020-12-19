import socket

import network

ssid = 'MicroPython-AP'
password = '123456789'

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password)

while ap.active() == False:
    print('Attompting AP activation')


print('AP activation successful')
print(ap.ifconfig())

def web_page():
    html = """<html><head><meta name="viewport" content="width=device-width, initial-scale=1"></head>
    <body><h1>Hello, World!</h1></body></html>"""
    return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
#     request = conn.recv(1024)
#     print('Content = %s' % str(request))
#     response = web_page()
#     conn.send(response)
#     conn.close()
