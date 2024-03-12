# Scenario
# Your task is to implement a simplified version of a file hosting service.
# All operations that should be supported are listed below. Partial credit will be granted for each test passed, so
# press “Submit” often to run tests and receive partial credits for passed tests. Please check tests for requirements
# and argument types.
# Implementation Tips
# Read the question all the way through before you start coding, but implement the operations and complete the
# levels one by one, not all together, keeping in mind that you will need to refactor to support additional function-
# ality.
# Please, do not change the existing method signatures.




# Level 1 – Initial Design & Basic Functions

# class FileNode:
#     type # file or dir
#     name # file name
#     size # size if not dir
#     children # other files
#     created # time created
#     ttl # time to live, can be None

from enum import Enum


class FileType(Enum):
    FILE = 0
    DIR = 1


class FileNode:
    def __init__(self, file_type, name, size=0, children=None, created=None, ttl=None):
        if children is None:
            children = []
        self.file_type = file_type
        self.name = name
        self.size = size
        self.children = children
        self.parent = None
        self.created = created
        self.ttl = ttl
        # tuple (created, size) of previous values
        self.history = []
        if file_type == FileType.FILE:
            self.history.append((created, size))

    def find_file(self, full_file_name):
        currentNode = self
        lastIndex = 0
        file_paths = full_file_name.split("/")

        nextNode = currentNode.has_sub_dir(file_paths[lastIndex])
        # search/add paths all the way to file name
        while nextNode:
            lastIndex += 1
            currentNode = nextNode
            nextNode = currentNode.has_sub_dir(file_paths[lastIndex])

        return currentNode.get_sub_file(file_paths[lastIndex])

    # return False if file already exists
    def insert_file(self, full_file_name, size, timestamp=None, ttl=None):
        currentNode = self
        lastIndex = 0
        file_paths = full_file_name.split("/")

        nextNode = currentNode.has_sub_dir(file_paths[lastIndex])
        # search/add paths all the way to file name
        while nextNode:
            lastIndex += 1
            currentNode = nextNode
            nextNode = currentNode.has_sub_dir(file_paths[lastIndex])

        while lastIndex < len(file_paths) - 1:
            currentNode = currentNode.add_child_dir(file_paths[lastIndex])
            lastIndex += 1

        # check and add file name
        leaf_name = file_paths[-1]
        # exhausted, now just add file
        if currentNode.get_sub_file(leaf_name):
            return False
        else:
            currentNode.add_child_file(leaf_name, child_file_size=size, timestamp=timestamp, ttl=ttl)
            return True

    # assuming file exisit
    def remove_file_without_updating_history(self, full_file_name):
        currentNode = self
        lastIndex = 0
        file_paths = full_file_name.split("/")

        nextNode = currentNode.has_sub_dir(file_paths[lastIndex])
        # search/add paths all the way to file name
        while nextNode:
            lastIndex += 1
            currentNode = nextNode
            nextNode = currentNode.has_sub_dir(file_paths[lastIndex])

        leaf_file = currentNode.get_sub_file(file_paths[lastIndex])
        if leaf_file:
            currentNode.children.remove(leaf_file)
        else:
            raise ValueError("No file found: ", full_file_name)

    def remove_from_parent(self):
        if self.parent:
            self.parent.children.remove(self)
            self.parent = None
        else:
            raise ValueError("no parent!")

    def has_sub_dir(self, sub_dir_name):
        if self.file_type == FileType.DIR:
            for sub_node in self.children:
                if sub_node.file_type == FileType.DIR and sub_node.name == sub_dir_name:
                    return sub_node
        return None

    def get_sub_file(self, sub_file_name):
        if self.file_type == FileType.DIR:
            for sub_node in self.children:
                if sub_node.file_type == FileType.FILE and sub_node.name == sub_file_name:
                    return sub_node
        return None

    def add_child_dir(self, child_dir_name):
        sub_dir = FileNode(file_type=FileType.DIR, name=child_dir_name)
        self.children.append(sub_dir)
        sub_dir.parent = self
        return sub_dir

    def add_child_file(self, child_file_name, child_file_size=0, timestamp=None, ttl=None):
        sub_file = FileNode(file_type=FileType.FILE, name=child_file_name, size=child_file_size, created=timestamp, ttl=ttl)
        self.children.append(sub_file)
        sub_file.parent = self
        return sub_file

    def find_files_with_prefix(self, prefix):
        results = []
        self.find_files_with_recur(prefix, results)
        return results

    def find_files_with_recur(self, prefix, results):
        if self.file_type == FileType.FILE:
            if self.name.startswith(prefix):
                results.append(self)
        else:
            for node in self.children:
                node.find_files_with_recur(prefix, results)

    def is_alive(self, querytime):
        if self.ttl:
            return (querytime-self.created) <= self.ttl
        else:
            return True

    def update_with_history(self, new_created, new_size=None):
        self.created = new_created
        self.size = new_size if new_size else self.size
        self.history.append((self.created, self.size))

    # returns true if it has history before timestamp
    def revert_back_to_time(self, timestamp):
        # tuple is (created, size), sort based on created
        sorted_history = sorted(self.history, key=lambda history_node_tuple: history_node_tuple[0], reverse=True)
        while sorted_history and sorted_history[0][0] > timestamp:
            sorted_history.pop(0)

        if sorted_history:
            self.created = sorted_history[0][0]
            self.size = sorted_history[0][1]
            return True
        else:
            return False

    # for all sub files and dirs, check history - revert to the first value that has created <= timestamp
    # if can't find one, remove this file
    def rollback(self, timestamp):
        for file_node in self.all_leaves():
            can_rewind = file_node.revert_back_to_time(timestamp)
            if not can_rewind:
                print("should remove: {}, created at {}".format(file_node.name, file_node.created))
                file_node.remove_from_parent()

    def all_leaves(self):
        ret = []
        for child in self.children:
            if child.file_type == FileType.FILE:
                ret.append(child)
            else:
                ret.extend(child.all_leaves())
        return ret


    def print_self(self, indent=""):
        info = (
            "{}{} -type:{} -size:{}".format(indent, self.name, self.file_type, self.size)
            if self.file_type == FileType.FILE
            else
            "{}{} -type:{}".format(indent, self.name, self.file_type)
        )
        if self.created:
            info += " -created:" + str(self.created)
        if self.ttl:
            info += " -ttl:" + str(self.ttl)
        print(info)

    def ll(self, level=0):
        indent = " " * (level + 1)
        self.print_self(indent)
        for child in self.children:
            child.ll(level+1)


