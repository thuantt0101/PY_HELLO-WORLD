# Queue là một cấu trúc dữ liệu tuyến tính (linear data structure).
# Nó có tính chất tương tự như list. Cho phép chúng ta thêm, sửa, xóa,
# truy xuất các phần tử bên trong. Trong python, Queue có ưu điểm lớn hơn list 
# đó là tốc độ truy xuất nhanh hơn. Độ phức tạp thời gian
# (time complexity) của queue là O(1) trong khi của list là O(n).
#  Queue là một lựa chọn thay thế tốt hơn cho list trong trường hợp dữ
# liệu của bạn có số lượng phần tử lớn.

# Khi làm việc với Queue ban có thể truy xuất các phần tử bên trong khối theo kiểu FIFO 
#  (first in first out) hoặc LIFO (last in first out) thông qua hàm pop().

# Queue thường được sử dụng trong các tác vụ liên quan tới threads synchronous. 
# Các thread sẽ sử dụng chung một dữ liệu và thay đổi
# các phần tử bên trong nó một cách tuần tự.
from concurrent.futures import ThreadPoolExecutor 
import queue


def _sum_queue(name, work_queue):
  sum = 0
  while not work_queue.empty():
    print(f"Task {name} running")
    count = work_queue.get()
    sum += count
  print(f"Task {name} total: {sum}")
  return sum

def task(name, work_queue):
  if work_queue.empty():
    print(f"Task {name} nothing to do")
  else:
    print("Start ThreadPoolExecutor!")
    with  ThreadPoolExecutor(max_workers = 5) as executor:
      print("Submit task!")  
      future = executor.submit(_sum_queue, name, work_queue)
      sum = future.result()
    return sum
    
# Create the queue of work
work_queue = queue.Queue()

# Put some work in the queue
for work in [15, 10, 5, 2]:
    work_queue.put(work)

# Create some synchronous tasks
tasks = [("one", work_queue), ("two", work_queue)]

# Run the tasks
for n, q in tasks:
    print(task(n, q))

# Trong ví dụ trên giải sử chúng ta có hai threads hoạt động một cách synchronous là one và two.
# Hai threads này sử dụng chung một nguồn dữ liệu là work_queue.
# Khi thread one chạy xong thì toàn bộ các phần tử của queue đã được trích xuất xong nên ở thread two
# chúng ta không có gì để chạy tiếp.
    


    
