import threading
import time
import queue
from tkinter import *

ws = Tk()

ws.geometry("200x200")

comque = queue.Queue()


def timeThread():
    prestime = 0
    while 1:

        comque.put(prestime)

        try:
            ws.event_generate('<<TimeChanged>>', when='tail')

        except TclError:
            break

        time.sleep(1)
        prestime += 1


clcvar = IntVar()
Label(ws, textvariable=clcvar, width=9).pack(pady=10)


def timeChanged(event):
    clcvar.set(comque.get())


ws.bind('<<TimeChanged>>', timeChanged)

Thr = threading.Thread(target=timeThread)
Thr.start()

ws.mainloop()