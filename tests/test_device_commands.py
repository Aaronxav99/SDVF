import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from sdvf import AndroidDevice


def test_status_default():
    bridge = AndroidDevice("test")
    assert bridge.get_status() == "disconnected"

def test_getprop(device):

    output, error = device.run_command(
        ["shell", "getprop", "ro.build.fingerprint"]
    )
    time.sleep(5)

    assert output is not None