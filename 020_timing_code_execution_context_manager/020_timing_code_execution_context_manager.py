import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.interval = self.end - self.start
        print(f"Time taken: {self.interval} seconds")

with Timer():
    # Code to be timed
    time.sleep(2)
