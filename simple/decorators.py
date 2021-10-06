import time
from functools import wraps


def trace(func, debug=True):
    """
    A simple decorator to print function name and it's arguments
    """
    wraps(func)
    def call(*args, **kwargs):
        if debug:
            all_args = ', '.join([repr(a) for a in args] +
                                 [f"{k}={v!r}" for k, v in kwargs.items()])
            print(f'Calling {func.__name__}({all_args})')
        return func(*args, **kwargs)
    return call


def timer(func):
    """
    Print the runtime of the decorated function
    """
    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer


@trace
@timer
def my_add(a,b,c):
    time.sleep(10)
    return a + b + c


if __name__ == '__main__':
    my_add(1,2, c=3)