# implement a resumable iterator with getState()/setState() for list
class Iterator:
    def __init__(self, list):
        self.list = list
        self.cur = 0

    def next(self):
        if self.cur >= len(self.list):
            raise StopIteration
        else:
            ret = self.list[self.cur]
            self.cur += 1
            return ret

    def has_next(self):
        return self.cur < len(self.list)

    def get_state(self):
        return self.cur

    def set_state(self, state):
        self.cur = state


def testItr():
    myItr = Iterator([1, 2, 3, 4, 5])
    expected_elements = [[1, 2, 3, 4, 5], [2, 3, 4, 5], [3, 4, 5], [4, 5], [5], []]

    states = []

    try:
        while True:
            states.append(myItr.get_state())
            myItr.next()
    except StopIteration:
        pass  # collect all possible state
    print(len(states))

    for index, state in enumerate(states):
        print("checking with state ", index)
        myItr.set_state(state)
        actual_elements = []
        try:
            while True:
                actual_elements.append(myItr.next())
        except StopIteration:
            print("finished collecting", state)

        assert actual_elements == expected_elements[index], (
            f"Elements mismatch at state {state}: expected {expected_elements[index]}, but got {actual_elements}"
        )

    print("succeed!")
    
testItr()

# myList = [1,2,3,4,5,6]
# myItr = Iterator(myList)
#
# print(myItr.next())
#
# print("saving state...")
# state = myItr.get_state()
#
# print("continue")
# print(myItr.next())
# print(myItr.next())
# print(myItr.next())
# print(myItr.next())
#
#
# print("resuming state...")
# myItr.set_state(state)
# print("continue")
# print(myItr.next())
# print(myItr.next())
# print(myItr.next())
# print(myItr.next())
