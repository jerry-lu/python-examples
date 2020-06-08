import functools

def foo(x):
    return 1

def bar(y):
    return 2

def baz(z):
    return 3

def compose(*fns):
    return functools.partial(functools.reduce, lambda v, fn: fn(v), fns)


example = compose(baz, bar, foo)
print(example)