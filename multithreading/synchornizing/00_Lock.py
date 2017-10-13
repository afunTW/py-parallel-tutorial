"""
Securely accessing shared variable in different thread

threading.Lock() only have two method:
    using acquire() to lock the state and
    using release() to unlock the state

if you call release() in unlock state, it raise RunTimeError

在不同的 thread 之間透過 Lock 的實作可以安全的存取同一個變數
實作內容僅僅只是透過 acquire 上鎖, release 解鎖
以此保證目前只有當前的 thread 可以操作
"""
import threading
import time

lock = threading.Lock()
shared_variable = 0

def add_one():
    global shared_variable
    lock.acquire()
    shared_variable += 1
    print('shared_variable = {} in thread {}'.format(shared_variable, threading.current_thread()))
    print('- {} sleep 1 sec'.format(add_one.__name__))
    time.sleep(1)
    print('- {} awake'.format(add_one.__name__))
    lock.release()

def add_two():
    global shared_variable
    lock.acquire()
    shared_variable += 2
    print('shared_variable = {} in thread {}'.format(shared_variable, threading.current_thread()))
    lock.release()

threads = []
for func in [add_one, add_two]:
    print('Ready to running {}'.format(func))
    threads.append(threading.Thread(target=func))
    threads[-1].start()

# wait for thread to complete before moving on with the main script
for thread in threads:
    thread.join()

print()
print('Thread {} - After thread.join()'.format(threading.current_thread()))
print('final shared_variable = {}'.format(shared_variable))
