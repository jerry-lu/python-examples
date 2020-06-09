import functools


def myfunc(n):
    return lambda a: a * n


def compose(*fns):
    return functools.partial(functools.reduce, lambda v, fn: fn(v), fns)


mydoubler = myfunc(2)
print(mydoubler(11))

mytripler = myfunc(3)
print(mytripler(11))

composite = compose(myfunc(2), myfunc(3))
print(composite(11))
