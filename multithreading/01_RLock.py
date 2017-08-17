"""
threading.Lock doesn't know which threading is holding even themself
so the threading.RLock (Re-rntrant Lock) is used

main use of threading.RLock is nested access share variable
e.g. recursion

即使是 thread A 使用 Lock 來限制存取, thread A 本身也不會知道是自己使用了 Lock
當 thread A 重複使用兩次 acquire (打算上鎖兩次) 就會產生 block (動彈不得)
這種情況下要使用的是 RLock, 不會因為重複 lock 就導致 block
主要使用情境在於類似 recursion 這種 nested access
"""
import threading


lock = threading.Lock()
rlock = threading.RLock()
shared_variable = 0

"""
block issue with threading.Lock
"""
def block_issue():
    global shared_variable
    lock.acquire()
    shared_variable += 1
    print('shared_variable = {} in thread {} with Lock'.format(shared_variable, threading.current_thread))

    # blocked
    lock.acquire()
    shared_variable += 2
    print('shared_variable = {} in thread {} with Lock'.format(shared_variable, threading.current_thread))

    lock.release()


"""
RLock solution
"""
def block_solution():
    global shared_variable
    rlock.acquire()
    shared_variable += 3
    print('shared_variable = {} in thread {} with RLock'.format(shared_variable, threading.current_thread))

    # this won't block
    rlock.acquire()
    shared_variable += 4
    print('shared_variable = {} in thread {} with RLock'.format(shared_variable, threading.current_thread))

    # release last locked rlock
    rlock.release()
    print('shared_variable = {} in thread {} with RLock'.format(shared_variable, threading.current_thread))

    # release first locked rlock
    rlock.release()
    print('shared_variable = {} in thread {}'.format(shared_variable, threading.current_thread))


# block_issue()
# print('shared_variable = {} after lock issue'.format(shared_variable))
block_solution()
print('shared_variable = {} after rlock condition'.format(shared_variable))