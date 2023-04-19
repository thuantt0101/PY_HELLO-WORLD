# Viết chương trình sắp xếp tuple (name: string, age: number, score: number) theo thứ tự tăng dần. 
# Tuple được nhập vào bởi người dùng. Tiêu chí sắp xếp như sau: name > age > score. 
def input_tupe():
    l = []
    for i in range(5):
        print('--------------------------------')
        print('enter row {0}'.format(i + 1))
        name = input('please input name : ')
        age = input('please input age ')
        score = input('please input score : ')
        t = (name, age, score)
        l.append(t)
    
    return l

def _sort(e):
    return e[0]

ls = input_tupe()
ls.sort()
print(ls)