import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from device_bridge import DeviceBridge


def test_status_default():
    bridge = DeviceBridge("test")
    assert bridge.get_status() == "disconnected"

from device_bridge import DeviceBridge

def test_device_intializes():
    bridge=DeviceBridge("ADBD")
    assert bridge.serial=="ADBD"
    assert bridge.connected==False

def test_status_default():
    bridge=DeviceBridge("test")
    assert bridge.get_status()=="disconnected"    