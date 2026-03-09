import subprocess
import time
import sys,os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
class LogCollector:
    def __init__(self,serial):
        self.serial=serial
        self.process=None


    def start(self,filename="logs/logcat.txt"):
        self.process=subprocess.Popen(
            ["adb","-s",self.serial,"logcat"],
            stdout=open(filename,"w"),
            stderr=subprocess.PIPE,
            text=True
        )    

    def stop(self):
        if self.process:
            self.process.terminate()