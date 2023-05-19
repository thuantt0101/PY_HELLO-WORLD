# Khi làm việc với các ứng dụng concurrent thì chúng ta nên hạn chế nhất có thể việc chia sẻ dữ liệu giữa các 
# process để tránh xảy ra các lỗi phát sinh do concurency.
# Tuy nhiên python vẫn cung cấp một cơ chế giúp chia sẻ dữ liệu giữa các process
# đó chính là các shared memory object trong multiprocessing như Value, Array. Thật vậy, giả
# sử ở ví dụ bên dưới chúng ta sử dụng 2 processes để thay đổi dấu các phần tử của một list các số nguyên.

from multiprocessing import Process, Lock, Value, Array
import time

def _counter_arr(arrs, process_name, lock):
    lock.acquire()
    for i, el in enumerate(arrs):
        time.sleep(0.01)
        arrs[i] = -arrs[i]
        print("{} : {}".format(process_name, arrs[i]))

    lock.release()

if __name__ == '__main__':
    
    # Have to use Array to share data from multiple process
    arrs = Array('i', range(1, 5)) 
    lock = Lock()
    exec1 = Process(target=_counter_arr, args=(arrs, "thuan process", lock))
    exec2 = Process(target= _counter_arr, args=(arrs, "ai process", lock))
    execs = [exec1, exec2]
    exec1.start()
    exec2.start()
    for i in execs:
        i.join()



