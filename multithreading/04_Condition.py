"""
Condition is simply more advanced Events object
It's communicator and can be used to notify() other thread

Condition 可以視為進階版的 Events, 多了 notify() 這個通知功能
在做事之前需要透過 acquire 與 release 來確保接下來不會被干擾
做完事情後可以透過 notify 通知其他 thread 資源可以存取了
接著最後才是透過 release 來釋放當前上鎖的狀態並真正釋放資源
"""
import random
import threading
import time

condition = threading.Condition()

container = []

def producer(container, nitems):
    for i in range(nitems):
        sleep_time = random.randrange(2, 5)
        time.sleep(sleep_time)
        # print('Thread {} - Producer sleep {}'.format(threading.current_thread(), sleep_time))

        # safely do things by lock the state
        condition.acquire()

        # put the item into container for consumption
        num = random.randint(1, 10)
        container.append(num)
        print('Thread {} - Producer produced: {}'.format(threading.current_thread(), num))
        print('Thread {} - Producer Container: {}'.format(threading.current_thread(), container))

        # notisfies the consumer about the availability
        condition.notify()

        # resource avaliable
        condition.release()


def consumer(container, nitems):
    for i in range(nitems):
        condition.acquire()

        # block until an item is avaliable for consumption
        condition.wait()
        print('Thread {} - Consumer acquire {} at {}'.format(threading.current_thread(), container.pop(), time.ctime()))
        print('Thread {} - Consumer Container: {}'.format(threading.current_thread(), container))

        condition.release()

threads = []
nloops = random.randrange(3, 6)
print('loops {} times'.format(nloops))

for func in [producer, consumer]:
    threads.append(threading.Thread(target=func, args=(container, nloops)))
    threads[-1].start()

for thread in threads:
    # wait for the threads to complete before moving on with the main script
    thread.join()

print()
print('Thread {} - After thread.join()'.format(threading.current_thread()))
print('All done')