def debug(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__}({args}, {kwargs}) = {result}")
        return result
    return wrapper

@debug
def multiply(x, y):
    return x * y


def blah(func):
    def wrapped(*args, **kwargs):
        print("you are calling blah on this func with args", args)
        print("you are calling blah on this func with kwargs", kwargs)

        return func(*args, **kwargs)
    return wrapped

@blah
def hello(n):
    print("MLGB", n)


if __name__ == '__main__':
    # print(multiply(5, 7))
    hello()