fileRoot = FileNode(file_type=FileType.DIR, name="ROOT")


# • FILE_UPLOAD(file_name, size)
# ○ Upload the file to the remote storage server
# ○ If a file with the same name already exists on the server, throws a runtime exception
def FILE_UPLOAD(file_name, size, timestamp=None, ttl=None):
    existing_file = FILE_GET(file_name)
    if existing_file:
        raise ValueError(file_name, " already exists!")
    else:
        fileRoot.insert_file(file_name, size, timestamp=timestamp, ttl=ttl)


# • FILE_GET(file_name)
# ○ Returns size of the file, or nothing if the file doesn’t exist
def FILE_GET(file_name):
    leafNode = fileRoot.find_file(file_name)
    if leafNode:
        return leafNode.size
    else:
        return None


# • FILE_COPY(source, dest)
# ○ Copy the source file to a new location
# ○ If the source file doesn’t exist, throws a runtime exception
# ○ If the destination file already exists, overwrites the existing file
# copy inside of the tree
def FILE_COPY(source, dest):
    # if source and dest are under same dir, then directly update
    existingSrc = fileRoot.find_file(source)
    if existingSrc:
        existingDest = fileRoot.find_file(dest)
        if existingDest:
            existingDest.update_with_history(existingSrc.created, existingSrc.size)
        else:
            fileRoot.insert_file(dest, existingSrc.size, timestamp=existingSrc.created)
    else:
        raise ValueError(source, "not found")


# Level 2 – Data Structures & Data Processing
# • FILE_SEARCH(prefix)
# ○ Find top 10 files starting with the provided prefix. Order results by their size in descending
# order, and in case of a tie by file name.
# search from the tree, return
def FILE_SEARCH(prefix):
    results = fileRoot.find_files_with_prefix(prefix)
    sorted_results = sorted(results, key=lambda node: (node.size, node.name))
    return sorted_results[:10]


# Level 3 – Refactoring & Encapsulation
# Files now might have a specified time to live on the server. Implement extensions of existing methods which in-
# herit all functionality but also with an additional parameter to include a timestamp for the operation, and new
# files might specify the time to live - no ttl means lifetime being infinite.
# • FILE_UPLOAD_AT(timestamp, file_name, file_size)
# • FILE_UPLOAD_AT(timestamp, file_name, file_size, ttl)
# ◦ The uploaded file is available for ttl seconds.
# • FILE_GET_AT(timestamp, file_name)
# • FILE_COPY_AT(timestamp, file_from, file_to)
# • FILE_SEARCH_AT(timestamp, prefix)
# ◦ Results should only include files that are still “alive”


