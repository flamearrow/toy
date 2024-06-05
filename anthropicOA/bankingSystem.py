MILLISECONDS_IN_1_DAY = 86400000

# • Level 1: The banking system should support creating new accounts, depositing money into accounts, and transferring money between two accounts.
# • Level 2: The banking system should support ranking accounts based on the total value of outgoing transactions.
# • Level 3: The banking system should allow scheduling payments and checking the status of scheduled payments
# • Level 4: The banking system should support merging two accounts while retaining both accounts' balance and transaction histories.


# Level 1
# Initially, the banking system does not contain any accounts, so implement operations to allow account creation, deposits, and transfers between 2 different accounts.
# • CREATE ACCOUNT <timestamp> < accountId> — should create a new account with the given identifier if it does not already exist. Returns "true" if the account was successfully created or "false" if an account with accountId already exists.
# • DEPOSIT <timestamp> <accountId> <amount> — should deposit the given amount of money to the specified accountId . Returns a string representing the total amount of money in the account after the query has been processed. If the specified account does not exist, should return an empty string.
# • TRANSFER < timestamp> <sourceAccountId> <targetAccountId> <amount> — should transfer the given amount of money from account sourceAccountId to account targetAccountId . Returns a
# string representing the balance of
# sourceAccountId if the transfer was successful or an empty string otherwise.
# • Returns an empty string if
# sourceAccountId Or targetAccountId doesn't exist.
# • Returns an empty string if
# sourceAccountId and targetAccountId are the same.
# • Returns an empty string if account
# sourceAccountId has insufficient funds to perform the transfer.

# Level 2
# The bank wants to identify people who are not keeping money in their accounts, so implement operations to support ranking accounts based on outgoing transactions.
# • TOP SPENDERS <timestamp> <n> — should return identifiers of the top n accounts with the highest amount of outgoing transactions - the total amount of money either transferred out of or paid/withdrawn (via the SCHEDULE_PAYMENT operation which will be introduced in level 3) - sorted in descending order, or in case of a tie, sorted alphabetically by accountId in ascending order. The output should be a string in the following format: "<accountId1> (<totalOutgoing1>), <accountId2>(<totalOutgoing2>), , <accountIdN>(<totalOutgoingN>)"
# • If less than n accounts exist in the system, then return all their identifiers (in the described format).

# Level 3
# The system should allow scheduling payments and checking the status of scheduled payments.
# SCHEDULE_PAYMENT <timestamp> <accountId> <amount> <delay> — should schedule a payment which will be performed at
# timestamp + delay . Returns a string with a unique identifier for the
# scheduled payment in the following format: "payment [ordinal number of the scheduled payment
# across all accounts]" - e.g., "payment1"
# "payment2", etc. If accountId doesn't exist, should
# return an empty string. The payment is skipped if the specified account has insufficient funds when the payment is performed. Additional conditions:
# • Successful payments should be considered outgoing transactions and included when ranking accounts using the TOP_SPENDERS operation.
# • Scheduled payments should be processed before any other transactions at the given timestamp.
# • If an account needs to perform several scheduled payments simultaneously, they should be processed in order of creation -e.g., "payment1" should be processed before "payment2"
# • CANCEL_PAYMENT <timestamp> <accountId> <paymentId> — should cancel the scheduled payment with paymentId . Returns "true" if the scheduled payment is successfully canceled. If paymentId does not exist or was already canceled, or if accountId is different from the source account for the scheduled payment, returns "false" . Note that scheduled payments must be performed before any
# CANCEL _PAYMENT operations at the given timestamp.

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


class Solution2:
    def __init__(self):
        # support history: {aid: [time: amount]}
        # {aId: amount}
        self.accounts = {}
        # {aid: volume}
        self.volume = {}
        self.transferId = 0
        # {transferId: {expiredAt, source, target, amount}}
        self.transfers = {}

    def createAccount(self, timestamp, accountId):
        if accountId in self.accounts:
            return "false"
        else:
            self.accounts[accountId] = 0
            self.volume[accountId] = 0
            return "true"

    def deposit(self, timestamp, accountId, amount):
        if accountId not in self.accounts:
            return ""
        else:
            self.accounts[accountId] = self.accounts[accountId] + amount
            self.volume[accountId] = self.volume[accountId] + amount
            return str(self.accounts[accountId])

    def pay(self, timestamp, accountId, amount):
        if accountId not in self.accounts:
            return ""
        else:
            if self.accounts[accountId] < amount:
                return ""
            else:
                self.accounts[accountId] = self.accounts[accountId] - amount
                self.volume[accountId] = self.volume[accountId] + amount
                return str(self.accounts[accountId])

    def topActivity(self, timestamp, n):
        sortedAccountByVolume = sorted(self.volume.items(), key=lambda x: (-x[1], x[0]))
        ret = []
        if len(sortedAccountByVolume) > n:
            ret = sortedAccountByVolume[:n]
        else:
            ret = sortedAccountByVolume
        return ", ".join(map(lambda x: "{}({})".format(x[0], x[1]), ret))

    def transfer(self, timestamp, sourceId, targetId, amount):
        if sourceId not in self.accounts or targetId not in self.accounts or sourceId == targetId:
            return ""
        if self.accounts[sourceId] < amount:
            return ""
        self.transferId += 1
        nextTID = self.transferId
        transferId = "transfer{}".format(nextTID)
        self.transfers[transferId] = [timestamp + MILLISECONDS_IN_1_DAY, sourceId, targetId, amount]
        self.volume[sourceId] += amount
        self.volume[targetId] += amount
        return transferId

    def acceptTransfer(self, timestamp, accountId, transferId):
        if transferId not in self.transfers:
            return "false"

        expiredAt, source, target, amount = self.transfers[transferId]

        if expiredAt < timestamp:
            return "false"
        if target != accountId:
            return "false"

        self.accounts[source] -= amount
        self.accounts[target] += amount
        del self.transfers[transferId]
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