# Level 1: The course registration system should support basic operations to create a course in the system and register a student for the course.
# Level 2: support retrieving pairs of students who take at least one course together.
# Level 3: support different types of courses, grading students and computing student Grade Point Averages (GPAs).
# 第三题 - 增加打分功能 每门课可以有两种打分方式：final一次定生死或者traditional。
# 第一种就是每门课记一个期末成绩就行
# 第二种要记期中/quiz/期末三种，AddCredit这个方法要支持两种打分方式
# 还要写一个function查找最高分学生

# Level 4: support retrieving the best student nominees for all university departments.

# You will receive a list of queries to the system, and the final output should be an array of strings representing the returned values of all queries. Each query will only call one operation.
# Level 1 Initially, the course registration system does not contain any courses, so course creation and registration operations are introduced first.
# - CREATE_COURSE - should add a course called with course ID being courseId, weighing credits credits.
# - A course ID consists of 6 symbols - the first 3 are letters and denote the department, and the last three are digits forming a 3-digit number.
# - Credits are simply units that show the amount of coursework. - If there is another course with the same name or , the method should return "false".
# - Otherwise, it should create a course and return "true" . - REGISTER FOR COURSE d courseId> - should register a course with a course ID courseId for a student with a student ID studentId.
# You will receive a list of queries to the system, and the final output should be an array of strings representing the returned values of all queries. Each query will only call one operation.
# Level 1 Initially, the course registration system does not contain any courses, so course creation and registration operations are introduced first. - CREATE_COURSE - should add a course called with course ID being courseId, weighing credits credits. - A course ID consists of 6 symbols - the first 3 are letters and denote the department, and the last three are digits forming a 3-digit number. - Credits are simply units that show the amount of coursework. - If there is another course with the same name or , the method should return "false". - Otherwise, it should create a course and return "true" . - REGISTER FOR COURSE d courseId> - should register a course with a course ID courseId for a student with a student ID studentId. scrollable to the right): Queries queries =[ ["CREATE_COURSE", "CSE220", "System Programming", "3"], ["CREATE_COURSE", "CSE221", "system Programming", "4"], ["CREATE_COURSE", "CSE220", "Computer Architecture", " 3 "], ["CREATE_COURSE", "CSE300", "Introduction to Algorithms", "20"], ["CREATE_COURSE", "CSE330", "Operating systems", "4"], ["REGISTER_FOR_COURSE", "sto01", "CSEZ20"], ["REGISTER_FOR COURSE", "sto01", "CSE220"], ["REGISTER FOR COURSE", "st001", "CSE300"], ["REGISTER FOR_COURSE", "stO01", "CSE330"] ] the output should be ["true", "false", "false", "true", "true", "true", "false", "true", "false"] Input/Output - [execution time limit] 4 seconds (is) - [memory limit] 1 GB - [input] array.array.string queries


class CourseSystem:
    def __init__(self):
        # {cid, [name, credit, type]}
        self.courses = {}
        # {sid, {cid:{component, grade}}
        self.student_course = {}


    def studentCredits(self, sId):
        return sum([self.courseCredit(cId) for cId in self.student_course[sId].keys()])

    def courseCredit(self, cId):
        if cId in self.courses:
            return self.courses[cId][1]
        else:
            return 0

    def registerCourse(self, sId, cId):
        if sId in self.student_course:
            if cId in self.student_course[sId]:
                return "false"
            elif self.studentCredits(sId) + self.courseCredit(cId) > 24:
                return "false"
            else:
                # self.student_course[sId].append(cId)
                # default component, grade
                self.student_course[sId][cId] = {}
                return "true"
        else:
            if self.courseCredit(cId) <= 24:
                self.student_course[sId] = {}
                self.student_course[sId][cId] = {}
                return "true"
            else:
                return "false"

    # def grade(self, sId, cId, points):


    def createCourse(self, cId, cName, cCredit, cType):
        if cId in self.courses:
            return "false"

        if cName in [name_credit[0] for name_credit in self.courses.values()]:
            return "false"

        self.courses[cId] = (cName, int(cCredit), cType)
        return "true"

    def setComponentGrade(self, sId, cId, component, grade):
        if cId not in self.student_course[sId]:
            return "invalid"
        studentGrade = self.student_course[sId][cId]
        if component in studentGrade:
            studentGrade[component] = int(grade)
            return "updated"
        else:
            studentGrade[component] = int(grade)
            return "set"

    def studentPairsWithAtLeastOneCourse(self):
        ret = []
        students = list(self.student_course.keys())
        for s1 in range(0, len(students)):
            for s2 in range(s1+1, len(students)):
                sid = students[s1]
                anotherSid = students[s2]
                if any([c1 in self.student_course[anotherSid].keys() for c1 in self.student_course[sid].keys()]):
                    ret.append((sid, anotherSid))
        return ret

    def getScoreSum(self, sId, cId):
        # return all grades sum
        return sum([score for score in self.student_course[sId][cId].values()])

    def isStandard(self, cId):
        return self.courses[cId][2] == "Standard"
    def getStandardCourse(self, sId):
        courses = [cId for cId in self.student_course[sId].keys() if self.isStandard(cId)]
        return [(self.courses[cId][1], self.getScoreSum(sId, cId)) for cId in courses]

    def getPassCourse(self, sId):
        courses = [cId for cId in self.student_course[sId].keys() if not self.isStandard(cId)]
        return [self.getScoreSum(sId, cId) for cId in courses]

    def hasUngradedCourse(self, sId):
        # {cId: {component, grade}}
        for cId in self.student_course[sId]:
            grades = self.student_course[sId][cId].keys()
            if any(grade not in grades for grade in ["midterm", "final", "homeworks"]):
                return True
        return False

    def getGpa(self, sId):
        if self.hasUngradedCourse(sId):
            return ""
        sum = 0
        credits = 0
        for (credit, grade) in self.getStandardCourse(sId):
            sum += credit * grade
            credits += credit
        gpa = sum // credits

        passed = 0
        failed = 0
        for grade in self.getPassCourse(sId):
            if grade >= 66:
                passed += 1
            else:
                failed += 1

        return "" + str(gpa) + ", " + str(passed) + ", " + str(failed)



