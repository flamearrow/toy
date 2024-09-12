import json


class FileIterator:
    def __init__(self, file_name):
        self.file_name = file_name
        with open(self.file_name, "r") as file_to_iterate:
            try:
                self.lst = json.load(file_to_iterate)
                self.cur = 0
            except:
                self.lst = []
                self.cur = 0

    def next(self):
        if self.cur < len(self.lst):
            ret = self.lst[self.cur]
            self.cur += 1
            return ret
        else:
            raise StopIteration

    def get_state(self):
        return self.cur

    def set_state(self, state):
        self.cur = state


def hasNext(itr):
    curState = itr.get_state()
    try:
        itr.next()
        return True
    except StopIteration:
        return False
    finally:
        itr.set_state(curState)


def testFileItr():
    myItr = FileIterator("itrF3")
    expected_elements = [[6, 7], [7]]
    # myItr = FileIterator("itrF1")
    # expected_elements = [[1, 2, 3, 4, 5], [2, 3, 4, 5], [3, 4, 5], [4, 5], [5]]

    states = []

    while hasNext(myItr):
        states.append(myItr.get_state())
        myItr.next()
    print(f"got {len(states)} states")

    for index, state in enumerate(states):
        print("checking with state ", index)
        myItr.set_state(state)
        actual_elements = []
        while hasNext(myItr):
            actual_elements.append(myItr.next())
        assert actual_elements == expected_elements[index], (
            f"Elements mismatch at state {state}: expected {expected_elements[index]}, but got {actual_elements}"
        )

    print("succeed!")

    myItr2 = FileIterator("itrF2")
    assert hasNext(myItr2) == False


if __name__ == '__main__':
    testFileItr()
