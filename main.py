from communication import *
from Alert import *
import serial
from Banner import banner

interface="com7"
if __name__ == '__main__':
    banner()
    try:
        ser = connect_to_serial(interface)
        while True:
            sensor = read_from_serial(ser)
            print(sensor)
            alert_sound()
            msg=alerts[sensor]

            popupmsg(msg,sensor)

    except serial.SerialException:
        print("connection refused")

