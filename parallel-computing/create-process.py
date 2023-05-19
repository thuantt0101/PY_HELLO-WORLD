from multiprocessing import Process
import time

def _counter(counter, process_name):
    while(counter):
        time.sleep(0.01)
        print("{} : {}".format(process_name, counter))
        counter -= 1

if __name__=='__main__':
    counter = 5
    exec1 = Process(target=_counter, args=(counter, "thuan process"))
    exec2 = Process(target=_counter, args=(counter, "ai process"))

    exec1.start()
    exec2.start()

    execs = [exec1, exec2]    
    # Khi làm việc với multi-process, chúng ta luôn cần một lệnh join() 
    # để đảm bảo main process hoàn thành sau cùng sau khi các child process khác kết thúc.

    # Ta nhận thấy rằng các process được thực hiện một cách độc 
    # lập và bất đồng bộ. Để đồng bộ các process với nhau thì chúng ta đơn giản là lock chúng lại.
    for exec in execs:
        exec.join()
    