# industry template

class Solution:
    def __init__(self):
        # account transfers with history
        # {accountId: [time, amount]}
        self.accounts = {}

        # {paymentId: [time, accountId, amount, delay]}
        self.payments = {}

        self.paymentId = 0

    def createAccount(self, timestamp, accountId):
        self.handleSchedule(timestamp)
        if accountId in self.accounts:
            return "false"
        else:
            self.accounts[accountId] = []
            return "true"

    def funds(self, accountId):
        return sum(map(lambda x: x[1], self.accounts[accountId]))

    def deposit(self, timestamp, accountId, amount):
        self.handleSchedule(timestamp)
        if accountId not in self.accounts:
            return "false"
        self.accounts[accountId].append([timestamp, amount])
        return self.funds(accountId)

    def transfer(self, timestamp, sourceAccountId, targetAccountId, amount):
        self.handleSchedule(timestamp)
        if sourceAccountId not in self.accounts or targetAccountId not in self.accounts or sourceAccountId == targetAccountId:
            return ""
        if self.funds(sourceAccountId) < amount:
            return ""

        self.accounts[sourceAccountId].append([timestamp, -amount])
        self.accounts[targetAccountId].append([timestamp, amount])
        return self.funds(sourceAccountId)

    def topSpenders(self, timestamp, n):
        self.handleSchedule(timestamp)
        # accountId, outgoingAmount
        outgoings = []
        for account, history in self.accounts.items():
            outgoingHistory = sum(
                map(
                    lambda x: x[1],
                    filter(lambda x: x[1] < 0, history)
                )
            )
            outgoings.append([account, outgoingHistory])

        sortedOutgoings = sorted(outgoings, key=lambda x: (x[1], x[0]))
        ret = []
        if len(sortedOutgoings) > n:
            ret = sortedOutgoings[:n]
        else:
            ret = sortedOutgoings

        return ", ".join(map(lambda x: "{}({})".format(x[0], abs(x[1])), ret))

    def schedulePayment(self, timestamp, accountId, amount, delay):
        self.handleSchedule(timestamp)
        if accountId not in self.accounts:
            return ""

        self.paymentId += 1
        paymentId = "payment{}".format(self.paymentId)
        self.payments[paymentId] = [timestamp, accountId, amount, delay]
        return paymentId

    def cancelPayment(self, timestamp, accountId, paymentId):
        self.handleSchedule(timestamp)
        if paymentId not in self.payments:
            return "false"
        time, pAccountId, amount, delay = self.payments[paymentId]
        if pAccountId != accountId:
            return "false"
        del self.payments[paymentId]
        return "true"

    def handleSchedule(self, currentTime):
        # [payemntID, [time, accountid, amount, delay]]
        pendingPayments = filter(lambda x: (x[1][0] + x[1][3]) <= currentTime, self.payments.items())
        handledPayments = []
        for payemntID, paymentDetails in pendingPayments:
            time, accountId, amount, delay = paymentDetails
            if self.funds(accountId) >= amount:
                self.accounts[accountId].append([time + delay, -amount])
                handledPayments.append(payemntID)

        for pId in handledPayments:
            del self.payments[pId]


def solution(queries):
    s = Solution()
    ret = []
    for query in queries:
        op = query[0]
        if op == 'CREATE_ACCOUNT':
            timestamp = query[1]
            accountId = query[2]
            ret.append(s.createAccount(int(timestamp), accountId))
        elif op == 'DEPOSIT':
            timestamp = query[1]
            accountId = query[2]
            amount = query[3]
            ret.append(s.deposit(int(timestamp), accountId, int(amount)))
        elif op == 'TRANSFER':
            timestamp = query[1]
            sourceAccountId = query[2]
            targetAccountId = query[3]
            amount = query[4]
            ret.append(s.transfer(int(timestamp), sourceAccountId, targetAccountId, int(amount)))
        elif op == 'TOP_SPENDERS':
            timestamp = query[1]
            n = query[2]
            ret.append(s.topSpenders(int(timestamp), int(n)))
        elif op == 'SCHEDULE_PAYMENT':
            timestamp = query[1]
            accountId = query[2]
            amount = query[3]
            delay = query[4]
            ret.append(s.schedulePayment(int(timestamp), accountId, int(amount), int(delay)))
        elif op == 'CANCEL_PAYMENT':
            timestamp = query[1]
            accountId = query[2]
            paymentId = query[3]
            ret.append(s.cancelPayment(int(timestamp), accountId, paymentId))
    return "\n".join(map(lambda x: str(x), ret))


# queries = [
#     ["CREATE_ACCOUNT", "1", "account1"],
#     ["CREATE_ACCOUNT", "2", "account1"],
#     ["CREATE_ACCOUNT", "3", "account2"],
#     ["DEPOSIT", "4", "non-existing", "2700"],
#     ["DEPOSIT", "5", "account1", "2700"],
#     ["TRANSFER", "6", "account1", "account2", "2701"],
#     ["TRANSFER", "7", "account1", "account2", "200"],
#     ["TRANSFER", "6", "non-existing", "account2", "500"],
# ]


# queries = [
#     ["CREATE_ACCOUNT", "1", "account3"],
#     ["CREATE_ACCOUNT", "2", "account2"],
#     ["CREATE_ACCOUNT", "3", "account1"],
#     ["DEPOSIT", "4", "account1", "2000"],
#     ["DEPOSIT", "5", "account2", "3000"],
#     ["DEPOSIT", "6", "account3", "4000"],
#     ["TOP_SPENDERS", "7", "3"],
#     ["TRANSFER", "8", "account3", "account2", "500"],
#     ["TRANSFER", "9", "account3", "account1", "1000"],
#     ["TRANSFER", "10", "account1", "account2", "2500"],
#     ["TOP_SPENDERS", "11", "3"],
# ]

# queries = [
#     ["CREATE_ACCOUNT", "1", "account1"],
#     ["CREATE_ACCOUNT", "2", "account2"],
#     ["DEPOSIT", "3", "account1", "2000"],
#     ["DEPOSIT", "4", "account2", "3000"],
#     ["SCHEDULE_PAYMENT", "5", "account1", "50", "10"],
#     ["SCHEDULE_PAYMENT", "6", "account2", "1000", "5"],
#     ["SCHEDULE_PAYMENT", "7", "account1", "3000", "7"],
#     ["DEPOSIT", "11", "account2", "5"],
#     ["CANCEL_PAYMENT", "12", "account2", "payment1"],
#     ["CANCEL_PAYMENT", "13", "account1", "payment1"],
#     ["DEPOSIT", "14", "account1", "5"],
#     ["DEPOSIT", "15", "account1", "5"],
# ]

queries = [
    ["CREATE_ACCOUNT", "1", "account1"],
    ["CREATE_ACCOUNT", "2", "account2"],
    ["CREATE_ACCOUNT", "3", "account3"],
    ["DEPOSIT", "4", "account1", "1000"],
    ["DEPOSIT", "5", "account2", "1000"],
    ["DEPOSIT", "6", "account3", "1000"],
    ["SCHEDULE_PAYMENT", "7", "account1", "300", "10"],
    ["SCHEDULE_PAYMENT", "8", "account2", "400", "10"],
    ["TOP_SPENDERS", "15", "3"],
    ["TOP_SPENDERS", "20", "3"],
]
print(solution(queries))
