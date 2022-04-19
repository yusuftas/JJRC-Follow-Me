from multiprocessing import Process, Pipe

import subprocess as sp
import os
import signal
import sys
from time import sleep

from Camera.camera_tcp import camera_tcp_process
from ui.mainwindow import camera_reader_proc


if __name__ == '__main__': 

    p_output, p_input = Pipe()

    print(p_output.fileno())
    print(p_input.fileno())

    reader_fd = os.fdopen(p_output.fileno(), 'r')
    #writer_fd = os.fdopen(p_input.fileno(), 'w')

    tcp_writer_proc = Process(target = camera_tcp_process, args=((p_output, p_input),))

    sleep(20)

    camera_proc     = Process(target = camera_reader_proc, args=(reader_fd,))

    camera_proc.daemon = True
    camera_proc.start()     # Launch the reader process


    camera_proc.join()


# # TODO: Make a better design for these processes
# tcp_proc = sp.Popen([".\\camera\\camera_tcp.py"], shell=True, stdout=sp.PIPE, bufsize=10 ** 8, creationflags=sp.CREATE_NEW_PROCESS_GROUP)
# main_proc = sp.Popen([".\\ui\\mainwindow.py"],  shell=True, stdin=tcp_proc.stdout,  creationflags=sp.CREATE_NEW_PROCESS_GROUP)
# main_proc.wait()

# tcp_proc.send_signal(signal.CTRL_BREAK_EVENT)
# tcp_proc.kill()