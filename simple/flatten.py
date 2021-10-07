"""Different techniques to flatten deeply nested data structures
"""

# Using genetaror
# yield from effectively delegates the iteration process to an outer iteration.
# yield from is especially useful when writing code that must recursively iterate through nested iterables.
# Limitation -it is still subject to Python’s recursion limit, so it would not be able to handle deeply nested structures.


def flatten(items):
    for i in items:
        if isinstance(i, (list, tuple, set)):
            yield from flatten(i)
        else:
            yield i

#A solution which can work for flattening even a few million layers is a below, from same book

def stronger_flatten(items):
    stack = [iter(items)]
    while stack:
        try:
            item = next(stack[-1])
            if isinstance(item, (list, tuple, set)):
                stack.append(iter(item))
            else:
                yield item
        except StopIteration:
            stack.pop()

d= [1,[2,[3,4]],[5,6]]
for f in flatten(d):
    print(f,end=' ')

for f in stronger_flatten(d):
    print(f,end=' ')