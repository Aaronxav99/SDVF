import pytest
from sdvf import AndroidDevice
from sdvf import DeviceInfo



def test_device1_uptime(device):
    output,error=device.run_command(
        ["shell","uptime"]     #information on how long the Android system has been running since its last boot
    ) 
    assert output is not None
    assert "load average" in output

def test_device_model(device):

    output, error = device.run_command(
        ["shell", "getprop", "ro.product.model"]
    )

    assert output is not None


def test_battery_status(device):

    output, error = device.run_command(
        ["shell", "dumpsys", "battery"]
    )

    assert output is not None
    assert "level" in output

def test_memory_info(device):

    output, error = device.run_command(
        ["shell", "cat", "/proc/meminfo"] #used to display detailed memory usage statistics from an Android device by accessing the Linux kernel's memory information file
    )

    assert output is not None
    assert "MemTotal" in output
    
def test_cpu_command(device):

    output, error = device.run_command(
        ["shell", "top", "-n", "1"]
    )

    assert output is not None  
    assert "CPU" in output or "Tasks" in output     

def test_get_device_info(device):
    info=device.get_device_info()
    

     # is it the right type?
    assert isinstance(info,DeviceInfo)    

    # are the fields actually populated?
    assert info.model != ""
    assert info.model != "unknown"
    assert info.android_version != ""
    assert info.build_fingerprint != ""

    print(f"\nDevice info: {info}")

@pytest.mark.parametrize("prop,expected",[
     ("ro.product.model",         ""),        # just check not empty
    ("ro.build.version.release", ""),        # just check not empty  
    ("ro.build.fingerprint",     "google"),  # should contain google
    ("ro.product.manufacturer",  ""),        #check if not empty

])

def test_device_properties(device,prop,expected):
    output,_=device.run_command(f"shell getprop {prop}".split())

    assert output is not None
    assert output.strip() != ""
    
    if expected:                              # only check if expected is not empty
        assert expected.lower() in output.lower()