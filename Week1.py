def safe_call(f, **kwargs):
    for i, j in kwargs.items():
        if i in f.__annotations__.keys():
            if (f.__annotations__[i] != type(j)):
                raise "Error"
    return f(**kwargs)


def f(x: int, y: float, z):
    return x+y+z


print(safe_call(f, x=5, y=7.0, z=3))
