# Như đã giới thiệu chương trước, trong ví dụ ở trên các threads là bất đồng bộ (asynchronous)
#  Hai threads chạy độc lập với nhau mà không theo thứ tự. Chúng ta có thể
# đồng bộ (synchronous) các thread. Tức là cho phép một thread chạy xong thì thread 
# khác mới được phép chạy bằng cách sử dụng Thread Lock trong python.

# Trong hàm run() của thread thì chỉ cần thêm hàm thread.acquire() 
# và thread.release() vào đầu và cuối hàm thì luồng sẽ được locking cho đến khi thread chạy xong thì thread khác mới được xử lý tiếp. Như chúng ta thấy, sau khi thread1 xử lý xong thì mới đến lượt thread2 xử lý.
import threading
import time


class FirstThread(threading.Thread):
    
    def __init__(self, thread_id, thread_name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.thread_name = thread_name
        self.counter = counter
    
    def run(self):
        threadLock.acquire()
        print("Start thread {}".format(self.thread_name))

        while(self.counter):
            time.sleep(0.01)
            print("{} : {}".format(self.thread_name, self.thread_id))                        
            self.counter -= 1

        print("End thread {}".format(self.thread_name))
        threadLock.release()

threadLock = threading.Lock()
thread1 = FirstThread(1, "thuan thread", 5)
thread2 = FirstThread(2, "ai thread", 5)

thread1.start()
thread2.start()
threads = [ thread2, thread1 ]

for i in threads:
    i.join()


    
