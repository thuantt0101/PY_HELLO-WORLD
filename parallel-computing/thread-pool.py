# Thread pool cũng tương tự như Process Pool nhưng là tập hợp của các các threads thay vì processes. 
# Các khởi tạo ThreadPoolExecutor trên concurrent.futures cũng
# hoàn toàn tương tự như ProcessPoolExecutor. Ta thực hiện như sau:

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

_submit_thread()