def solution(queries):
    c = CourseSystem()
    ret = []
    for query in queries:
        op = query[0]
        if op == 'CREATE_COURSE':
            cid = query[1]
            cname = query[2]
            cCredit = query[3]
            ret.append(
                c.createCourse(cid, cname, cCredit, cType = "Standard")
            )
        elif op == 'CREATE_COURSE_EXT':
            cid = query[1]
            cname = query[2]
            cCredit = query[3]
            cType = query[4] if len(query) == 5 else "Standard"
            ret.append(
                c.createCourse(cid, cname, cCredit, cType)
            )
        elif op == 'REGISTER_FOR_COURSE':
            sid = query[1]
            cid = query[2]
            ret.append(
                c.registerCourse(sid, cid)
            )
        elif op == 'GET_PAIRED_STUDENTS':
            ret.append(
                c.studentPairsWithAtLeastOneCourse()
            )
        elif op == 'SET_COMPONENT_GRADE':
            sId = query[1]
            cId = query[2]
            component = query[3]
            grade = query[4]
            ret.append(
                c.setComponentGrade(sId, cId, component, grade)
            )
        elif op == 'GET_GPA':
            sId = query[1]
            ret.append(
                c.getGpa(sId)
            )

    return ret


if __name__ == '__main__':
    # queries = [
    #     ["CREATE_COURSE", "CSE220", "System Programming", "3", "engineering"],
    #     ["CREATE_COURSE", "CSE221", "System Programming", "4", "engineering"],
    #     ["CREATE_COURSE", "CSE220", "Computer Architecture", "3", "cs"],
    #     ["CREATE_COURSE", "CSE300", "Introduction to Algorithms", "20", "math"],
    #     ["CREATE_COURSE", "CSE330", "Operating Systems", "4", "cs"],
    #     ["CREATE_COURSE", "CSE331", "Computation complexity", "4", "math"],
    #     ["REGISTER_FOR_COURSE", "st001", "CSE220"],
    #     ["REGISTER_FOR_COURSE", "st001", "CSE220"],
    #     ["REGISTER_FOR_COURSE", "st001", "CSE300"],
    #     ["REGISTER_FOR_COURSE", "st001", "CSE300"],
    #     ["REGISTER_FOR_COURSE", "st002", "CSE300"],
    #     ["REGISTER_FOR_COURSE", "st003", "CSE300"],
    #     ["REGISTER_FOR_COURSE", "st004", "CSE301"],
    #     ["REGISTER_FOR_COURSE", "st005", "CSE301"],
    #     ["STUDENT_PARIS_WITH_AT_LEASE_ONE_COURSE"],
    # ]

    queries = [
        ["CREATE_COURSE_EXT", "CSE220", "Data Structures", "3", "Standard"],
        ["CREATE_COURSE_EXT", "CSE300", "Operating Systems", "4"],
        ["CREATE_COURSE_EXT", "CSE330", "Computer Architecture", "3", "Pass/Fail"],
        ["REGISTER_FOR_COURSE", "st001", "CSE220"],
        ["REGISTER_FOR_COURSE", "st001", "CSE330"],
        ["REGISTER_FOR_COURSE", "st002", "CSE330"],
        ["GET_PAIRED_STUDENTS"],
        ["REGISTER_FOR_COURSE", "st002", "CSE220"],
        ["GET_PAIRED_STUDENTS"],
        ["SET_COMPONENT_GRADE", "st002", "CSE220", "homeworks", "20"],
        ["SET_COMPONENT_GRADE", "st002", "CSE220", "homeworks", "25"],
        ["SET_COMPONENT_GRADE", "st002", "CSE300", "homeworks", "25"],
        ["SET_COMPONENT_GRADE", "st002", "BIO777", "homeworks", "25"],
        ["SET_COMPONENT_GRADE", "st002", "CSE220", "midterm", "23"],
        ["SET_COMPONENT_GRADE", "st002", "CSE220", "final", "33"],
        ["GET_GPA", "st002"],
        ["SET_COMPONENT_GRADE", "st002", "CSE330", "homeworks", "25"],
        ["SET_COMPONENT_GRADE", "st002", "CSE330", "midterm", "25"],
        ["SET_COMPONENT_GRADE", "st002", "CSE330", "final", "15"],
        ["GET_GPA", "st002"],
        ["REGISTER_FOR_COURSE", "st002", "CSE300"],
        ["GET_GPA", "st002"],
        ["SET_COMPONENT_GRADE", "st002", "CSE300", "homeworks", "20"],
        ["SET_COMPONENT_GRADE", "st002", "CSE300", "midterm", "20"],
        ["SET_COMPONENT_GRADE", "st002", "CSE300", "final", "35"],
        ["GET_GPA", "st002"]
    ]

    result = solution(queries)
    for r in result:
        print(r)
