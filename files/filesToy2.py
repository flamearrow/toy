import json

if __name__ == '__main__':
    with open("test2.json", "r") as jsonFile:
       obj = json.load((jsonFile))

    if isinstance(obj, list):
        print("got a list")
        sortedObj = sorted(obj, key=lambda x: x["age"])
        print("\n".join(["{} : {}".format(x["name"], x["age"]) for x in sortedObj]))
    elif isinstance(obj, dict):
        print("got a dict")