def insert(**values):
    for key in values:
        print(key, values[key])




if __name__ == '__main__':
    insert(a="b")
    arr = [{"age" : 24, "weight" : 100, "name" : "tom"}, {"age" : 23, "weight" : 100, "name" : "jerry"}]

    b = set()
    b.add("a")
    b.add("c")

    where = [("age", "G", 23), ("weight", "G", 23)]

    def filterwhere(row):
        for column, op, value in where:
            if op == "G":
                if row[column] <= value:
                    return False
            elif op == "E":
                if row[column] != value:
                    return False
            elif op == "L":
                if row[column] >= value:
                    return False
        return True

    filtered = list(filter(filterwhere, arr))
    print(filtered)
