"""
Securely accessing shared variable in different thread
"""
import threading


lock = threading.Lock()
shared_variable = 0

def add_one():
    global shared_variable
    lock.acquire()
    print('Current thread: {}'.format(threading.current_thread()))
    shared_variable += 1
    lock.release()

def add_two():
    global shared_variable
    lock.acquire()
    print('Current thread: {}'.format(threading.current_thread()))
    shared_variable += 2
    lock.release()

threads = []
for func in [add_one, add_two]:
    threads.append(threading.Thread(target=func))
    threads[-1].start()

# wait for thread to complete before moving on with the main script
for thread in threads:
    thread.join()

print('shared_variable={}'.format(shared_variable))