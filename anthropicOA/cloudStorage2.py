# industry template

class Solution:
    def __init__(self):
        # {name: size}
        self.files = {}

        # {user: capacity}
        self.users = {}

        # {user: [filename]}
        self.owner = {}

    def userSize(self, userId):
        ret = 0
        for fName in self.owner[userId]:
            ret += self.files[fName]
        return ret

    def userQuota(self, userId):
        if userId == "admin":
            return 99999999999
        return self.users[userId] - self.userSize(userId)

    def addFile(self, name, size, userId=None):
        if name in self.files:
            return "false"
        else:
            self.files[name] = size
            if userId:
                if self.userQuota(userId) < size:
                    return "no quota"
                else:
                    self.owner[userId].append(name)
                    return "{}".format(self.userQuota(userId))

            return "true"

    def getFileSize(self, name):
        if name not in self.files:
            return ""
        else:
            return "{}".format(self.files[name])

    def deleteFile(self, name):
        if name in self.files:
            ret = "{}".format(self.files[name])
            del self.files[name]
            return ret
        else:
            return ""

    def getNLargest(self, prefix, n):

        filteredFiles = list(filter(lambda x: x[0].startswith(prefix), self.files.items()))

        sortedFiles = sorted(filteredFiles, key=lambda x: (-x[1], x[0]))
        ret = []

        if len(sortedFiles) > n:
            ret = sortedFiles[:n]
        else:
            ret = sortedFiles

        return ", ".join(map(lambda x: "{}({})".format(x[0], x[1]), ret))

    def addUser(self, userId, capacity):
        if userId in self.users:
            return "false"
        self.users[userId] = capacity
        self.owner[userId] = []
        return "true"

    def mergeUser(self, userId1, userId2):
        if userId1 not in self.users or userId2 not in self.owner or userId1 == userId2:
            return ""
        filesOwnedBy2 = self.owner[userId2]
        self.owner[userId1] = self.owner[userId1] + filesOwnedBy2
        self.users[userId1] += self.users[userId2]
        del self.owner[userId2]
        del self.users[userId2]
        return "{}".format(self.userQuota(userId1))


def solution(queries):
    s = Solution()
    ret = []
    for query in queries:
        op = query[0]
        if op == 'ADD_FILE':
            name = query[1]
            size = query[2]
            ret.append(s.addFile(name, int(size)))
        elif op == 'GET_FILE_SIZE':
            name = query[1]
            ret.append(s.getFileSize(name))
        elif op == 'DELETE_FILE':
            name = query[1]
            ret.append(s.deleteFile(name))
        elif op == 'GET_N_LARGEST':
            name = query[1]
            n = query[2]
            ret.append(s.getNLargest(name, int(n)))
        elif op == 'ADD_USER':
            userId = query[1]
            capacity = query[2]
            ret.append(s.addUser(userId, int(capacity)))
        elif op == 'ADD_FILE_BY':
            userId = query[1]
            name = query[2]
            size = query[3]
            ret.append(s.addFile(userId, int(size), name))
        elif op == 'MERGE_USER':
            userId1 = query[1]
            userId2 = query[2]
            ret.append(s.mergeUser(userId1, userId2))

    return "\n".join(map(lambda x: str(x), ret))


# queries = [
#   ["ADD_FILE", "/dir1/dir2/file.txt", "10"],
#   ["ADD_FILE", "/dir1/dir2/file.txt", "15"],
#   ["GET_FILE_SIZE", "/dir1/dir2/file.txt"],
#   ["DELETE_FILE", "/non-existing.file"],
#   ["DELETE_FILE", "/dir1/dir2/file.txt"],
#   ["GET_FILE_SIZE", "/non-existing.file"],
# ]

queries = [
    ["ADD_FILE", "/dir/file1.txt", "5"],
    ["ADD_FILE", "/dir/file2", "20"],
    ["ADD_FILE", "/dir/deeper/file3.mov", "9"],
    ["GET_N_LARGEST", "/dir", "2"],
    ["GET_N_LARGEST", "/dir/file", "3"],
    ["ADD_FILE", "/big_file.mp4", "20"],
    ["GET_N_LARGEST", "/", 2],
]

# queries = [
#   ["ADD_USER", "user1", "100"],
#   ["ADD_USER", "user2", "50"],
#   ["ADD_FILE_BY", "/dir/file1.txt", "user1", "90"],
#   ["ADD_FILE_BY", "/dir/file2.txt", "user1", "10"],
#   ["ADD_FILE_BY", "/dir/file3.txt", "user2", "40"],
#   ["MERGE_USER", "user1", "user2"]
# ]
print(solution(queries))

