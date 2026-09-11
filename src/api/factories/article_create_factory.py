import time


def wait_until(action, condition, timeout=2.0, interval=0.1):
    deadline = time.monotonic() + timeout
    while True:
        result = action()

        if condition(result):
            return result

        if time.monotonic() >= deadline:
            raise AssertionError(f"Condition not met within {timeout}s")
        time.sleep(interval)
