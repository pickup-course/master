#cm_timer.py

import time
from contextlib import contextmanager

class cm_timer_1:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, type, value, traceback):
        self.end = time.time()
        print(f"time: {self.end - self.start:.2f}")

@contextmanager
def cm_timer_2():
    start = time.time()
    yield
    end = time.time()
    print(f"time: {end - start:.2f}")

if __name__ == '__main__':
    with cm_timer_1():
        time.sleep(5.5)
    with cm_timer_2():
        time.sleep(5.5)

