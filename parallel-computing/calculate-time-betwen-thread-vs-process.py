
# https://phamdinhkhanh.github.io/2020/11/30/ParallelComputingPython.html#5-queue

import cProfile

from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor
from time import sleep

def _counter(counter, task_name):
  print("Start process {}!".format(task_name))
  while (counter):
    print("{} : {}".format(task_name, counter))
    counter -= 1
  print("End process {}!".format(task_name))
  return "Completed {}!".format(task_name)

def _submit_thread():
  executor = ThreadPoolExecutor(max_workers=5)
  future = executor.submit(_counter, 10, "task1")
  print('State of future: ', future.done())
  print('futre result: ', future.result())
  print('State of future: ', future.done())


def _submit_process():
    # max_workers : number of workers, so luong worker cang lon thi cang nhieu threads sinh ra de tinh toan process
    executor = ProcessPoolExecutor(max_workers=5)
    
    # submit() :duoc su dung de load cac task vao process pool
    future = executor.submit(_counter, 20, "task1")

    # done(): kiem tra trang thai cua task
    print('State of future: ', future.done())
    
    # result() : dung de kiem tra ket qua sau khi task cuoi cung trong process pool
    
    print('future result: ', future.result())

    # da thuc thi xong. do do trang thai done() sau khi result duoc tra ve la True
    print('State of future', future.done())

# _submit_thread()
if __name__=='__main__':
    cProfile.run('_submit_process()')
    cProfile.run('_submit_thread()')


# Với cùng các tác vụ như nhau thì ta thấy thời gian thực thi của Thread Pool chỉ là 0.001 seconds
# nhanh thời gian thực thi của Process Pool là 0.072 seconds. Lý do là vì thread là một phiên bản light weight 
# hơn process rất nhiều. Bạn có thể nhận thấy điều này một cách trực quan thông qua số hàm được gọi ở cả hai phương pháp.
# Vậy lựa chọn thế nào giữa process pool và thread pool?
# Chúng ta đã biết rằng khi sử dụng threads thì sẽ có lợi về I/O vì các threads có thể chia sẻ data qua lại lẫn nhau. Còn giữa các
# processes thì data được sử dụng hoàn toàn độc lập nên không có lợi về I/O.
# Tuy nhiên khi sử dụng process thì chúng ta sẽ được allocate về CPU, Memomory,… 
# nên lời khuyên là nếu task của bạn gặp phải giới hạn về I/O bound thì nên sử dụng thread pool và giới
# hạn về CPUs bound thì nên sử dụng process pool.