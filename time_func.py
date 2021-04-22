import time

def time_func(func):
    def wrapper(*args, **kwargs):
        ti = time.time()
        func(*args, **kwargs)
        tf = time.time()
        print("%s running time: %f sec"%(func.__name__, tf-ti))
    
    return wrapper
