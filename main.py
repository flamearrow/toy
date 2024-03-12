# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def raise_some_error():
    # raise ValueError("value error")
    # raise TypeError("type error")
    raise KeyError("key error")


# x is a dict {}
def pass_all_conditions(x, conditions):
    for condition in conditions:
        if condition[0] == "G":
            if x[condition[1]] > condition[2]:
                break
            else:
                return False
        elif condition[0] == "E":
            if x[condition[1]] == condition[2]:
                break
            else:
                return False
        elif condition[0] == "S":
            if x[condition[1]] < condition[2]:
                break
            else:
                return False
    return True

def select_on_where(x, clauses):
    ret = {}
    for key in clauses:
        ret[key] = x[key]
    return ret


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arr = [1,2,3]
    b = [True, False]
    conditions = [("G", "age", 23), ("E", "name", "Tom")]
    clauses = ["name", "age", "address"]
    sorted_key = "age"
    is_asc = True
    b_filtered = list(filter(lambda x: pass_all_conditions(x, conditions), arr))
    b_filtered.sort(key=lambda x: x[sorted_key], reverse=is_asc)
    b_mapped = list(map(lambda x: select_on_where(x, clauses), b_filtered))
    # arr2 = arr[::-1]
    # arr3 = arr[-2:]
    # print(arr3)

    # value = "mlgb"
    # new_value = value[-2::-1]
    # print(new_value)
    #
    # for i in value:
    #     print("i: ", i, " ascii: ", ord(i))

    # toy_dict = {"a": {"blah", "blah"}}
    # # blah.pop("a")
    # for b in toy_dict:
    #     print("b: ", b)

    # toy_list = [1, 2, 3, 4]
    # # toy_array.pop(0)
    # # for i in toy_array:
    # #     print(i)
    #
    # toy_list[0:2] = [7,8,9]
    # # print(toy_list)
    #
    # toyl = [None] * 23
    # for index, item in enumerate(toyl):
    #     if item:
    #         print("index: ", index, " - item: ", item)
    # i = -1
    # if i < 0:
    #     raise ValueError("value is error")
    try:
        raise_some_error()
    except ValueError as e:
        print("error!", e)