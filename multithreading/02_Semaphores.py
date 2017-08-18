"""
Semaphores is simply advanced counter and
it will block only after number of threads have acquireed it
    using acquire() to count - 1
    using release() to count + 1

BoundedSemaphore raise an error if release() increase counter beyond the maximize size
Semaphore not bounded

demo with simply producer and consumer problem

Semaphore 可以是做就是簡單的計數器
呼叫一次 acquire 就會 - 1; 呼叫一次 release 就會 + 1
通常為了限制存取資源會使用 Semaphore, e.g. Server 限制一次只會有 10 個 client 連線
另外為了預防人為錯誤, 會使用 BoundedSemaphore 而不是 Semaphore
"""
import random
import threading
import time

max_items = random.randrange(1,10)

# consider this container capacity is number of max_items
container = threading.BoundedSemaphore(max_items)

def producer(nloops):
    print('producer have {} loops'.format(nloops))
    for i in range(nloops):
        time.sleep(random.randrange(2, 5))
        print(time.ctime(), end=": ")

        try:
            # counter + 1
            container.release()
            print('Producer {}: Produced items'.format(threading.current_thread))
        except ValueError as e:
            print('Producer {}: Full of items, skipping'.format(threading.current_thread))

def consumer(nloops):
    print('consumer have {} loops'.format(nloops))
    for i in range(nloops):
        time.sleep(random.randrange(2, 5))
        print(time.ctime(), end=": ")

        # disable the blocking behavior by passing block flag
        # counter -1
        if container.acquire(False):
            print('Consumer {}: Consumed items'.format(threading.current_thread))
        else:
            print('Consumer{}: Empty, skipping'.format(threading.current_thread))

threads = []
nloops = random.randrange(3, 6)
print('Start with {} items'.format(max_items))

threads.append(threading.Thread(target=producer, args=(nloops,)))
threads.append(threading.Thread(target=consumer, args=(random.randrange(nloops, nloops+max_items+2), )))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print('All done')