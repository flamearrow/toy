MILLISECONDS_IN_1_DAY = 86400000

# • Level 1: The banking system should support creating new accounts, depositing money into accounts, and transferring money between two accounts.
# • Level 2: The banking system should support ranking accounts based on the total value of outgoing transactions.
# • Level 3: The banking system should allow scheduling payments and checking the status of scheduled payments
# • Level 4: The banking system should support merging two accounts while retaining both accounts' balance and transaction histories.


class Solution:
    def __init__(self):
        # {aId: (amount, {time:transactionVolume})}
        self.accounts = {}
        self.transferCnt = 0
        # {transferId: [from, to, amount, expireAt]}
        self.pendingTransfers = {}

    def createAccount(self, ts, aId):
        if aId in self.accounts:
            return "false"
        else:
            self.accounts[aId] = [0, {}]
            return "true"

    def deposit(self, ts, aId, amt):
        if aId not in self.accounts:
            return ""
        self.accounts[aId][0] = self.accounts[aId][0] + int(amt)
        self.accounts[aId][1][ts] = int(amt)
        return str(self.accounts[aId][0])

    def pay(self, ts, aId, amt):
        if aId not in self.accounts:
            return ""
        if self.accounts[aId][0] - int(amt) <= 0:
            return ""
        self.accounts[aId][0] = self.accounts[aId][0] - int(amt)
        self.accounts[aId][1][ts] = int(amt)
        return str(self.accounts[aId][0])

    def topActivity(self, ts, n):
        toAccoutns = sorted(self.accounts.items(), key=lambda x: (-sum(x[1][1].values()), x[0]))
        topN = toAccoutns[:int(n)] if len(toAccoutns) >= int(n) else toAccoutns
        ret = list(map(lambda pair: "{}({})".format(pair[0], sum(pair[1][1].values())), topN))
        return ", ".join(ret)

    def transfer(self, ts, src, tgt, amount):
        if src == tgt:
            return ""
        if src not in self.accounts or tgt not in self.accounts:
            return ""
        if self.accounts[src][0] < int(amount):
            return ""
        self.transferCnt += 1
        tId = "transfer{}".format(self.transferCnt)
        self.pendingTransfers[tId] = [src, tgt, amount, int(ts) + MILLISECONDS_IN_1_DAY]

        self.accounts[src][1][ts] = int(amount)
        self.accounts[tgt][1][ts] = int(amount)

        return tId

    def accept(self, ts, accountId, transferId):
        if transferId not in self.pendingTransfers:
            return "false"

        src, tgt, amount, expireAt = self.pendingTransfers[transferId]

        if accountId != tgt:
            return "false"
        if expireAt <= int(ts):
            return "false"

        self.accounts[src][0] -= int(amount)
        self.accounts[tgt][0] += int(amount)
        del self.pendingTransfers[transferId]
        return "true"


def solution(queries):
    s = Solution()
    ret = []
    for query in queries:
        op = query[0]
        if op == 'CREATE_ACCOUNT':
            ts = query[1]
            aId = query[2]
            ret.append(s.createAccount(ts, aId))
        elif op == 'DEPOSIT':
            ts = query[1]
            aId = query[2]
            amt = query[3]
            ret.append(s.deposit(ts, aId, amt))
        elif op == 'PAY':
            ts = query[1]
            aId = query[2]
            amt = query[3]
            ret.append(s.pay(ts, aId, amt))
        elif op == 'TOP_ACTIVITY':
            ts = query[1]
            n = query[2]
            ret.append(s.topActivity(ts, n))
        elif op == 'TRANSFER':
            ts = query[1]
            src = query[2]
            tgt = query[3]
            amount = query[4]
            ret.append(s.transfer(ts, src, tgt, amount))
        elif op == 'ACCEPT_TRANSFER':
            ts = query[1]
            accountId = query[2]
            transferId = query[3]
            ret.append(s.accept(ts, accountId, transferId))

    return "\n".join(map(lambda x: str(x), ret))


# queries = [
#     ["CREATE_ACCOUNT", "1", "account1"],
#     ["CREATE_ACCOUNT", "2", "account1"],
#     ["CREATE_ACCOUNT", "3", "account2"],
#     ["DEPOSIT", "4", "non-existing", "2700"],
#     ["DEPOSIT", "5", "account1", "2700"],
#     ["PAY", "6", "non-existing", "2700"],
#     ["PAY", "7", "account1", "2701"],
#     ["PAY", "8", "account1", "200"]
# ]
# queries = [
#     ["CREATE_ACCOUNT", "1", "account1"],
#     ["CREATE_ACCOUNT", "2", "account2"],
#     ["CREATE_ACCOUNT", "3", "account3"],
#     ["DEPOSIT", "4", "account1", "2000"],
#     ["DEPOSIT", "5", "account2", "3000"],
#     ["DEPOSIT", "6", "account3", "4000"],
#     ["TOP_ACTIVITY", "7", "3"],
#     ["PAY", "8", "account1", "1500"],
#     ["PAY", "9", "account2", "250"],
#     ["DEPOSIT", "10", "account3", "250"],
#     ["TOP_ACTIVITY", "11", "3"]
# ]

queries = [
    ["CREATE_ACCOUNT", "1", "account1"],
    ["CREATE_ACCOUNT", "2", "account2"],
    ["DEPOSIT", "3", "account1", "2000"],
    ["DEPOSIT", "4", "account2", "3000"],
    ["TRANSFER", "5", "account1", "account2", "5000"],
    ["TRANSFER", "16", "account1", "account2", "1000"],
    ["ACCEPT_TRANSFER", "20", "account1", "transfer1"],
    ["ACCEPT_TRANSFER", "21", "non-existing", "transfer1"],
    ["ACCEPT_TRANSFER", "22", "account1", "transfer2"],
    ["ACCEPT_TRANSFER", "25", "account2", "transfer1"],
    ["ACCEPT_TRANSFER", "30", "account2", "transfer1"],
    ["TRANSFER", "40", "account1", "account2", "1000"],
    ["ACCEPT_TRANSFER", str(45 + MILLISECONDS_IN_1_DAY), "account2", "transfer2"],
    ["TRANSFER", str(50 + MILLISECONDS_IN_1_DAY), "account1", "account1", "1000"]
]
print(solution(queries))