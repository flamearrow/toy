# Level 1: In-memory database should support basic operations to manipulate records, fields, and values within fields.
# Level 2: In-memory database should support displaying a specific record's fields based on a filter.
# Level 3: In-memory database should support TTL (Time-To-Live) configurations on database records.
# Level 4: In-memory database should support backup and restore functionality. <- this one
# or Level 4: In-memory database should support look-back operations to retrieve values stored at a specific timestamp in the past.

# currentValues: field, value, ttl
# backuped values: snapshot with value and updated ttl
class Solution:
    def __init__(self):
        # {key: {field: (value, at, ttl)}}
        self.values = {}
        # {ts: {key: {field: (value, ttl}}
        self.backUps = {}

        # {key: {field: {at: value}}
        self.newValues = {}

    def set(self, key, field, value, ts=None, ttl=None):
        if key not in self.values:
            self.values[key] = {}
            self.newValues[key] = {}
        self.values[key][field] = (value, int(ts) if ts else None, int(ttl) if ttl else None)

        if ts:
            # remove all entries when at >= ts
            if field not in self.newValues[key]:
                self.newValues[key][field] = {}
            timeValueDict = self.newValues[key][field]

            timesToRemove = []
            for time in timeValueDict:
                if time >= int(ts):
                    timesToRemove.append(time)
            for time in timesToRemove:
                del timeValueDict[time]
            timeValueDict[int(ts)] = value
            if ttl:
                timeValueDict[int(ts)+int(ttl)] = None

        return ""

    def expired(self, key, field, at):
        if not self.values[key][field][2]:
            return True
        else:
            return int(at) < (self.values[key][field][1] + self.values[key][field][2])

    def get(self, key, field, ts=None):
        if key not in self.values:
            return ""

        if field not in self.values[key]:
            return ""
        if ts:
            if self.expired(key, field, ts):
                return self.values[key][field][0]
        else:
            return self.values[key][field][0]

    def delete(self, key, field, ts=None):
        if key not in self.values:
            return "false"

        if field not in self.values[key]:
            return "false"

        if ts:
            if self.expired(key, field, ts):
                del self.values[key][field]
                return "true"
            else:
                return "false"
        else:
            del self.values[key][field]
            return "true"

    def scan(self, key, ts=None):
        if key not in self.values:
            return ""
        ret = []
        for field in self.values[key]:
            if ts:
                if self.expired(key, field, ts):
                    ret.append("{}({})".format(field, self.values[key][field][0]))
            else:
                ret.append("{}({})".format(field, self.values[key][field][0]))

        return ", ".join(sorted(ret))

    def scanPrefix(self, key, prefix, ts=None):
        if key not in self.values:
            return ""
        ret = []
        for field in self.values[key]:
            if field.startswith(prefix):
                if ts:
                    if self.expired(key, field, ts):
                        ret.append("{}({})".format(field, self.values[key][field][0]))
                else:
                    ret.append("{}({})".format(field, self.values[key][field][0]))

        return ", ".join(sorted(ret))

    def backUp(self, ts): # return number of records, not number of fields
        # scan through the values and save all none expred values
        if not self.values:
            self.backUps = {ts, None}
            return "0"

        # {key: {field: (value, ttl)}} - no "at"
        backUp = {}
        for key in self.values:
            if key not in backUp:
                backUp[key] = {}
            for field in self.values[key]:
                if not self.values[key][field][2]: # no ttl
                    backUp[key][field] = (self.values[key][field][0], None)
                elif self.expired(key, field, ts):  # only add non expired values, minus delta from ttl
                    backUp[key][field] = (self.values[key][field][0], self.values[key][field][2] - int(ts) + self.values[key][field][1])
        self.backUps[ts] = backUp
        return "{}".format(len(backUp))

    # find key closed before ot at tsToRestore
    def restore(self, ts, tsToRestore):
        backupKey = -1
        for i in sorted(self.backUps.keys(), reverse=True):
            if i <= tsToRestore:
                backupKey = i
                break

        # rebuild - updating ttl
        restoredBackUp = self.backUps[backupKey]
        values = {}  # {key: {field: (value, at, ttl)}}
        for key in restoredBackUp:
            if key not in values:
                values[key] = {}
            for field in restoredBackUp[key]:
                # update ttl
                if not restoredBackUp[key][field][1]:
                    values[key][field] = (restoredBackUp[key][field][0], int(ts), None)
                else:
                    values[key][field] = (restoredBackUp[key][field][0], int(ts), restoredBackUp[key][field][1])
        self.values = values
        return ""

    # need to save values
    #  {time: value}
    # when set with {time, value}, add {time, value}
    # when set with {time, value, ttl}, add {time, value}, {time+ttl, None}
    #  for both options, delete all entries with values > time

    def getWhen(self, key, field, atATts, ts):
        # ignore empty cases
        fieldValuesDict = self.newValues[key][field]
        foundTime = -1
        for time in sorted(fieldValuesDict.keys(), reverse=True):
            if time <= int(atATts):
                foundTime = time
                break
        return fieldValuesDict[foundTime] if fieldValuesDict[foundTime] else "None"


