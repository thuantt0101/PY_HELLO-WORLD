from multiprocessing import Process, Lock
import time

def _counter_lock(counter, process_name, lock):
    lock.acquire()
    while(counter):
        time.sleep(0.01)
        print("{}: {}".format(process_name, counter))
        counter -= 1
    lock.release()


if __name__ =='__main__':
    counter = 5
    lock = Lock()
    exec1 = Process(target=_counter_lock, args=(counter, "thuan process", lock))
    exec2 = Process(target=_counter_lock, args=(counter, "ai process", lock))
    execs = [exec1, exec2]
    for exec in execs:
        exec.start()
