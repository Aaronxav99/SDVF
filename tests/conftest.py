import pytest
import sys,os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from sdvf import AndroidDevice
from sdvf import LogCollector
from sdvf.profiler import Profiler




@pytest.fixture(scope="session", autouse=True)
def logger():
    log = LogCollector("emulator-5554")
    log.start()
    yield log
    log.stop()

@pytest.fixture(scope="session")
def device():
    bridge = AndroidDevice("emulator-5554")
    bridge.connect()
    yield bridge
    bridge.disconnect()


@pytest.fixture(scope="session", autouse=True)
def profiler():
    p = Profiler("emulator-5554", interval=1)
    p.start()
    yield p
    p.stop()
    p.summary()    