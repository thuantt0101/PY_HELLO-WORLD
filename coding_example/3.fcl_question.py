
import pandas as pd

Type = ['Electronics', 'Electronics', 'Electronics', 'Education', 'Education', 'Electronics', 'Education']
Item = ['Phone', 'Monitor', 'Keyboard', 'Book', 'Textbook', 'Monitor', 'Book']
Number = [10, 20, 15, 30, 20, 20, 30]

def numDuplicates(types, items, numbers):
    products = {'Type': type, 'Item' : items, 'Number' : numbers}
    df = pd.DataFrame(products)
    duplicateProducts = df[df.duplicated()]
    numOfdup = len(duplicateProducts)
    return numOfdup

print(numDuplicates(Type, Item, Number))
    

