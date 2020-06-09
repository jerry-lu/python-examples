def foo(x):
    return x + 1

def bar(y):
    return y + 2

def baz(z):
    return z + 3

def example(x):
    y = foo(x)
    z = bar(y)
    w = baz(z)
    return w


test1 = example(4)
print(test1)