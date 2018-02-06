import logging.handlers

import subprocess
from threading import Thread

import datetime
from time import sleep

from utilities_file import touch_file, get_modification_date

log = logging.getLogger("Schrodinger_Watchdog")
log.setLevel(logging.DEBUG)

handler = logging.handlers.SysLogHandler('/dev/log')

formatter = logging.Formatter('%(module)s.%(funcName)s: %(message)s')
handler.setFormatter(formatter)

log.addHandler(handler)


class Watchdog:
    """Test"""
    path_DeviceManager  = "/home/pi/Schrodinger_Watchdog/watchdog_DeviceManager"
    path_XBoxController = "/home/pi/Schrodinger_Watchdog/watchdog_XBoxController"

    def __init__(self):

        self.receive_events_thread = Thread(target=self._receive_events_thread)
        self.receive_events_thread.daemon = True
        self.receive_events_thread.start()

        print("Watchdog started")
        log.info('Watchdog started')

        self.startPrograms()

    def loop(self):
        log.debug('Watchdog timer elapsed')

        now = datetime.datetime.utcnow()
        log.debug("Current time: " + str(now))

        # touch_file(self.path_DeviceManager)
        # touch_file(self.path_XBoxController)

        modification_DeviceManager = get_modification_date(self.path_DeviceManager)
        modification_XBoxController = get_modification_date(self.path_XBoxController)

        log.debug("Device manager was modified @: " + str(modification_DeviceManager))
        log.debug("XBoxController was modified @: " + str(modification_XBoxController))

        diff_XBoxController = now - modification_XBoxController
        diff_DeviceManager  = now - modification_DeviceManager


        log.debug("DeviceManager diff: " + str(diff_DeviceManager))
        log.debug("XBoxController diff: " + str(diff_XBoxController))


    def _receive_events_thread(self):
        log.debug("Watchdog thread started")

    def startPrograms(self):

        # test touch
        # touch_file(self.path_DeviceManager)
        # touch_file(self.path_XBoxController)

        log.debug("Starting gpsd...")
        subprocess.run(["sudo", "/usr/sbin/gpsd", "/dev/ttyUSB0", "-F", "/var/run/gpsd.sock", "-n"])

        log.debug("Starting DeviceManager...")
        subprocess.run(["sudo", "python3", "/home/pi/Schrodinger/DeviceManager.py"])

        log.debug("Starting XBoxController...")
        subprocess.run(["sudo", "python3", "/home/pi/Socket_IO_Client/client.py"])

if __name__ == "__main__":
    watchdog = Watchdog()

    while 1:
        watchdog.loop()
        sleep(5)

