import json

if __name__ == '__main__':
    with open("test.json", "r") as json_file:
        json_obj = json.load(json_file)

    print(json_obj[0]["name"])
    print(type(json_obj)) # List

    with open("test2.json", "r") as json_file:
        json_obj2 = json.load(json_file)

    print(json_obj2["name"])
    print(type(json_obj2)) # Dict