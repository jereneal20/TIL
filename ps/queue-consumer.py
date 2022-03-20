import queue
import random
import threading
import time


class Worker(threading.Thread):
    def __init__(self, queue, lock):
        super().__init__()
        self.queue = queue
        self.lock = lock

    def run(self):
        while True:
            try:
                job = self.queue.get(block=True)
                self.work(job)
                if self.lock.locked():
                    print(self.name + " Release")
                try:
                    self.lock.release()
                except RuntimeError:
                    pass

            except queue.Empty:
                return
            self.queue.task_done()

    def work(self, val):
        time.sleep(random.random())
        print(self.name + " " + str(val) + ": " + str(val*val))
        return val*val


lock = threading.Lock()
cond = threading.Condition(lock)

q = queue.Queue()
w = []
for _ in range(3):
    w.append(Worker(q, lock))
    w[-1].setDaemon(True)
    w[-1].start()

for i in range(10):
    q.put_nowait(i)
q.put_nowait(3)

lock.acquire(blocking=True)
lock.acquire(blocking=True)
print("Lock released")
q.join()

print("Everything is joined")
