import functools
import inspect

'''
A simple Decorator to cache calculated result
'''


class Memoize(object):
    def __init__(self, max_size):
        self.arg = max_size
        self.memo = {}

    def __call__(self, fn):
        @functools.wraps(fn)
        def decorated(*args, **kwargs):
            sig = inspect.signature(fn)
            calling_sig= (str(sig.bind(*args, **kwargs).arguments.values()))
            if not calling_sig in self.memo:
                print("Calculating value")
                if len(self.memo) == self.arg:
                    print("Popping items")
                    self.memo.popitem()
                self.memo[calling_sig] = fn(*args, **kwargs)
            # print(self.memo)
            return self.memo[calling_sig]
        return decorated


@Memoize(max_size=30)
def mul(a, b):
    return a * b


if __name__ == '__main__':
    print(mul(1, 2))
    print(mul(2, 2))
    print(mul(1, 2))
    print(mul(3, 2))
    print(mul(14, 2))
    print(mul(15, b=2))
    print(mul(1, 2))
    print(mul(15, b=2))
    print(mul(15, b=2))

