# industry template
# Instructions
# Your task is to implement a simplified version of a program registering the working hours of contract workers at a facility. All operations that should be supported by this program are described below.
# Solving this task consists of several levels. Subsequent levels are opened when the current level is correctly solved. You always have access to the data for the current and all previous levels.
# Requirements
# Your task is to implement a simplified version of a program registering the working hours of contract workers at a facility. Plan your design according to the level specifications below:
# • Level 1: The working hours register program should support adding workers to the system, registering the time when workers enter or leave the office and retrieving information about the time spent in the office.
# • Level 2: The working hours register program should support retrieving statistics about the amount of time that workers spent in the office.
# • Level 3: The working hours register program should support promoting workers, assigning them new positions and new compensation. The program should also support calculating a worker's salary for a given period.
# • Level 4: The working hours register program should support setting time periods to be double-paid.
# To move to the next level, you need to pass all the tests at this level.
# Note
# You will receive a list of queries to the system, and the final output should be an array of strings representing the returned values of all queries. Each query will only call one operation.
# Level 1
# Introduce operations for adding workers, registering their entering or leaving the office and retrieving information about the amount of time that they have worked.
# • ADD_WORKER <workerId> <position> <compensation> — should add the workerId to the system and save additional information about them: their position and compensation. If the workerId already exists, nothing happens and this operation should return "false". If the workerId was successfully added, return "true". workerId and position are guaranteed to contain only English letters and spaces.
# • REGISTER <workerId> <timestamp> — should register the time when the workerId entered or left the office. The time is represented by the timestamp. Note that REGISTER operation calls are given in the increasing order of the timestamp parameter. If the workerId doesn't exist within the system, nothing happens and this operation should return "invalid_request". If the workerId is not in the office, this operation registers the time when the workerId entered the office. If the workerId is already in the office, this operation registers the time when the workerId left the office. If the workerId's entering or leaving time was successfully registered, return "registered".
# • GET <workerId> — should return a string representing the total calculated amount of time that the workerId spent in the office. The amount of time is calculated using finished working sessions only. It means that if the worker has entered the office but hasn't left yet, this visit is not considered in the calculation. If the workerId doesn't exist within the system, return an empty string.
# Examples
# The example below shows how these operations should work (the section is scrollable to the right):
#
#
# 1111
#
# queries = [
# 	["ADD_WORKER", "Ashley", "Middle Developer", "150"],
#     ["ADD_WORKER", "Ashley", "Junior Developer", "100"],
#     ["REGISTER", "Ashley", "10"],
#     ["REGISTER", "Ashley", "25"],
#     ["GET", "Ashley"],
#     ["REGISTER", "Ashley", "40"],
#     ["REGISTER", "Ashley", "67"],
#     ["REGISTER", "Ashley", "100"],
#     ["GET", "Ashley"],
#     ["GET", "Walter"],
#     ["REGISTER", "Walter", "120"]
# ]
#
# the output should be ["true", "false", "registered", "registered", "15", "registered", "registered", "registered", "42", "", "invalid_request"].
#
# Input/Output
# • [execution time limit] 4 seconds (py3)
# • [memory limit] 1 GB
# • [input] array.array.string queriesAn array of queries to the system. It is guaranteed that all the queries parameters are valid: each query calls one of the operations described in the description, all operation parameters are given in the correct format, and all conditions required for each operation are satisfied.Guaranteed constraints:1 ≤ queries.length ≤ 500.
# • [output] array.stringAn array of strings representing the returned values of queries.
# [Python 3] Syntax Tips
# # Prints help message to the console# Returns a stringdefhelloWorld(name):    print("This prints to the console when you Run Tests")    return"Hello, "+ name
# Level 2
# Introduce an operation to retrieve ordered statistics about the workers.
# • TOP_N_WORKERS <n> <position> — should return the string representing ids of the top n workers with the given position sorted in descending order by the total time spent in the office. The amount of time is calculated using finished working sessions only. In the case of a tie, workers must be sorted in alphabetical order of their ids. The returned string should be in the following format: "workerId1(timeSpentInOffice1), workerId2(timeSpentInOffice2), ..., workerIdN(timeSpentInOfficeN)". If less than n workers with the given position exist within the system, then return all ids in the described format. If there are no workers with the given position within the system, return an empty string. Note that if a worker exists within the system and doesn't have any finished periods of being in the office, their time spent in the office is considered to be 0.
# Examples
# The example below shows how this operation should work (the section is scrollable to the right):
#
# 2222
# queries = [
# 	["ADD_WORKER", "John", "Junior Developer", "120"],
#     ["ADD_WORKER", "Jason", "Junior Developer", "120"],
#     ["ADD_WORKER", "Ashley", "Junior Developer", "120"],
#     ["REGISTER", "John", "100"],
#     ["REGISTER", "John", "150"],
#     ["REGISTER", "Jason", "200"],
#     ["REGISTER", "Jason", "250"],
#     ["REGISTER", "Jason", "275"],
#     ["TOP_N_WORKERS", "5", "Junior Developer"],
#     ["TOP_N_WORKERS", "1", "Junior Developer"],
#     ["REGISTER", "Ashley", "400"],
#     ["REGISTER", "Ashley", "500"],
#     ["REGISTER", "Jason", "575"],
#     ["TOP_N_WORKERS", "3", "Junior Developer"],
#     ["TOP_N_WORKERS", "3", "Middle Developer"]
# ]
#
# the output should be ["true", "true", "true", "registered", "registered", "registered", "registered", "registered", "Jason(50), John(50), Ashley(0)", "Jason(50)", "registered", "registered", "registered", "Jason(350), Ashley(100), John(50)", ""].
# Input/Output
# • [execution time limit] 4 seconds (py3)
# • [memory limit] 1 GB
# • [input] array.array.string queriesAn array of queries to the system. It is guaranteed that all the queries parameters are valid: each query calls one of the operations described in the description, all operation parameters are given in the correct format, and all conditions required for each operation are satisfied.Guaranteed constraints:1 ≤ queries.length ≤ 500.
# • [output] array.stringAn array of strings representing the returned values of queries.
# [Python 3] Syntax Tips
# # Prints help message to the console# Returns a stringdefhelloWorld(name):    print("This prints to the console when you Run Tests")    return"Hello, "+ name
#
# Level 3
# Introduce operations for worker promotion and salary calculation.
# • PROMOTE <workerId> <newPosition> <newCompensation> <startTimestamp> — should register a new position and new compensation for the workerId. newPosition is guaranteed to be different from the current worker's position. New position and new compensation are active from the moment of the first entering the office after or at startTimestamp. In other words, the first time period of being in office for the newPosition is the first time period that starts after or at startTimestamp. startTimestamp is guaranteed to be greater than timestamp parameter of the last REGISTER call for any worker. If the PROMOTE operation is called repeatedly for the same workerId before they entered the office with the newPosition, nothing happens, and this operation should return "invalid_request". If workerId doesn't exist within the system, nothing happens, and this operation should return "invalid_request". If the worker's promotion was successfully registered, return "success".
#
# Note: TOP_N_WORKERS operation should take only the worker's current position into account. GET operation should return the total amount of time across all the worker's past and current positions.
#
#
# • CALC_SALARY <workerId> <startTimestamp> <endTimestamp> — should calculate net salary that workerId has earned for the time period between startTimestamp and endTimestamp. No restrictions are applied to startTimestamp and endTimestamp, except that it is guaranteed that endTimestamp > startTimestamp >= 0. Note that workers are only paid for the time they were present in the office. The amount of time is calculated using finished working sessions only. For any finished working session "sessionStartTimestamp, sessionEndTimestamp" salary is calculated as salary = (sessionEndTimestamp - sessionStartTimestamp) * compensationDuringPeriod. Note, that compensationDuringPeriod may differ for different periods, because workers may be promoted. If workerId doesn't exist within the system, nothing happens and this operation should return an empty string
# Examples
# The example below shows how these operations should work (the section is scrollable to the right):
#
#
# 3333
# queries = [
#     ["ADD_WORKER", "John", "Middle Developer", "200"],
#     ["REGISTER", "John", "100"],
#     ["REGISTER", "John", "125"],
#     ["PROMOTE", "John", "Senior Developer", "500", "200"],
#     ["REGISTER", "John", "150"],
#     ["PROMOTE", "John", "Senior Developer", "350", "250"],
#     ["REGISTER", "John", "300"],
#     ["REGISTER", "John", "325"],
#     ["CALC_SALARY", "John", "0", "500"],
#     ["TOP_N_WORKERS", "3", "Senior Developer"],
#     ["REGISTER", "John", "400"],
#     ["GET", "John"],
#     ["TOP_N_WORKERS", "10", "Senior Developer"],
#     ["TOP_N_WORKERS", "10", "Middle Developer"],
#     ["CALC_SALARY", "John", "110", "350"],
#     ["CALC_SALARY", "John", "900", "1400"]
# ]
#
# the output should be ["true", "registered", "registered", "success", "registered", "invalid_request", "registered", "registered", "35000", "John(0)", "registered", "250", "John(75)", "", "45500", "0"].
# Input/Output
# • [execution time limit] 4 seconds (py3)
# • [memory limit] 1 GB
# • [input] array.array.string queriesAn array of queries to the system. It is guaranteed that all the queries parameters are valid: each query calls one of the operations described in the description, all operation parameters are given in the correct format, and all conditions required for each operation are satisfied.Guaranteed constraints:1 ≤ queries.length ≤ 500.
# • [output] array.stringAn array of strings representing the returned values of queries.
# [Python 3] Syntax Tips
# # Prints help message to the console# Returns a stringdefhelloWorld(name):    print("This prints to the console when you Run Tests")    return"Hello, "+ name
class Solution:
    def __init__(self):
        # need to save history
        # {workerId: [position, comp, promoted]}
        self.workers = {}
        # need to save comp per session
        # {workerId: [[start, end, comp]]}
        self.sessions = {}

    def addWorker(self, workerId, position, comp):
        if workerId in self.workers:
            return "false"
        else:
            self.sessions[workerId] = []
            self.workers[workerId] = [[position, comp, -1]]
            return "true"

    def register(self, workerId, timeStamp):
        if workerId not in self.workers:
            return "invalid_request"
        else:
            if not self.sessions[workerId] or self.sessions[workerId][-1][
                1] != -1:  # sign on, add a new session with current comp
                c = 0
                for position, comp, promoted in sorted(self.workers[workerId], key=lambda x: -x[2]):
                    if promoted <= timeStamp:
                        c = comp
                        break
                self.sessions[workerId].append([timeStamp, -1, c])
            else:  # last session end -1, sign off
                self.sessions[workerId][-1][1] = timeStamp
            return "registered"

    def get(self, workerId):
        if workerId not in self.sessions:
            return ""
        validSesssions = list(filter(lambda x: (x[0] != -1 and x[1] != -1), self.sessions[workerId]))
        return sum(map(lambda x: (x[1] - x[0]), validSesssions))

    def topNWorkers(self, n, position):
        # use their latest
        workerWithPosition = map(lambda x: x[0], filter(lambda x: x[1][-1][0] == position, self.workers.items()))

        # [workerId, [[start, end, comp]]]
        filteredSesssions = filter(lambda x: x[0] in workerWithPosition, self.sessions.items())

        # {worker: time}
        ret = {}
        for workerId, sessions in filteredSesssions:
            ret[workerId] = 0
            for start, end, comp in sessions:
                if comp == self.workers[workerId][-1][1] and end > 0 and start > 0:  # only add the latest comp
                    ret[workerId] = ret[workerId] + (end - start)

        sortedRet = sorted(ret.items(), key=lambda x: -x[1])
        out = []
        if len(sortedRet) <= n:
            out = sortedRet
        else:
            out = sortedRet[:n]

        return ", ".join(map(lambda x: "{}({})".format(x[0], x[1]), out))

    def promote(self, workerId, newPosition, newCompensation, startTimeStamp):
        # if there's a last session with same salay, if no, block this promotion
        lastSessionComp = self.sessions[workerId][-1][2]
        latestComp = self.workers[workerId][-1][1]
        if lastSessionComp != latestComp:
            return "invalid_request"
        self.workers[workerId].append([newPosition, newCompensation, startTimeStamp])
        return "success"

    def calSalary(self, workerId, startTimeStamp, endTimeStamp):
        validSessions = list(filter(lambda x: x[0] != -1 and x[1] != -1, self.sessions[workerId]))
        ret = 0
        for sessionStart, sessionEnd, sessionComp in validSessions:
            overlapStart = max(sessionStart, startTimeStamp)
            overlapEnd = min(sessionEnd, endTimeStamp)
            if overlapEnd > overlapStart:
                ret += (overlapEnd - overlapStart) * int(sessionComp)
        return ret


