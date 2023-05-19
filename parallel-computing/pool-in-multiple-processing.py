# Trong python chúng ta có thể sử dụng pool để tận dụng được các tính toán song song trên nhiều process một lúc
# Cơ chế của pool đã loại bỏ hạn chế của GIL trong
# python, cho phép nhiều luồng hoạt động đồng thời và giúp đẩy nhanh quá trình tính toán.

# Trong Pool chúng ta có thể khai báo nhiều workers cùng thực hiện chương trình.
# Các chương trình có thể thực hiện một cách bất đồng bộ thông qua hàm apply_async().

# Tức là cho phép thực hiện song song nhiều method trên các workers.
# Đồng thời apply_async() cũng cho phép đưa vào các hàm callback để xử lý giữa liệu sau cùng.

# Ví dụ bên dưới chúng ta sẽ sử dụng 5 workers để tính toán bất đồng bộ bình phương của các số trong 
# phạm vi 20. Kết quả sau khi tính sẽ được lưu vào một list.

import multiprocessing as mp
import time

def _square(x):
    return x*x

def log_result(result):
    # Ham duoc goi bat ky khi nao _quare(i) tra ra ket qua
    # result_list duoc thuc hien tren main process, khong phai pool workers.
    result_list.append(result)

def apply_async_with_callback():
    pool = mp.Pool(processes=5)
    for i in range(20):
        pool.apply_async(_square, args=(i,), callback=log_result)
    
    pool.close()
    pool.join()
    print(result_list)

if __name__=='__main__':
    result_list = []
    apply_async_with_callback()

# [0, 1, 9, 25, 16, 36, 49, 64, 81, 100, 144, 4, 169, 225, 256, 289, 324, 361, 196, 121]
# Ta thấy thứ tự của list không theo tuần tự từ thấp tới cao do hàm được gọi bất đồng bộ.
