# Fibonacy
# 1 1 2 3 5 8 ....

def fib():
    """
        declare two param to store values of current value and next_value
        while each loop => return current_value
        and assign value next_value for current_value 
        and next_value = current_value + next_value
    """
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a + b
    
# Testing
import types
if type(fib()) == types.GeneratorType:    
    counter = 0
    for n in fib():
        print(n)
        counter +=1
        if counter == 10:
            break

    
    



