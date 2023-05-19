# Trong python thì bắt đầu từ version 3.2 chúng ta có thể sử dụng module concurrent.futures
# để xử lý bất đồng bộ các tasks. Đây là một abstract layer được kế thừa trên
# cả hai modules là threading và multiprocessing để tạo ra một interface 
# cho phép khởi tạo các task sử dụng pool của các processes và threads.
# Để khởi tạo một Process Pool, chúng ta sử dụng ProcessPoolExecutor trong concurrent.futures module.

from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import as_completed
from time import sleep
import timeit

def _counter(counter, task_name):
    print("Start process {}".format(task_name))
    while(counter):
        sleep(0.01)
        print("{} : {}".format(task_name, counter))
        counter -= 1        
    print("End process {}".format(task_name))
    return "Complete {}".format(task_name)

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


# map()
x1s = [5, 10, 20, 35]
x2s = [15, 20, 30, 55]
y1s = [5, 10, 10, 15]
y2s = [15, 20, 20, 35]

def _bbox(x1, x2, y1, y2):
  w = x2-x1
  h = y2-y1
  area = w*h
  return area

if __name__=='__main__':
    # _submit_process()
    with ProcessPoolExecutor(max_workers=5) as executor:
        results = executor.map(_bbox, x1s, x2s, y1s, y2s)

    for result in results:
        print(result)    
