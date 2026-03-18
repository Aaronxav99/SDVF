import time


def timer(func):
    def wrapper(*args, **kwargs):
        start=time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.3f} seconds")
        return result
    return wrapper
@timer
def slow_function():
    time.sleep(2)

slow_function()
# slow_function took 2.001 seconds



def retry(times=3,delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1,times+1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt} failed :{e}")
                    if attempt < times:
                        time.sleep(delay)
                    else:
                        print(f"All {times} attempts failed")
                        raise
        return wrapper
    return decorator                
counter = {"count": 0}

@retry(times=3, delay=1)
def flaky_adb_command():
    counter["count"] += 1
    if counter["count"] < 3:
        raise RuntimeError("ADB connection dropped")
    print(f"success on attempt {counter['count']}")

flaky_adb_command()