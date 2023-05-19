import threading
import time

class FirstThread(threading.Thread):

    def __init__(self, thread_id, thread_name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.thread_name = thread_name
        self.counter = counter

    def run(self):
        print("Start thread {}!".format(self.thread_name))
        while(self.counter):
            time.sleep(0.01)
            print("{0} : {1}".format(self.thread_name, self.counter))
            self.counter -= 1
        
        print("End thread : {}".format(self.thread_name))

thread1= FirstThread(1, "thuan thread", 5)
thread2 = FirstThread(2, "ai thread", 5) 

thread1.start()
thread2.start()
    