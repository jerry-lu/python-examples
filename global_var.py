store = 0

def add(x):
    global store
    store += x

add(2)
print(add(3))
