import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from sdvf import AndroidDevice


def test_status_default():
    bridge = AndroidDevice("test")
    assert bridge.get_status() == "disconnected"



def test_device_intializes():
    bridge=AndroidDevice("ADBD")
    assert bridge.serial=="ADBD"
    assert bridge.connected==False


def test_profiler_is_collecting(profiler):
    import time
    time.sleep(3)  # let it collect a few points
    assert len(profiler.data) > 0, "Profiler collected no data"
    assert any(d.cpu_percent >= 0.0 for d in profiler.data), "No CPU readings"
    print(f"\nProfiler has {len(profiler.data)} points so far")    

    