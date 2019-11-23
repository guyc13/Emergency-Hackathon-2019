
import tkinter as tk
from tkinter import ttk
import datetime
import winsound
from serial import Serial


def read_from_serial(ser):
    count = 1
    # while True:
    for line in ser.read():
        # print(str(count) + str(': ') + chr(line) )
        count = count+1
        return chr(line)


def connect_to_serial(interface):
    ser = Serial(port=interface, baudrate=9600)
    print("connected to: " + ser.portstr)
    return ser


def close_connection(ser):
    ser.close()


def write_to_serial(ser,command):
    ser.write(command)


def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("ALERT!!!")
    label = tk.Label(popup, background='grey', anchor='s', text=str(datetime.datetime.now().ctime())+'\n'
                                  + msg, font=NORM_FONT, width=50, fg='orange')
    label.pack(side="top", fill="x", pady=100)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()



# if __name__ == '__main__':
#     ser=connect_to_serial(interface)
#     read_from_serial(ser)
#     # winsound.Beep(freq, duration)
#     # popupmsg(alerts["A"])
#     # ser.close()
#

