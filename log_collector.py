import subprocess
import time
import sys,os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
class LogCollector:
    def __init__(self,serial,filename=r"D:\upskilling\tasks\month_1\week_1\SDVF\logs\logcat.txt"):
        self.serial=serial
        self.process=None
        self.filename=filename
        # self.log_file=None


    def start(self):
        self.log_file=open(self.filename,"w")
        self.process=subprocess.Popen(
            ["adb","-s",self.serial,"logcat"],
            stdout=self.log_file,
            stderr=subprocess.PIPE,  #subprocess.PIPE means — "capture this stream and give it to me in Python so I can read
            text=True
        )   
        print(f"logcat started->{self.filename}") 

    def stop(self):
        if self.process:
            self.process.terminate()
            self.process=None
            print(f"logcat is stopped")
        if self.log_file:
            self.log_file.close()    
            self.log_file=None

    #context manager
    def __enter__(self):
        self.start()
        return self
    def __exit__(self, exc_type, exc, tb):
        self.stop()
        return False   # dont supress the exceptions 

    def parse_errors(self):
        with open(self.filename,"r") as f:
            for line in f:
                if "ERROR" in line or "CRITICAL" in line or "FATAL" in line:
                    yield line.strip() 
    

if __name__ == "__main__":
    import time
    with LogCollector("emulator-5554") as collector:
        print("collecting logs for 5 seconds...")
        time.sleep(5)
   

    print("\n--- Errors Found ---")
    error_count = 0
    for error in collector.parse_errors():
        print(error)
        error_count += 1
    
    print(f"\nTotal errors found: {error_count}")

    print("done — check logs/logcat.txt")
            