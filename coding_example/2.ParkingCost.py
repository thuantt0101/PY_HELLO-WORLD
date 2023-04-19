# Một buổi tối, anh Sơn đậu ba chiếc ô tô của mình trong một khu vực, 
# nơi tính tiền đỗ xe một cách khác thường - họ có giá khác nhau cho mỗi thương hiệu xe.

# Với chiếc AUDI,đỗ, a Sơn trả a đồng mỗi phút. Khi đỗ chiếc Mercedes ,
#  anh Sơn phải trả b đồng mỗi xe cho mỗi phút. Khi đỗ chiếc cadillac, anh Sơn trả c đồng mỗi xe mỗi phút.


# Cho các số a, b và c, cũng như khoảng thời gian mà ba chiếc xe ô tô của anh Sơn đậu, 
# xác định số tiền anh Sơn cần trả cho chủ sở hữu của khu vực đỗ xe.
# Input: a,b,c là ba số thực không âm , 1<a,b,c>100


def cal_parking_cost():    
    a =  int(input("please enter cost for AUDI :"))
    while a <= 0:
        print('a have to be greater than 0')
        a = int(input("please enter cost for AUDI :"))
         
    b = int(input("Please enter cost for Mercedes : "))
    while b <=0 :
        print('a have to be greater than 0')
        b = int(input("please enter cost for AUDI :"))       


    c = int(input("Please enter cost for cadillac : "))
    while c <=0 :
        print('a have to be greater than 0')
        c = int(input("please enter cost for AUDI :"))        
    
    minutes = 5

    return (a + b + c) * minutes


cost = cal_parking_cost()    
print("cost is {0}".format(cost))