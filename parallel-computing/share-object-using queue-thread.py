# Queue là một định dạng stack an toàn khi làm việc với multi thread và process. 
# Chúng ta có thể tạo ra một queue và cho phép các thread, process truy cập dữ liệu mà
# không bị hiện tượng concurrency vì dữ liệu được truy suất 
# và sử dụng một lần bởi một thread hoặc process.

# Bên dưới chúng ta sẽ lấy ví dụ về việc sử dụng 2 process để đọc các dữ 
# liệu trong một queue. Hai process này tới phiên của mình sẽ lấy ra các 
# phần từ nằm trong queue theo kiểu FIFO (First Come First Out).

from multiprocessing import Process, Queue
import time

def _counter_queue(queue, process_name, max_count):
    while (max_count):
        time.sleep(0.01)
        value = queue.get()
        print("{}: {}".format(process_name, value))
        max_count -= 1

if __name__=='__main__':
    q = Queue()
    for i in range(10):
        q.put(i)
    max_count = 5

    exec1 = Process(target=_counter_queue, args=(q,"thuan process", max_count)  )
    exec2 = Process(target=_counter_queue, args=(q, "ai process", max_count))
    exec1.start()
    exec2.start()
    execs = [exec1, exec2]
    for i in execs:
        i.join()

# ai process: 0
# thuan process: 1
# ai process: 2
# thuan process: 3
# ai process: 4
# thuan process: 5
# ai process: 6
# thuan process: 7
# thuan process: 8
# ai process: 9

# Như vậy không có bất kỳ một data nào được sử dụng chung giữa 2 processes nên tránh được concurrency    


    
