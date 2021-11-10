i = 5
def f(arg=1):
    print(arg)
i = 6
f()

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

