"""
Securely accessing shared variable in different thread

threading.Lock() only have two method:
    using acquire() to lock the state and
    using release() to unlock the state

if you call release() in unlock state, it raise RunTimeError
"""
import threading


lock = threading.Lock()
shared_variable = 0

def add_one():
    global shared_variable
    lock.acquire()
    shared_variable += 1
    print('shared_variable = {} in thread {}'.format(shared_variable, threading.current_thread))
    lock.release()

def add_two():
    global shared_variable
    lock.acquire()
    shared_variable += 2
    print('shared_variable = {} in thread {}'.format(shared_variable, threading.current_thread))
    lock.release()

threads = []
for func in [add_one, add_two]:
    threads.append(threading.Thread(target=func))
    threads[-1].start()

# wait for thread to complete before moving on with the main script
for thread in threads:
    thread.join()

print('final shared_variable={}'.format(shared_variable))