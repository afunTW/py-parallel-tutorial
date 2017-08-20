"""
Barriers can be used by different threads to wait for each other,
thread pass a barrier by calling wait()
and it will block until all threads have made that call

Barriers 用於不同 thread 之間需要互相等待的時候
呼叫 wait() 的時候該 thread 會 block 住
等到所有 thread 都呼叫 wait() 之後才會解鎖
"""
import random
import threading
import time

num_of_barrier = 4

# number of thread will need
barrier = threading.Barrier(num_of_barrier)
names = ['Amber', 'Bob', 'Cathy', 'Daniel']

def player():
    name = names.pop()
    time.sleep(random.randrange(2, 5))
    print('Thread {} - {} reached the barrier at {}'.format(threading.current_thread(), name, time.ctime()))
    barrier.wait()

threads = []
print('Race start...')

for i in range(num_of_barrier):
    threads.append(threading.Thread(target=player))
    threads[-1].start()

for thread in threads:
    thread.join()

print()
print('Thread {} - After thread.join()'.format(threading.current_thread()))
print('Race over')