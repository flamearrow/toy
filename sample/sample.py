class C:
    def __init__(self):
        # value, count
        self.container = {}

    def add(self, value):
        if value in self.container:
            self.container[value] = self.container[value]+1
        else:
            self.container[value] = 1
        return ""

    def exists(self, value):
        if value in self.container:
            return "true"
        else:
            return "false"

    def remove(self, value):
        if value in self.container:
            count = self.container[value]
            if count == 1:
                self.container.pop(value)
            else:
                self.container[value] = count-1
            return "true"
        else:
            return "false"

    def get_next(self, value):
        sorted_values = sorted([v for v in self.container])
        for sorted_value in sorted_values:
            if sorted_value > value:
                return str(sorted_value)
        return ""

def solution(queries):
    ret = []
    c = C()
    for action, value_in_str in queries:
        value = int(value_in_str)
        if action == "ADD":
            ret.append(c.add(value))
        elif action == "REMOVE":
            ret.append(c.remove(value))
        elif action == "EXISTS":
            ret.append(c.exists(value))
        elif action == "GET_NEXT":
            ret.append(c.get_next(value))

    return ret


if __name__ == '__main__':
    ret = solution(
        [["ADD","0"],
         ["ADD","1"],
         ["ADD","1"],
         ["ADD","11"],
         ["ADD","22"],
         ["ADD","3"],
         ["ADD","5"],
         ["GET_NEXT","0"],
         ["GET_NEXT","1"],
         ["REMOVE","1"],
         ["GET_NEXT","1"],
         ["ADD","0"],
         ["ADD","1"],
         ["ADD","2"],
         ["ADD","1"],
         ["GET_NEXT","1"],
         ["GET_NEXT","2"],
         ["GET_NEXT","3"],
         ["GET_NEXT","5"]]
    )

    for value in ret:
        print(ret)

