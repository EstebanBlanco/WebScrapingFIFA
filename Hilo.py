import threading
import Extractor
import time


class Hilo(threading.Thread):
    quit = False

    def __init__(self):
        super().__init__()
        self.cond = threading.Condition()

    def delay(self, seconds):
        deadline = time.monotonic() + seconds
        with self.cond:
            if self.quit:
                raise SystemExit()
            if time.monotonic() >= deadline:
                return
            self.cond.wait(time.monotonic() - deadline)

    def run(self):
        while not self.quit:
            Extractor.ExtractData()
            self.delay(300000)

    def terminate(self):
        with self.cond:
            self.quit = True
            self.cond.notify_all()
        self.join()