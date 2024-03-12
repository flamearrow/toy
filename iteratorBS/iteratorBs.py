# desing an interator of a list resumable with following interfaces, and raise an exception when next() doesn't have anything
# get_state(), set_set(), next(), hasNext()
# then come up with some tests



class NoMoreItemsException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class InvalidStateException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Iterator:
    def __init__(self, lst):
        self.lst = lst
        self.current = 0

    def next(self):
        if (self.current >= len(self.lst)):
            raise NoMoreItemsException()
        ret = self.lst[self.current]
        self.current += 1
        return ret

    def getState(self) -> int:
        return self.current

    def setState(self, newState):
        if (self.current >= len(self.lst)):
            raise InvalidStateException()
        self.current = newState

    def hasNext(self):
        return self.current < len(self.lst)


def testEmptyInput():
    itr = Iterator(())
    assert (not itr.hasNext())

# it = Iterator((1,2,3,4,5))

# it.next()
# it.next()
# it.next()
# state = it.getState()
# it.next()
# it.next()


# it.setState(state)
# while(it.hasNext()):
#     print(it.next())

# try:
#     print(it.next())
# except NoMoreItemsException as e:
#     print("no more items!", e)
