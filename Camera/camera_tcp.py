import socket
import sys
import time


def camera_tcp_process(pipe):
    p_output, p_input = pipe

    # TODO: Create a config file for these values
    TCP_IP="172.16.10.1"
    TCP_PORT=8888 
    BUFFER_SIZE = 4096 

    try:
        TCP_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        TCP_sock.settimeout(5.0)
        TCP_sock.connect((TCP_IP,TCP_PORT))

        # TODO: Make heartbeat configurable for different drones
        heartbeat=bytearray([0x0,0x1,0x2,0x3,0x4,0x5,0x6,0x7,0x8,0x9,0x28,0x28])
        TCP_sock.send(heartbeat)
    except:
        print("Failed")
        exit(-1)

    t0=time.time()
    while(1):
        try:
            data = TCP_sock.recv(BUFFER_SIZE)
            #sys.stdout.buffer.write(data)
            p_input.send(data)
        except ValueError:
            print(ValueError)
            continue
        if time.time()-t0>1:
            t0=time.time()
            try:
                TCP_sock.send(heartbeat)
            except:
                exit(-1)
    TCP_sock.close()