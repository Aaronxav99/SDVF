import subprocess
from dataclasses import dataclass

@dataclass
class DeviceInfo:
    model:str
    android_version:str
    build_fingerprint:str


class DeviceBridge:

    def __init__(self,serial:str):
        '''
        initialize device serial number
        '''
        self.serial=serial
        self.connected=False

    def connect(self):
        result=subprocess.run(
            ["adb","devices"],
            capture_output=True,
            text=True
        )

        if self.serial in result.stdout:
            self.connected=True
            print(f"{self.serial} is connected")
        else:
            self.connected=False
            print(f"{self.serial} not connected")      
            print(f"available devices: \n {result.stdout}")
    def disconnect(self):
        self.connected=False
        print(f"{self.serial} is diconnected")

    def get_status(self):
        return "connected" if self.connected else "disconnected"  


    def run_command(self,command):
        if not self.connected:
            raise RuntimeError(f"{self.serial} not connected try connect()")
        try:
            result = subprocess.run(
                ["adb", "-s", self.serial] + command,
                capture_output=True,
                text=True,
                timeout=10  # absurdly small, forces timeout
            )
            result.check_returncode()  # raises if adb errored
            return result.stdout, result.stderr
        except subprocess.TimeoutExpired:
            return None, "Command Timeout out"  
        except subprocess.CalledProcessError as e:
            return None,f"adb error {e}"  
        
    def get_device_info(self) -> DeviceInfo  :
         model, _ = self.run_command("shell getprop ro.product.model".split())
         android_version, _ = self.run_command("shell getprop ro.build.version.release".split())
         build_fingerprint, _ = self.run_command("shell getprop ro.build.fingerprint".split())
         return DeviceInfo(
            model=model.strip() if model else "unknown",
            android_version=android_version.strip() if android_version else "unknown",
            build_fingerprint=build_fingerprint.strip() if build_fingerprint else "unknown"
        )
         
    
        
#             
# d = DeviceBridge("emulator-5554")  # replace with your device ID from adb devices
# d.connect()
# # output, error = d.run_command("shell getprop ro.build.fingerprin")
# # print(f"Device model: {output} and {error}")
# d.get_device_info()





        
        
    
    


         
