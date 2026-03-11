import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from device_bridge import AndroidDevice


def test_status_default():
    bridge = AndroidDevice("test")
    assert bridge.get_status() == "disconnected"



def test_device_intializes():
    bridge=AndroidDevice("ADBD")
    assert bridge.serial=="ADBD"
    assert bridge.connected==False

    