def solution(queries):
    s = Solution()
    ret = []
    for query in queries:
        op = query[0]
        if op == 'ADD_WORKER':
            workerId = query[1]
            position = query[2]
            comp = query[3]
            ret.append(s.addWorker(workerId, position, comp))
        elif op == 'REGISTER':
            workerId = query[1]
            timeStamp = query[2]
            ret.append(s.register(workerId, int(timeStamp)))
        elif op == 'GET':
            workerId = query[1]
            ret.append(s.get(workerId))
        elif op == 'TOP_N_WORKERS':
            n = query[1]
            position = query[2]
            ret.append(s.topNWorkers(int(n), position))
        elif op == 'PROMOTE':
            workerId = query[1]
            newPosition = query[2]
            newCompensation = query[3]
            startTimeStamp = query[4]
            ret.append(s.promote(workerId, newPosition, newCompensation, int(startTimeStamp)))
        elif op == 'CALC_SALARY':
            workerId = query[1]
            startTimeStamp = query[2]
            endTimeStamp = query[3]
            ret.append(s.calSalary(workerId, int(startTimeStamp), int(endTimeStamp)))

    return "\n".join(map(lambda x: str(x), ret))


# queries = [
# 	["ADD_WORKER", "Ashley", "Middle Developer", "150"],
#     ["ADD_WORKER", "Ashley", "Junior Developer", "100"],
#     ["REGISTER", "Ashley", "10"],
#     ["REGISTER", "Ashley", "25"],
#     ["GET", "Ashley"],
#     ["REGISTER", "Ashley", "40"],
#     ["REGISTER", "Ashley", "67"],
#     ["REGISTER", "Ashley", "100"],
#     ["GET", "Ashley"],
#     ["GET", "Walter"],
#     ["REGISTER", "Walter", "120"]
# ]

