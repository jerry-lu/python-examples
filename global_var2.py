store = 2
# not actually changing global var, the store within the func is local
def add(x):
    store = 0
    store += x
    return store

print(add(1))
print(add(1))
