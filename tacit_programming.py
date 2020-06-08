def foo(x):
    return 1

def bar(y):
    return 2

def baz(z):
    return 3

def example(x):
    y = foo(x)
    z = bar(y)
    w = baz(z)
    return w


test1 = example(4)
print(test1)