# call FILE UPLOAD, get the node, update uploaded time and ttl
# add timesstamp and ttl in FileNode, with ttl possibly being None
def FILE_UPLOAD_AT(timestamp, file_name, file_size, ttl=None):
    FILE_UPLOAD(file_name=file_name, timestamp=timestamp, size=file_size, ttl=ttl)


# return files with either non ttl, or timestamp - fileNode.timestamp >= ttl
def FILE_GET_AT(timestamp, file_name):
    f = FILE_GET(file_name)
    if f:
        return f.is_alive(timestamp)
    else:
        return False


# copy everything but timestamp
def FILE_COPY_AT(timestamp, file_from, file_to):
    # if source and dest are under same dir, then directly update
    existingSrc = fileRoot.find_file(file_from)
    if existingSrc:
        existingDest = fileRoot.find_file(file_to)
        if existingDest:
            existingDest.update_with_history(timestamp, existingSrc.size)
        else:
            fileRoot.insert_file(file_to, existingSrc.size, timestamp)
    else:
        raise ValueError(file_from, "not found")


# search prefix, filter out with files with either non ttl, or timestamp - fileNode.timestampe >= ttl
def FILE_SEARCH_AT(timestamp, prefix):
    files = FILE_SEARCH(prefix)
    filtered_files = [file for file in files if file.is_alive(timestamp)]
    return filtered_files



# Level 4 – Extending Design & Functionality
# • ROLLBACK(timestamp)
# ◦ Rollback the state of the file storage to the state specified in the timestamp
# ◦ All ttls should be recalculated accordingly

# each file needs to have history, pop back to the history value
def ROLLBACK(timestamp):
    fileRoot.rollback(timestamp)

# Task
# Example of fire structure with various files:
# 1 ----- [server34] ----- 24000 Bytes Limit -------
# 2 ----------------------- Size -------
# 3 +- file-1.zip 4321 Bytes
# 4 +- dir-a
# 5 | +- dir-c
# 6 | | +- file-2.txt 1100 Bytes
# 7 | | +- file-3.csv 2122 Bytes
# 8 +- dir-b
# 9 | +- file-4.mdx 3378 Bytes

if __name__ == '__main__':
    # FILE_UPLOAD("fil1e-1.zip", 1234)
    # FILE_UPLOAD("dir-a/dir-e/file-4.txt", 2345)
    # FILE_UPLOAD("dir-a/dir-c/file-2.txt", 3456)
    # FILE_UPLOAD("dir-a/dir-c/file-3.txt", 4567)
    # FILE_COPY("dir-a/dir-c/file-2.txt", "dir-a/dir-e/file-1.txt")
    # FILE_COPY("dir-a/dir-c/file-2.txt", "dir-a/dir-c/file-3.txt")
    # v = FILE_GET("dir-a/dir-c/file-3.txt")
    # print(v)
    # for fileNode in FILE_SEARCH("file"):
    #     print(fileNode.name, "with size", fileNode.size)
    FILE_UPLOAD_AT(10, "fil1e-1.zip", 100, ttl=90)
    FILE_UPLOAD_AT(20, "dir-a/dir-e/file-4.txt", 200, ttl=150)
    FILE_UPLOAD_AT(30,"dir-a/dir-c/file-2.txt", 150, 50)
    FILE_UPLOAD_AT(40,"dir-a/dir-c/file-3.txt", 199, 100)
    FILE_UPLOAD_AT(timestamp=50, file_name="dir-a/dir-uploaded-at/file-11.txt", file_size=100, ttl=99)
    FILE_UPLOAD_AT(timestamp=60, file_name="dir-a/dir-uploaded-at/file-2.txt", file_size=90)
    FILE_COPY_AT(70, "dir-a/dir-c/file-2.txt", "dir-a/dir-e/file-1.txt")
    FILE_COPY_AT(80, "dir-a/dir-c/file-2.txt", "dir-a/dir-c/file-3.txt")
    # fileRoot.remove_file_without_updating_history("dir-a/dir-c/file-3.txt")
    # fileRoot.remove_file_without_updating_history("dir-a/dir-uploaded-at/file-2.txt")
    fileRoot.ll()
    ROLLBACK(35)
    print("-----after rollback-----")
    fileRoot.ll()



