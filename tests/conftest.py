import pytest
import sys,os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from sdvf import AndroidDevice
from sdvf import LogCollector



@pytest.fixture(scope ="session")
def device():
    bridge=AndroidDevice("emulator-5554")
    bridge.connect()
    logger = LogCollector("emulator-5554")
    logger.start()

    yield bridge

    logger.stop()
    bridge.disconnect()