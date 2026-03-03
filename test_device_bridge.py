from device_bridge import DeviceBridge

def test_device_intializes():
    bridge=DeviceBridge("ADBD")
    assert bridge.serial=="ADBD"
    assert bridge.connected==False