# queries = [
# 	["ADD_WORKER", "John", "Junior Developer", "120"],
#     ["ADD_WORKER", "Jason", "Junior Developer", "120"],
#     ["ADD_WORKER", "Ashley", "Junior Developer", "120"],
#     ["REGISTER", "John", "100"],
#     ["REGISTER", "John", "150"],
#     ["REGISTER", "Jason", "200"],
#     ["REGISTER", "Jason", "250"],
#     ["REGISTER", "Jason", "275"],
#     ["TOP_N_WORKERS", "5", "Junior Developer"],
#     ["TOP_N_WORKERS", "1", "Junior Developer"],
#     ["REGISTER", "Ashley", "400"],
#     ["REGISTER", "Ashley", "500"],
#     ["REGISTER", "Jason", "575"],
#     ["TOP_N_WORKERS", "3", "Junior Developer"],
#     ["TOP_N_WORKERS", "3", "Middle Developer"]
# ]

queries = [
    ["ADD_WORKER", "John", "Middle Developer", "200"],
    ["REGISTER", "John", "100"],
    ["REGISTER", "John", "125"],
    ["PROMOTE", "John", "Senior Developer", "500", "200"],
    ["REGISTER", "John", "150"],
    ["PROMOTE", "John", "Senior Developer", "350", "250"],
    ["REGISTER", "John", "300"],
    ["REGISTER", "John", "325"],
    ["CALC_SALARY", "John", "0", "500"],
    ["TOP_N_WORKERS", "3", "Senior Developer"],
    ["REGISTER", "John", "400"],
    ["GET", "John"],
    ["TOP_N_WORKERS", "10", "Senior Developer"],
    ["TOP_N_WORKERS", "10", "Middle Developer"],
    ["CALC_SALARY", "John", "110", "350"],
    ["CALC_SALARY", "John", "900", "1400"]
]

print(solution(queries))
