# cloudStorage
# Instructions
# Solving this task consists of several steps. Subsequent steps will open when the current step is correctly solved. You always have access to the data, such as descriptions and tests, for the current and all previous steps. Partial credit will be granted for each test passed, so press Submit often to run tests and receive partial credit for passed tests.
#
# Requirements
# Your task is to implement a simple cloud storage system that maps objects (files) to their meta information. Specifically, the storage should maintain files along with some information about them (name, size, etc.). Plan your design according to the level specifications below (current level is in bold):
#
# Level 1: The cloud storage system should support adding new files, retrieving files, and moving files.
# Level 2: The cloud storage system should support displaying the largest files.
# Level 3: The cloud storage system should support file versioning.
# Level 4: The cloud storage system should support deleting and restoring files based on some given prefixes.
# To move to the next level, you need to pass all the tests at this level.
#
# Note
# Each query will only call one operation.
#
#
#
# Level 1
# The cloud storage system should support operations to add and retrieve files.
#
# ADD_FILE <file_name> <size> - should add a new file with the name file_name to the storage. size is the amount of storage required in bytes. If a file with the same name already exists, it should be overwritten. It is guaranteed that file_name is either a name of an existing file or a new correct file name. Returns “overwritten” if a file was overwritten, or “created” otherwise.
#
# GET_FILE_SIZE <file_name> - should return a string representing the size of the file file_name if it exists, or "" otherwise.
#
# MOVE_FILE <name_from> <name_to> - moves file from name_from to name_to. name_from and name_to are guaranteed to be different. If a file with the name name_from doesn’t exist, nothing happens. If name_to already exists, nothing happens. It is guaranteed that name_to is either a name of an existing file or a new correct file name. Returns “true” if the file was successfully moved, or “false” otherwise.
#
# The example below shows how these operations should work (please note the section is scrollable to the right):
#
# queries = [
#   ["ADD_FILE", "/file-a.txt", "4"],
#   ["ADD_FILE", "/file-a.txt", "8"],
#   ["ADD_FILE", "/dir-a/dir-c/file-b.txt", "11"],
#   ["ADD_FILE", "/dir-a/dir-c/file-c.txt", "1"],
#   ["ADD_FILE", "/dir-b/file-f.txt", "3"],
#   ["GET_FILE_SIZE", "/file-a.txt"],
#   ["GET_FILE_SIZE", "/file-c.txt"],
#   ["MOVE_FILE", "/dir-b/file-f.txt", "/dir-b/file-e.txt"],
#   ["MOVE_FILE", "/dir-b/file-a.txt", "/dir-b/file"],
#   ["MOVE_FILE", "/file-a.txt", "/dir-b/file-e.txt"]
# ]
# The output should be ["created", "overwritten", "created", "created", "created", "8", "", "true", "false", "false"].
#
#
#
# Level 2
# Implement a method for retrieving some statistics about files with a specific prefix.
#
# GET_LARGEST_N <file_prefix> <n> - should return a string representing the names of the top n largest files with names starting with <file_prefix> in the following format: <file_name_1>(<size_1>), <file_name_2>(<size_2>), .... Returned files should be sorted by size in descending order, or in case of a tie, sorted in lexicographical order of their names. If the number of such files is less than n, all of them should be returned in the specified format.
# The example below shows how these operations should work (please note the section is scrollable to the right):
#
# Queries
# plaintext
# Copy code
# queries = [
#   ["ADD_FILE", "/dir/file1.txt", "5"],
#   ["ADD_FILE", "/dir/file2", "20"],
#   ["ADD_FILE", "/dir/deeper/file3.mov", "9"],
#   ["GET_LARGEST_N", "/dir", "2"],
#   ["GET_LARGEST_N", "/dir/file", "3"],
#   ["GET_LARGEST_N", "/another_dir", "file.txt"],
#   ["ADD_FILE", "/big_file.mp4", "20"],
#   ["GET_LARGEST_N", "/", "2"],
# ]
# The output should be ["created", "created", "created", "/dir/file2(20), /dir/deeper/file3.mov(9)", "/dir/file2(20), /dir/deeper/file3.mov(9), /dir/file1.txt(5)", ""].
#
#
#
#
#
# Level 3
# Implement support for versioning.
#
# Overwriting a file should increment its version by 1, starting from 1.
#
# Just as in Level 1, ADD_FILE should still add a file to storage. If a file with the same name already exists at file_name, it should be overwritten and the operation should return “overwritten”, or return “created” otherwise. When overwriting existing files, the previous versions of the file should be kept. Same guarantees to the input apply.
#
# Similarly, MOVE_FILE should do nothing when name_to already exists or when name_from does not exist (and should return false), but it should move all versions of the file otherwise (and return true). Same guarantees to the input apply.
#
# GET_VERSION <file_name> <version> - returns the size of the specified version of the specified file as a string. If the file with the name file_name does not exist, or if the specified version is greater than the latest version, return "".
#
# GET_FILE_SIZE and GET_LARGEST_N should reference the latest version of each file.
#
# DELETE_VERSION <file_name> <version> - deletes the specified version of the file. If the file with the name file_name or the file version does not exist, returns false, otherwise returns true. Note that after deleting the specified version, all higher versions should decrease their version number by one. If the only version of the file is deleted, the file is permanently removed.
#
# The example below shows how these operations should work (please note the section is scrollable to the right):
#
# Queries
# plaintext
# Copy code
# queries = [
#   ["ADD_FILE", "/file-a.txt", "6"],
#   ["ADD_FILE", "/file-a.txt", "3"],
#   ["GET_VERSION", "/file-a.txt", "2"],
#   ["GET_VERSION", "/file-a.txt", "4"],
#   ["GET_VERSION", "/file-a.txt", "1"],
#   ["DELETE_VERSION", "/file-a.txt", "1"],
#   ["GET_VERSION", "/file-a.txt", "1"],
# ]
# The output should be ["created", "overwritten", "6", "3", "", "true", "false", "3"].
#
#
#
#
#
# Level 4
# Implement support for deleting and restoring files based on a given prefix.
#
# DELETE_FILES <prefix> - moves all versions of all files with the specified prefix to the trash. Returns the number of deleted files as a string. If such files do not exist, returns “0”. If the trash already contains a file with the same name as a file which should be deleted, then the existing file in the trash and all its versions are permanently removed, and the newly deleted file and all its versions are placed in the trash.
#
# Note: Deleting the only version of a file using DELETE_VERSION is not equivalent to moving to trash. In that case, the file is permanently removed.
#
# RESTORE_FILES <prefix> - restores all versions of all files with the specified prefix from the trash. Returns the number of restored files as a string. If such files do not exist in the trash, returns “0”. If the filesystem already contains a file with the same name as a file which should be restored, then the existing file in the filesystem and all its versions are permanently removed, and the newly restored file and all its versions are placed in the filesystem.
#
# The example below shows how these operations should work:
#
# Queries
# plaintext
# Copy code
# queries = [
#   ["ADD_FILE", "/dir1/dir2/a.txt", "3"],
#   ["ADD_FILE", "/dir1/b.txt", "1"],
#   ["DELETE_FILES", "/dir1"],
#   ["GET_FILE_SIZE", "/dir1/dir2/a.txt"],
#   ["RESTORE_FILES", "/dir1/dir2"],
#   ["GET_FILE_SIZE", "/dir1/dir2/a.txt"]
# ]
# The output should be ["created", "created", "2", "", "1", "3"].
#
class Solution:
    def __init__(self):
        # {name: {version: size}}
        self.files = {}

        # {name: {version: size}}
        self.trash = {}

    def addFile(self, fileName, size):
        if fileName in self.files:
            prevVersion = sorted(self.files[fileName].keys())[-1]
            self.files[fileName][prevVersion + 1] = int(size)
            return "overwritten"
        else:
            self.files[fileName] = {1: int(size)}
            return "created"

    def getFileSize(self, fileName):
        if fileName in self.files:
            prevVersion = sorted(self.files[fileName].keys())[-1]
            return self.files[fileName][prevVersion]
        else:
            return ""

    def moveFile(self, nameFrom, nameTo):
        if (nameFrom not in self.files) or (nameTo in self.files):
            return "false"
        else:
            self.files[nameTo] = self.files[nameFrom]
            del self.files[nameFrom]
            return "true"

    def getLargestN(self, filePrefix, n):
        filteredFiles = filter(lambda x: x[0].startswith(filePrefix), self.files.items())
        sortedNameSizePairs = list(sorted(filteredFiles, key=lambda x: (-x[1][sorted(x[1].keys())[-1]], x[0])))
        result = []
        if len(sortedNameSizePairs) >= n:
            result = sortedNameSizePairs[:n]
        else:
            result = sortedNameSizePairs
        return ", ".join(list(map(lambda x: "{}({})".format(x[0], x[1][sorted(x[1].keys())[-1]]), result)))

    def getVersion(self, fileName, version):
        if not fileName in self.files:
            return ""
        prevVersion = sorted(self.files[fileName].keys())[-1]
        if int(version) > prevVersion:
            return ""
        return self.files[fileName][version]

    def deleteVersion(self, fileName, version):
        if not fileName in self.files:
            return "false"
        if not version in self.files[fileName]:
            return "false"
        del self.files[fileName][version]
        if not self.files[fileName]:
            del self.files[fileName]
            return "true"
        for v in sorted(self.files[fileName].keys()):
            if v > version:
                self.files[fileName][v - 1] = self.files[fileName][v]
        lastV = sorted(self.files[fileName].keys())[-1]
        del self.files[fileName][lastV]
        return "true"

    def deleteFiles(self, prefix):
        toDeletedFiles = list(map(lambda x: x[0], filter(lambda x: x[0].startswith(prefix), self.files.items())))
        for file in toDeletedFiles:
            self.trash[file] = self.files[file]
            del self.files[file]
        return str(len(toDeletedFiles))

    def restoreFiles(self, prefix):
        toRestoreFiles = list(map(lambda x: x[0], filter(lambda x: x[0].startswith(prefix), self.trash.items())))
        for file in toRestoreFiles:
            self.files[file] = self.trash[file]
            del self.trash[file]
        return str(len(toRestoreFiles))


