# Implement a function called “cd”,
# which given a PWD and an input path, outputs the directory the operating system should switch to:
# i.e.
# fun cd(pwd: String, input: String): String
# e.g.
# cd("/home/bugs", ".") -> "/home/bugs"
# cd("/home/bugs", "bunny") -> "/home/bugs/bunny"
# cd("/home/bugs", "../daffy") -> "/home/daffy"
# fun cd(pwd: String, input: String, symlinkmap: Map<String, String>): String
# e.g.
# cd("/home/bugs", "lola/../basketball", {"/home/bugs/lola":"/home/lola"}) -> "/home/lola/basketball"
# /home/bugs/lola/basketball -> "/home/lola/basketball"
# "/home/bugs/basketball"
# * 写一个 cd( ) method, 输入: current directory, relative destination, 输出：最终的 path 相当于在 terminal 里 cd xxxx 然后 pwd
# * 第二问：加对 ~ 符号的支持，也就是 user home directory
# * 第三问：加 symbolic link 支持。Given there is a map of symbolic link path and there respective real path.

# cd(/foo/bar, baz, {/foo/bar: /abc}) = /abc/baz
# cd(/foo/bar, baz, {/foo/bar: /abc, /abc: /bcd, /bcd/baz: /xyz}) = /xyz
# dictionary 里有可能有短匹配和长匹配，应该先匹配长的(more specific), 比如：‍
# cd(/foo/bar, baz, {/foo/bar: /abc, /foo/bar/baz: /xyz}) = /xyz

# use a pathStack to save all dirs
# parse the to Path, if starts with ~ or /, clear pathStack and reset, save all dirs to a list toDirs
# for each dir in toDirs, append to pathStack, check with symblink, match the longest prefix
def cd(curPath, toPath, symblinks=None):
    pathStack = []
    if curPath.startswith("/"):
        pathStack = list(filter(lambda x: len(x) > 0, curPath.split("/")))
    elif curPath.startswith("~"):
        pathStack = ["Users", "myId"]
        pathStack = pathStack + list(filter(lambda x: len(x) > 0, curPath[1:].split("/")))
    else:
        raise Exception(f"invalid curPath: {curPath}")

    toDirs = []
    if toPath.startswith("~"):
        pathStack = ["Users", "myId"]
        toDirs = list(filter(lambda x: len(x) > 0, toPath[1:].split("/")))
    elif toPath.startswith("/"):  # /a/b/../../c
        pathStack = []
        toDirs = list(filter(lambda x: len(x) > 0, toPath[1:].split("/")))
    else:  # starts with relative dir names
        toDirs = list(filter(lambda x: len(x) > 0, toPath.split("/")))

    for toDir in toDirs:
        if toDir == ".":
            continue
        elif toDir == "..":
            if pathStack:
                pathStack.pop()
        elif toDir == "~":
            raise Exception("unexpected toDir: ~")  # got some incorrect toPath like /a/~/b
        else:
            pathStack.append(toDir)

        if symblinks:
            curAbsPath = "/" + "/".join(pathStack)
            while True:
                # find the longest matching prefix from the symblinks map
                matchedPrefixesFromLongToShort = sorted([prefix for prefix in symblinks if curAbsPath.startswith(prefix)], key=lambda prefix: len(prefix), reverse=True)
                if matchedPrefixesFromLongToShort:
                    longestPrefix = matchedPrefixesFromLongToShort[0]
                    curAbsPath = symblinks[longestPrefix] + curAbsPath[len(longestPrefix):]  # replace curAbsPath's prefix with symblink
                else:
                    break
            pathStack = list(filter(lambda x: len(x) > 0, curAbsPath.split("/")))

    return "/" + "/".join(pathStack)


def testCD():
    assert "/a" == cd("/a", ".")
    assert "/" == cd("/a", "../..")
    assert "/c/d/e/f" == cd("/a", "../c/d/e/f")
    assert "/home/daffy" == cd("/home/bugs", "../daffy")
    assert "/Users/daffy" == cd("~", "../daffy")
    assert "/Users/myId" == cd("/home/asdf/asdf", "~")
    assert "/Users/myId" == cd("~/bugs", "..")
    assert "/Users/myId/asdf" == cd("~/bugs", "~/asdf")
    assert "/Users/myId" == cd("/", "~")
    assert "/ss" == cd("/a/b/c", "d/e", {"/a/b/c": "/h", "/a/b/c/d": "/f", "/a/b/c/d/e": "/g", "/f/e": "/ss"})

    # /Users/myId
    # /asdf
    # /asdf/e
    assert "/asdf" == cd("/a/", "~/e", {"/Users/myId/e": "/asdf"})

    # cd(/foo/bar, baz, {/foo/bar: /abc, /foo/bar/baz: /xyz}) = /xyz
    assert "/xyz" == cd("/foo/bar", "baz", {"/foo/bar": "/abc", "/foo/bar/baz": "/xyz"})
    print("success")


if __name__ == '__main__':
    testCD()
