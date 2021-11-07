from app import *
import pty
import os
import subprocess
import select
import termios
import struct
import fcntl
import shlex
import psutil

def create_new_shell():
    
    if app.config["child_pid"]:
        # already started child process, don't start another
        return

    # create child process attached to a pty we can read from and write to
    (child_pid, fd) = pty.fork()
    if child_pid == 0:
        # this is the child process fork.
        # anything printed here will show up in the pty, including the output
        # of this subprocess
        subprocess.run(app.config["cmd"])
    else:
        # this is the parent process fork.
        # store child fd and pid
        app.config["fd"] = fd
        app.config["child_pid"] = child_pid
        set_winsize(fd, 50, 50)
        cmd = " ".join(shlex.quote(c) for c in app.config["cmd"])
        # logging/print statements must go after this because... I have no idea why
        # but if they come before the background task never starts
        socketio.start_background_task(target=read_and_forward_pty_output)
    

def set_winsize(fd, row, col, xpix=0, ypix=0):
    winsize = struct.pack("HHHH", row, col, xpix, ypix)
    fcntl.ioctl(fd, termios.TIOCSWINSZ, winsize)


def read_and_forward_pty_output():
    max_read_bytes = 1024 * 20
    while True:
        socketio.sleep(0.01)
        if app.config["fd"]:
            timeout_sec = 0
            (data_ready, _, _) = select.select([app.config["fd"]], [], [], timeout_sec)
            if data_ready:
                try:
                    output = os.read(app.config["fd"], max_read_bytes).decode()
                except Exception as ex:
                    print(ex,"\n\n\n\n\n\n\n\n\n\n")
                    
                    app.config["fd"] = None
                    app.config["child_pid"] =  None
                    create_new_shell()
                socketio.emit("pty-output", {"output": output}, namespace="/pty")


@socketio.on("pty-input", namespace="/pty")
def pty_input(data):
    """write to the child pty. The pty sees this as if you are typing in a real
    terminal.
    """
    if(psutil.Process(app.config["child_pid"]).children(recursive=True) == []):
        app.config["fd"] = None
        app.config["child_pid"] =  None
        create_new_shell()
    if app.config["fd"]:
        os.write(app.config["fd"], data["input"].encode())


@socketio.on("resize", namespace="/pty")
def resize(data):
    if app.config["fd"]:
        set_winsize(app.config["fd"], data["rows"], data["cols"])


@socketio.on("connect", namespace="/pty")
def connect():
    """new client connected"""
    create_new_shell()