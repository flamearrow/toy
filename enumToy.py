from enum import Enum
class T(Enum):
    Red = 1,
    Blue =2

def b(t):
    if t == T.Red:
        print("red")
    elif t == T.Blue:
        print("blue")

if __name__ == '__main__':
    b(T.Red)