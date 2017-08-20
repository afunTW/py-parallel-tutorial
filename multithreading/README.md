# Multithreading

## Synchorzing Thread

Simple implementation with threading subclass `Lock`, `RLock`, `Semaphore`, `Events`, `Condition`, `Barries` for synchorzing in different thread.

Using `acquire(blocking)` method to block the thread

- acquire(False): immediately return
  - return 0: lock can not be acquire
  - return 1: lock was acquire
- acquire(True): thread blocks and wait for the lock be released

Using `release()` method to release the lock

## Priority Queue

In order to hold a specfic number of items.