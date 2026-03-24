import subprocess
import threading
import time
from dataclasses import dataclass,field
from typing import List


@dataclass
class DataPoint:
    timestamp: float
    cpu_percent: float
    thermal_temp:float =None

class Profiler:
    def __init__(self,serial,interval=1):
        self.serial=serial
        self.interval=interval
        self.running=False
        self.data:List[DataPoint]=[]
        self.thread=None

    def _get_cpu(self):
        try:
            result = subprocess.run(
                ["adb", "-s", self.serial, "shell", "top", "-n", "1", "-b"],
                capture_output=True, text=True, timeout=5
            )
            for line in result.stdout.splitlines():
                if "%cpu" in line.lower():
                    import re
                    match = re.search(r'(\d+)%idle', line)
                    if match:
                        idle = float(match.group(1))
                        cores = int(line.split('%cpu')[0].strip()) // 100
                        cores = max(cores, 1)
                        used = 100 - (idle / cores)
                        return round(used, 1)
        except Exception:
            pass
        return 0.0


    def _get_thermal(self):
        try:
            result = subprocess.run(
                ["adb", "-s", self.serial, "shell",
                 "cat", "/sys/class/thermal/thermal_zone0/temp"],
                capture_output=True, text=True, timeout=5
            )
            temp = float(result.stdout.strip())
            return temp / 1000.0
        except Exception:
            pass
        return None

    def _capture_loop(self):
        while self.running:
            point=DataPoint(
                timestamp=time.time(),
                cpu_percent=self._get_cpu(),
                thermal_temp=self._get_thermal()

            )
            self.data.append(point)
            time.sleep(self.interval)


    def start(self):
        self.running = True
        self.data = []
        self.thread = threading.Thread(target=self._capture_loop)
        self.thread.daemon = True
        self.thread.start()
        print(f"Profiler started — sampling every {self.interval}s")        
    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join(timeout=5)
        print(f"Profiler stopped — {len(self.data)} data points collected")
    def summary(self):
        if not self.data:
            print("No data collected")
            return
        cpu_values = [d.cpu_percent for d in self.data]
        temp_values = [d.thermal_temp for d in self.data if d.thermal_temp is not None]

        print(f"CPU  — avg: {sum(cpu_values)/len(cpu_values):.1f}%  "
            f"max: {max(cpu_values):.1f}%")

        if temp_values:
            print(f"Temp — avg: {sum(temp_values)/len(temp_values):.1f}°C  "
                f"max: {max(temp_values):.1f}°C")
        else:
            print("Temp — not available (emulator or no thermal sensor)")


if __name__ == "__main__":
    p = Profiler("emulator-5554", interval=1)
    p.start()
    print("Profiling for 5 seconds...")
    time.sleep(5)
    p.stop()
    p.summary()




        