def solution(queries):
    s = Solution()
    ret = []
    for query in queries:
        op = query[0]
        if op == 'ADD_FILE':
            fileName = query[1]
            size = query[2]
            ret.append(s.addFile(fileName, size))
        elif op == 'GET_FILE_SIZE':
            fileName = query[1]
            ret.append(s.getFileSize(fileName))
        elif op == 'MOVE_FILE':
            nameFrom = query[1]
            nameTo = query[2]
            ret.append(s.moveFile(nameFrom, nameTo))
        elif op == 'GET_LARGEST_N':
            filePrefix = query[1]
            n = query[2]
            ret.append(s.getLargestN(filePrefix, int(n)))
        elif op == 'GET_VERSION':
            fileName = query[1]
            version = query[2]
            ret.append(s.getVersion(fileName, int(version)))
        elif op == 'DELETE_VERSION':
            fileName = query[1]
            version = query[2]
            ret.append(s.deleteVersion(fileName, int(version)))
        elif op == 'DELETE_FILES':
            prefix = query[1]
            ret.append(s.deleteFiles(prefix))
        elif op == 'RESTORE_FILES':
            prefix = query[1]
            ret.append(s.restoreFiles(prefix))

    return "\n".join(map(lambda x: str(x), ret))

if __name__ == '__main__':
    # queries = [
    #   ["ADD_FILE", "/file-a.txt", "4"],
    #   ["ADD_FILE", "/file-a.txt", "8"],
    #   ["ADD_FILE", "/dir-a/dir-c/file-b.txt", "11"],
    #   ["ADD_FILE", "/dir-a/dir-c/file-c.txt", "1"],
    #   ["ADD_FILE", "/dir-b/file-f.txt", "3"],
    #   ["GET_FILE_SIZE", "/file-a.txt"],
    #   ["GET_FILE_SIZE", "/file-c.txt"],
    #   ["MOVE_FILE", "/dir-b/file-f.txt", "/dir-b/file-e.txt"],
    #   ["MOVE_FILE", "/dir-b/file-a.txt", "/dir-b/file"],
    #   ["MOVE_FILE", "/file-a.txt", "/dir-b/file-e.txt"]
    # ]

    # queries = [
    #   ["ADD_FILE", "/dir/file1.txt", "5"],
    #   ["ADD_FILE", "/dir/file2", "20"],
    #   ["ADD_FILE", "/dir/deeper/file3.mov", "9"],
    #   ["GET_LARGEST_N", "/dir", "2"],
    #   ["GET_LARGEST_N", "/dir/file", "3"],
    #   ["GET_LARGEST_N", "/another_dir", "1"],
    #   ["ADD_FILE", "/big_file.mp4", "20"],
    #   ["GET_LARGEST_N", "/", "2"],
    # ]

    # queries = [
    #   ["ADD_FILE", "/file-a.txt", "6"],
    #   ["ADD_FILE", "/file-a.txt", "3"],
    #   ["GET_VERSION", "/file-a.txt", "2"],
    #   ["GET_VERSION", "/file-a.txt", "4"],
    #   ["GET_VERSION", "/file-a.txt", "1"],
    #   ["DELETE_VERSION", "/file-a.txt", "1"],
    #   ["GET_VERSION", "/file-a.txt", "1"],
    # ]

    # queries = [
    #   ["ADD_FILE", "/file-a.txt", "6"],
    #   ["ADD_FILE", "/file-a.txt", "3"],
    #   ["ADD_FILE", "/file-b.txt", "9"],
    #   ["ADD_FILE", "/file-b.txt", "10"],
    #   ["MOVE_FILE", "/file-a.txt", "/file-c.txt"],
    #   ["GET_VERSION", "/file-a.txt", "2"],
    #   ["GET_VERSION", "/file-a.txt", "4"],
    #   ["GET_VERSION", "/file-a.txt", "1"],
    #   ["DELETE_VERSION", "/file-a.txt", "1"],
    #   ["GET_VERSION", "/file-a.txt", "1"],
    # ]
    queries = [
        ["ADD_FILE", "/dir1/dir2/a.txt", "3"],
        ["ADD_FILE", "/dir1/b.txt", "1"],
        ["DELETE_FILES", "/dir1"],
        ["GET_FILE_SIZE", "/dir1/dir2/a.txt"],
        ["RESTORE_FILES", "/dir1/dir2"],
        ["GET_FILE_SIZE", "/dir1/dir2/a.txt"]
    ]
    print(solution(queries))