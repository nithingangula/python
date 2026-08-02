import threading
import time

class MyThread(threading.Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        for i in range(3):
            print(f"{self.name} is running...")
            time.sleep(1)

t1 = MyThread("Thread-A")
t2 = MyThread("Thread-B")

t1.start()
t2.start()

t1.join()
t2.join()

print("Finished")