def solution(queries):
    s = Solution()
    ret = []
    for query in queries:
        op = query[0]
        if op == 'SET':
            key = query[1]
            field = query[2]
            value = query[3]
            ret.append(s.set(key, field, value))
        elif op == 'GET':
            key = query[1]
            field = query[2]
            ret.append(s.get(key, field))
        elif op == 'DELETE':
            key = query[1]
            field = query[2]
            ret.append(s.delete(key, field))
        elif op == 'SCAN':
            key = query[1]
            ret.append(s.scan(key))
        elif op == 'SCAN_BY_PREFIX':
            key = query[1]
            prefix = query[2]
            ret.append(s.scanPrefix(key, prefix))
        elif op == 'SET_AT':
            key = query[1]
            field = query[2]
            value = query[3]
            ts = query[4]
            ret.append(s.set(key, field, value, ts))
        elif op == 'SET_AT_WITH_TTL':
            key = query[1]
            field = query[2]
            value = query[3]
            ts = query[4]
            ttl = query[5]
            ret.append(s.set(key, field, value, ts, ttl))
        elif op == 'DELETE_AT':
            key = query[1]
            field = query[2]
            ts = query[3]
            ret.append(s.delete(key, field, ts))
        elif op == 'GET_AT':
            key = query[1]
            ts = query[2]
            ret.append(s.get(key, ts))
        elif op == 'SCAN_AT':
            key = query[1]
            ts = query[2]
            ret.append(s.scan(key, ts))
        elif op == 'SCAN_BY_PREFIX_AT':
            key = query[1]
            prefix = query[2]
            ts = query[3]
            ret.append(s.scanPrefix(key, prefix, ts))
        elif op == 'BACKUP':
            ts = query[1]
            ret.append(s.backUp(ts))
        elif op == 'RESTORE':
            ts = query[1]
            tsToRestore = query[2]
            ret.append(s.restore(ts, tsToRestore))
        elif op == 'GET_WHEN': # support lookback at GET operation
            key = query[1]
            field = query[2]
            atTs = query[3]
            ts = query[4]
            ret.append(s.getWhen(key, field, atTs, ts))

    return ret

if __name__ == '__main__':
    # queries = [
    #     ["SET", "A", "BC", "E"],
    #     ["SET", "A", "BD", "F"],
    #     ["SET", "A", "C", "G"],
    #     ["SCAN_BY_PREFIX", "A", "B"],
    #     ["SCAN", "A"],
    #     ["SCAN_BY_PREFIX", "B", "B"],
    # ]

    queries = [
        ["SET_AT_WITH_TTL", "A", "BC", "E", "1", "9"],
        ["SET_AT_WITH_TTL", "A", "BC", "D", "5", "10"],
        ["SET_AT", "A", "BC", "F", "10"],
        ["SET_AT_WITH_TTL", "A", "BC", "G", "11", "5"],
        # ["SCAN_BY_PREFIX_AT", "A", "B", "14"],
        # ["SCAN_BY_PREFIX_AT", "A", "B", "15"],
        # ["GET_WHEN", "A", "BC", "2", "11"],
        ["GET_WHEN", "A", "BC", "5", "12"],
        ["GET_WHEN", "A", "BC", "7", "13"],
        ["GET_WHEN", "A", "BC", "10", "13"],
        ["GET_WHEN", "A", "BC", "15", "20"],
        ["GET_WHEN", "A", "BC", "16", "21"],
        ["GET_WHEN", "A", "BC", "17", "22"],
    ]

    # queries = [
    #     ["SET_AT", "A", "B", "C", "1"],
    #     ["SET_AT_WITH_TTL", "X", "Y", "Z", "2", "15"],
    #     ["GET_AT", "X", "Y", "3"],
    #     ["SET_AT_WITH_TTL", "A", "D", "E", "4", "10"],
    #     ["SCAN_AT", "A", "13"],
    #     ["SCAN_AT", "X", "16"],
    #     ["SCAN_AT", "X", "17"],
    #     ["DELETE_AT", "X", "Y", "20"]
    # ]
    # queries = [
    #     ["SET_AT_WITH_TTL", "A", "B", "C", "1", "10"],
    #     ["BACKUP", "3"],
    #     ["SET_AT", "A", "D", "E", "4"],
    #     ["BACKUP", "5"],
    #     ["DELETE_AT", "A", "B", "8"],
    #     ["BACKUP", "9"],
    #     ["RESTORE", "10", "7"],
    #     ["BACKUP", "11"],
    #     ["SCAN_AT", "A", "15"],
    #     ["SCAN_AT", "A", "16"]
    # ]

    print("\n".join(solution(queries)))