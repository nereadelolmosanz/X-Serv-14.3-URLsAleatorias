#!/usr/bin/python

"""
Simple HTTP Server version 2: reuses the port, so it can be
restarted right after it has been killed. Accepts connects from
the outside world, by binding to the primary interface of the host.

Jesus M. Gonzalez-Barahona and Gregorio Robles
{jgb, grex} @ gsyc.es
TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
"""

import socket

# Create a TCP objet socket and bind it to a port
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Let the port be reused if no process is actually using it
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind to the address corresponding to the main name of the host
mySocket.bind((socket.gethostname(), 1235))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an almost-infinite loop; the loop can be stopped with Ctrl+C)

try:
    while True:
        print ('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print ('Request received:')
        print (recvSocket.recv(2048))
        print ('Answering back...')

# Apartado 1: Elemento de imagen
        recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                        "<html><body><h1> IMAGEN </h1>" +
                        "<p>And in particular hello to you, " +
                        str(address[0]) +
                        "</p>" +
						'<img src="smiley.gif" alt="Smiley face" height="42" width="42">' +
                        "</body></html>" +
                        "\r\n")


# Apartado 2: Mensaje de error
#        recvSocket.send("HTTP/1.1 404 NOT FOUND \r\n\r\n" +
#                        "<html><body><h1>Oops!\n</h1>" +
#                        "<p>Error 404 NOT FOUND, " +
#                        str(address[0]) +
#                        "</p>" +
#                        "</body></html>" +
#                        "\r\n")


# Apartado 3: Redireccion a http://gsyc.es/
#        recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
#                        "<html><body><h1> IMAGEN </h1>" +
#                        "<p>And in particular hello to you, " +
#                        str(address[0]) +
#                       "</p>" +
#                        "</body></html>" +
#                        "\r\n")

        recvSocket.close()
except KeyboardInterrupt:
    print ("Closing binded socket")
    mySocket.close()
