# ========================================================================================================
# PART I
# ========================================================================================================

# Halloween is coming and some users want to coordinate Roblox costumes with their friends.
# A costume consists of 1 Shirt and 1 Pants.
# Everyone in the group needs to wear the same shirt and same pants.


# Given a dictionary of items owned by users (assumption: users don't own duplicate items):
# e.g.
#   {
#     "user1": ["shirt1", "shirt2", "pants1", "pants2"],
#     "user2": ["shirt1", "pants1", "pants2", "pants3"]
#   }

# and a dictionary of item to type (either "shirt" or "pants"):
# e.g.
#   {
#     "shirt1": "shirt",
#     "shirt2": "shirt",
#     "pants1": "pants",
#     "pants2": "pants",
#     "pants3": "pants"
#   }

# Please print all possible costumes (1 shirt + 1 pants) that the whole group has!
# e.g.
#     shirt1, pants1
#     shirt1, pants2

# void possibleGroupCostumes(HashMap<String, List<String>> userItems, HashMap<String, String> itemTypes);

# ========================================================================================================
# PART II
# ========================================================================================================

# Costumes can also include accessories, e.g. hats.

# e.g.

# userItems:
#   {
#     "user1": ["shirt1", "pants1", "hat1", "shoes1", "socks1"],
#     "user2": ["shirt1", "pants1", "hat2", "shoes1"]
#   }

# itemTypes:
#   {
#     "shirt1": "shirt",
#     "pants1": "pants",
#     "pants2": "pants",
#     "hat1": "hat",
#     "hat2": "hat",
#     "shoes1": "shoes",
#     "socks1": "socks"
#   }

# Users in a group must wear every type of accessory that they all have.

# i.e.
#   If everyone has a hat, everyone must wear a hat.
#   If someone does not have a hat, nobody can wear a hat.

# Please modify your function to print one possible costume for each member of the group.

# e.g.
#     user1: shirt1, pants1, hat1, shoes1      # User 1 cannot wear socks because User 2 does not have socks
#     user2: shirt1, pants1, hat2, shoes1      # User 1 and 2 can both wear hats and shoes

# import requests
# import mysql.connector
# import pandas as pd

def findCombinations(users, itemTypes):
    shirts = set()
    pants = set()
    for user in users:
        items = users[user]
        for item in items:
            if itemTypes[item] == "shirt":
                shirts.add(item)
            else:
                pants.add(item)

    sharedShirts = list(filter(lambda x: all(x in i[1] for i in users.items()), shirts))
    sharedPants = list(filter(lambda x: all(x in i[1] for i in users.items()), pants))

    for shirt in sharedShirts:
        for pant in sharedPants:
            print(shirt, ", ", pant)


def findCombinations2(users, itemTypes):
    allTypes = set()
    for user in users:
        items = users[user]
        for item in items:
            allTypes.add(itemTypes[item])

    sharedTypes = list(
        filter(lambda x: all(x in map(lambda itemName: itemTypes[itemName], i[1]) for i in users.items()), allTypes))

    for user in users:
        remainedTypes = list(sharedTypes)
        result = []
        for item in users[user]:
            if itemTypes[item] in remainedTypes:
                result.append(item)
                remainedTypes.remove(itemTypes[item])
        print(user, ": ", ", ".join(result))


# findCombinations(
#     {
#         "user1": ["shirt1", "shirt2", "pants1", "pants2"],
#         "user2": ["shirt1", "pants1", "pants2", "pants3"]
#     },
#     {
#         "shirt1": "shirt",
#         "shirt2": "shirt",
#         "pants1": "pants",
#         "pants2": "pants",
#         "pants3": "pants"
#     }
# )


findCombinations2(
    {
        "user1": ["shirt1", "pants1", "hat1", "shoes1", "socks1"],
        "user2": ["shirt1", "pants1", "hat2", "shoes1"]
    },
    {
        "shirt1": "shirt",
        "pants1": "pants",
        "pants2": "pants",
        "hat1": "hat",
        "hat2": "hat",
        "shoes1": "shoes",
        "socks1": "socks"
    }
)