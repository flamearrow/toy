# industry template
# 1.Level 1仍旧是set，get， delete，但是对相同的key field储存的value，不再是替换已储存的value，而是要与之前已储存的value加总。
# 2.Lev‍‌‌‍‍el 2是加入modification的计次。对同一个key的set，delete这些操作都计入modification，最后要求返回被modify最多的n个key。
# 3.Level 3没做完，如图。
class Solution:
    def __init__(self):
        # {key: {field: [values]}}
        self.values = {}
        # {key: count}
        self.modified = {}

        # {key: [userId]}
        self.locked = {}

    # same key and field, adds up value
    def set(self, key, field, value, callerId=None):
        # print("  values", self.values)
        # print("  key, field, value, callerId", key, field, value, callerId)
        if key not in self.values:
            self.values[key] = {field: [value]}
            if key not in self.modified:  # can be deleted before
                self.modified[key] = 1
            else:
                self.modified[key] += 1
        else:
            lockedBy = self.lockedBy(key)
            if not lockedBy or lockedBy == callerId:
                self.modified[key] += 1
                if field not in self.values[key]:
                    self.values[key][field] = [value]
                else:
                    self.values[key][field].append(value)

        return self.get(key, field)

    def lockedBy(self, key):
        if key not in self.locked:
            return None
        elif len(self.locked[key]) == 0:
            return None
        else:
            return self.locked[key][0]

    # return the sum of all values of a field
    def get(self, key, field):
        if key not in self.values:
            return "0"
        if field not in self.values[key]:
            return "0"
        return "{}".format(sum(self.values[key][field]))

    def delete(self, key, field, callerId=None):
        if key not in self.values:
            return "false"
        if field not in self.values[key]:
            return "false"
        lockedBy = self.lockedBy(key)
        if not lockedBy or lockedBy == callerId:
            self.modified[key] += 1
            del self.values[key][field]
            return "true"
        else:  # locked by others
            return "false"

    # return as key(modifiedTimes)
    def mostModifiedKey(self, n):
        sortedModified = sorted(self.modified.items(), key=lambda x: (-x[1], x[0]))
        ret = []
        if len(sortedModified) > n:
            ret = sortedModified[:n]
        else:
            ret = sortedModified
        return ", ".join(map(lambda x: "{}({})".format(x[0], x[1]), ret))

    def lock(self, callerId, key):
        if key not in self.values:
            return "invalid_request"
        lockedBy = self.lockedBy(key)
        if not lockedBy:
            self.locked[key] = [callerId]
            return "acquired"
        elif lockedBy == callerId:
            return ""
        else:
            self.locked[key].append(callerId)
            return "wait"

    def unlock(self, key):
        if key not in self.locked:
            return "invalid_request"
        lockedBy = self.lockedBy(key)
        if lockedBy:
            self.locked[key].pop(0)
            return "released"
        else:
            return ""


def solution(queries):
    s = Solution()
    ret = []
    for query in queries:
        op = query[0]
        if op == 'SET_OR_INC':
            key = query[1]
            field = query[2]
            value = query[3]
            ret.append(s.set(key, field, int(value)))
        elif op == 'GET':
            key = query[1]
            field = query[2]
            ret.append(s.get(key, field))
        elif op == 'DELETE':
            key = query[1]
            field = query[2]
            ret.append(s.delete(key, field))
        elif op == 'MOST_MODIFIED':
            n = query[1]
            ret.append(s.mostModifiedKey(int(n)))
        if op == 'SET_OR_INC_BY_CALLER':
            key = query[1]
            field = query[2]
            value = query[3]
            callerId = query[4]
            ret.append(s.set(key, field, int(value), callerId))
        elif op == 'DELETE_BY_CALLER':
            key = query[1]
            field = query[2]
            callerId = query[3]
            ret.append(s.delete(key, field, callerId))
        elif op == 'LOCK':
            callerId = query[1]
            key = query[2]
            ret.append(s.lock(callerId, key))
        elif op == 'UNLOCK':
            key = query[1]
            ret.append(s.unlock(key))
    return "\n".join(map(lambda x: str(x), ret))


queries = [
    ["SET_OR_INC", "A", "B", "4"],
    ["LOCK", "user1", "A"],
    ["LOCK", "user2", "A"],
    ["LOCK", "user3", "B"],
    ["UNLOCK", "B"],
    ["SET_OR_INC", "A", "C", "5"],
    ["DELETE", "A", "B"],
    ["SET_OR_INC_BY_CALLER", "A", "B", "3", "user2"],
    ["GET", "A", "B"],
    ["DELETE_BY_CALLER", "A", "B", "user3"],
    ["SET_OR_INC_BY_CALLER", "A", "B", "5", "user1"],
    ["UNLOCK", "A"],
    ["SET_OR_INC_BY_CALLER", "A", "B", "2", "user1"],
    ["SET_OR_INC_BY_CALLER", "A", "B", "1", "user2"],
]
print(solution(queries))
