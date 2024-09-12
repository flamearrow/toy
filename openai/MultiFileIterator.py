from FileIterator import FileIterator
from FileIterator import hasNext


# Build a multi file iterator
# state is a) currentIndex and b) states of each internal iterator
# trick: don't save list of internal itrs, but just return them dynamically
# only save the itr index
# have a moveToNext to make sure curItr has next, or curItr overflown
# getState: return curIndex and all internal itrs states
# setState: set curIndex and set all internal itrs states
class MultiFileIterator:
    def __init__(self, fileNames):
        self.fileItrs = [FileIterator(fileName) for fileName in fileNames]
        self.curItrIndex = 0
        self._move_to_next()

    def __next__(self):
        return self.next()

    def __iter__(self):
        return self

    # try move to next itr/state so that its hasNext
    # otherwise let itrIndex overflow
    def _move_to_next(self):
        while self.curItrIndex < len(self.fileItrs):
            if hasNext(self.fileItrs[self.curItrIndex]):
                return
            self.curItrIndex += 1

    def get_state(self):
        return self.curItrIndex, [itr.get_state() for itr in self.fileItrs]

    def set_state(self, state):
        self.curItrIndex, curItrStates = state
        for index, itr in enumerate(self.fileItrs):
            itr.set_state(curItrStates[index])

    def next(self):
        if self.curItrIndex >= len(self.fileItrs):
            raise StopIteration
        else:
            ret = self.fileItrs[self.curItrIndex].next()
            self._move_to_next()
            return ret


# for lazy, save list of file names, initialize the iterator when needed
# when saving state, return a list of nullable states, null if the iterator is not implemented
# when setting state, nullify the iterator if state is empty
class MultiFileIteratorLazy:
    def __init__(self, fileNames):
        self.fileNames = fileNames
        self.fileItrs = [None] * len(fileNames)
        self.curItrIndex = 0
        self._move_to_next()

    def _current_itr(self):
        if not self.fileItrs[self.curItrIndex]:
            self.fileItrs[self.curItrIndex] = FileIterator(self.fileNames[self.curItrIndex])
        return self.fileItrs[self.curItrIndex]

    # try move to next itr/state so that its hasNext
    # otherwise let itrIndex overflow
    def _move_to_next(self):
        while self.curItrIndex < len(self.fileItrs):
            if hasNext(self._current_itr()):
                return
            self.curItrIndex += 1

    def get_state(self):
        return self.curItrIndex, [itr.get_state() if itr else None for itr in self.fileItrs]

    def set_state(self, state):
        self.curItrIndex, curItrStates = state
        for index, state in enumerate(curItrStates):
            if state:
                self.fileItrs[index].set_state(state)
            else:
                self.fileItrs[index] = None

    def next(self):
        if self.curItrIndex >= len(self.fileItrs):
            raise StopIteration
        else:
            ret = self._current_itr().next()
            self._move_to_next()
            return ret


def testMultiFileItr():
    multiItr = MultiFileIteratorLazy(["itrF1", "itrF2", "itrF3"])
    expected_elementses = (
        [1, 2, 3, 4, 5, 6, 7], [2, 3, 4, 5, 6, 7], [3, 4, 5, 6, 7], [4, 5, 6, 7], [5, 6, 7], [6, 7], [7])
    states = []
    while hasNext(multiItr):
        states.append(multiItr.get_state())
        multiItr.next()

    print(f"states: {states}")

    for index, state in enumerate(states):
        expected_elements = expected_elementses[index]
        multiItr.set_state(state)
        actual_elements = []
        while hasNext(multiItr):
            actual_elements.append(multiItr.next())
        assert actual_elements == expected_elements, f"incorrect! expected: {expected_elements}, but got {actual_elements}"

    print("success!")


def testIterateMultifiles():
    mfi = MultiFileIteratorLazy(["itrF1", "itrF2", "itrF3"])
    while hasNext(mfi):
        print(mfi.next())


def testIterateSinglefile():
    mfi = MultiFileIterator(["itrF1"])
    while hasNext(mfi):
        print(mfi.next())

def testIterateSingleEmptyFile():
    mfi = MultiFileIterator(["itrF2"])
    while hasNext(mfi):
        print(mfi.next())


def testIterateMultipleEmptyFiles():
    mfi = MultiFileIterator(["itrF4"])
    while hasNext(mfi):
        print(mfi.next())

def testIterateNofile():
    mfi = MultiFileIterator([])
    while hasNext(mfi):
        print(mfi.next())

def testIterateMultifile2():
    mfi = MultiFileIterator(["itrF2", "itrF3", "itrF4"])
    while hasNext(mfi):
        print(mfi.next())


def testIterationLoop():
    mfi = MultiFileIterator(["itrF1", "itrF2", "itrF3"])
    for v in mfi:
        print(v)


if __name__ == '__main__':
    testIterationLoop()
    # testMultiFileItr()
    # testIterateMultifiles()
    # testIterateSinglefile()
    # testIterateSingleEmptyFile()
    # testIterateMultipleEmptyFiles()
    # testIterateNofile()
    # testIterateMultifile2()
