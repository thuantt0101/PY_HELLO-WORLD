
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
print("Type of BASE DIR : {0} and value of Base Dir is : {1}".format(type(BASE_DIR), BASE_DIR )) 
# Output : Type of BASE DIR : <class 'pathlib.WindowsPath'> and value of Base Dir is : D:\1. DATA WORLD\2. PYTHON\PY WORKSPACE\PY_HELLO WORLD

staticfiles_dirs = [ 
    os.path.join(BASE_DIR, 'static')
]

print("Type of staticfiles_dirs  is : {0} and value is : {1}".format(type(staticfiles_dirs), staticfiles_dirs))
# output: Type of staticfiles_dirs  is : <class 'list'> and value is : ['D:\\1. DATA WORLD\\2. PYTHON\\PY WORKSPACE\\PY_HELLO WORLD\\static']
