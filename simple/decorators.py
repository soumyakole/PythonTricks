from functools import wraps


def trace(func, debug=True):
    """
    A simple decorator to print function name and it's arguments
    """
    wraps(func)
    def call(*args, **kwargs):
        if debug:
            print('Calling', func.__name__,
                  'With positional arguments', ','.join(map(lambda x: str(x), args)) if args else (),
                  'and with keyword arguments', ','.join('{}={}'.format(k,v) for k,v in kwargs.items()) if kwargs else {}
                  )
        return func(*args, **kwargs)
    return call


