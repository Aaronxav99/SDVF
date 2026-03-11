import pytest
import sys,os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from device_bridge import AndroidDevice
from log_collector import LogCollector



@pytest.fixture
def device():
    bridge=AndroidDevice("emulator-5554")
    bridge.connect()
    logger = LogCollector("emulator-5554")
    logger.start()

    yield bridge

    logger.stop()
    bridge.disconnect()