import threading

import time

def task(name):
    for i in range(3):
        print(f'{name}running{i}')
        time.sleep(1)

t1 = threading.Thread(target=task,args=("Thread1",))
t2 = threading.Thread(target=task,args=("Thread2",))

t1.start()
t2.start()

t1.join()
t2.join()