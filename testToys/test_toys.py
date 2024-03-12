import unittest


class MyException(Exception):
    def __init__(self):
        super().__init__()


def blah():
    try:
        throwExp()
    except MyException as e:
        print("gotcha")


def throwExp():
    raise MyException()


class BlahTestCase(unittest.TestCase):
    def test_blah(self):
        with self.assertRaises(MyException):
            throwExp()


if __name__ == '__main__':
    blah()
    print("bglm")