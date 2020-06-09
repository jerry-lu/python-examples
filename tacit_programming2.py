import functools

def foo(x):
    return x + 1

def bar(y):
    return y + 2

def baz(z):
    return z + 3

def compose(*fns):
    return functools.partial(functools.reduce, lambda v, fn: fn(v), fns)


example = compose(baz, bar, foo)
print(example(1))
