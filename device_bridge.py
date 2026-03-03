class DeviceBridge:

    def __init__(self,serial:str):
        '''
        initialize device serial number
        '''
        self.serial=serial
        self.connected=False

    def connect(self):
        '''
        connect to adb devices
        '''
        raise NotImplementedError("connect to adb not implemented")
        
    def get_logs(self):
         '''
         getting logs from device
         '''
         raise NotImplementedError("get logs is not implemeted")
    


         
