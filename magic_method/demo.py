


def checkNumType(correct_type):
    def check(old_func):
        def new_func(arg):
            if(isinstance(arg, correct_type)):
                return old_func(arg)
            else:
                print('Bad Type')
        return new_func
    return check                

@checkNumType(int)
def time3(num):
    return num * 3

print(time3(3))
