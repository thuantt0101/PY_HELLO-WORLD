# object.__enter__(self)

# Summary: Python calls the __enter__() magic method when starting a 
# with block whereas the __exit__() method is called at the end. 
# An object that implements both __enter__() and __exit__() methods is called a context manager.
# By defining those methods, you can create your own context manager.

class MySecretConnection:
    def __init__(self, url):
        self.url = url

    def __enter__(self):
        print('entering', self.url)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('leaving', self.url)


# testing
with MySecretConnection('https://finxter.com') as finxter:
    # Called finxter.__enter__()
    pass
    # Called finxter.__exit__()
# entering https://finxter.com
# leaving https://finxter.com

# conn = MySecretConnection("abc") # nothing printed
