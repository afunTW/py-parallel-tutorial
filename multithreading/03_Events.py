"""
Events is a simple communicator based on internal flag
thread method
    - set(): set flag
    - clear(): clear the flag
    - wait(): block, until the internal flag set()

Events 可以視為 thread 之間的溝通管道
有 set(), clear(), wait() 三種溝通方式
主要透過 wait 等待 set, 透過 clear 之後進行下一輪 wait-set
"""
import random
import threading
import time

event = threading.Event()

def waiter(event, nloops):
    for i in range(nloops):
        print('Thread {}: Waiting for flag to be set - {} iteration'.format(threading.current_thread(), i+1))

        # block until flag become true
        event.wait()

        print('Thread {}: Wait complete - {}'.format(threading.current_thread(), time.ctime()))
        event.clear()
        print()

def setter(event, nloops):
    for i in range(nloops):
        sleep_time = random.randrange(2, 5)
        time.sleep(sleep_time)
        print('Thread {}: sleep {} sec - {}'.format(threading.current_thread() , sleep_time, time.ctime()))
        event.set()

threads = []
nloopss = random.randrange(3, 6)
print('loops {} times'.format(nloopss))

threads.append(threading.Thread(target=waiter, args=(event, nloopss)))
threads[-1].start()
threads.append(threading.Thread(target=setter, args=(event, nloopss)))
threads[-1].start()

# wait until all thread done and go through the main thread
for thread in threads:
    thread.join()

print('Thread {} - After thread.join()'.format(threading.current_thread()))
print('All done')
