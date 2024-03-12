class Row:
    def __init__(self, row_id, **values):
        self.row_id = row_id
        self.values = values

    def update_values(self, **new_values):
        for column in new_values:
            self.values[column] = new_values[column]

    def get(self, column_name):
        if column_name in self.values:
            return self.values[column_name]
        else:
            return None


class CourseDB:
    def __init__(self):
        self.next_registered_id = 0
        # course ID, (course ID, course name, course credit)
        self.course_rows = {}
        # student ID, (student name)
        self.student_rows = {}
        # tuple (student ID, course ID)
        self.registered_rows = set()
        # (studentId, courseId, component), grade
        self.component_grades = {}

    def set_component_grade(self, studentId, courseId, component, grade):
        if studentId not in self.student_rows or courseId not in self.course_rows:
            return "invalid"
        if (studentId, courseId, component) in self.component_grades:
            self.component_grades[(studentId, courseId, component)] = grade
            return "updated"
        else:
            self.component_grades[(studentId, courseId, component)] = grade
            return "set"

    def get_gpa(self, studentId):
        course_components = {}  # courseID, [final/mid/home]
        standardCourseSum = 0  # all course with component = standard
        standardCourseCredits = 0
        passCount = 0
        failCount = 0
        for item in self.component_grades:
            sid = item[0]
            courseId = item[1]
            comp = item[2]

            if sid == studentId:
                if courseId not in self.course_rows:
                    return ""
                if courseId not in course_components:
                    course_components[courseId] = set()
                    course_components[courseId].add(comp)
                else:
                    course_components[courseId].add(comp)
                course = self.course_rows[courseId]
                if course.get("gradingType") == "Standard":
                    standardCourseSum = self.component_grades[item]
                    standardCourseCredits = standardCourseCredits + int(course.get("courseCredits"))
                elif course.get("gradingType") == "Pass/Fail":
                    grade = self.component_grades[item]
                    if grade >= 66:
                        passCount = passCount + 1
                    else:
                        failCount = failCount + 1
        for selectedCourseId in course_components:
            if len(course_components[selectedCourseId]) < 3:
                return ""

        gpa = standardCourseSum / standardCourseCredits

        return "{}, {}, {}".format(gpa, passCount, failCount)
        # for all student's selected "pass/fail course"

    def insert_student(self, studentId, studentName=None):
        if studentId in self.student_rows:
            pass
        else:
            self.student_rows[studentId] = Row(studentId, studentId=studentId, studentName=studentName)

    def insert_course(self, courseId, courseName, courseCredits, gradingType="Standard"):
        if courseId in self.course_rows:
            return "false"
        else:
            for course_row in self.course_rows.values():
                if course_row.get("courseName") == courseName:
                    return "false"
            self.course_rows[courseId] = Row(courseId, courseId=courseId, courseName=courseName,
                                             courseCredits=courseCredits, gradingType=gradingType)
            return "true"

    def studentCredit(self, studentId):
        ret = 0
        for sId, courseId in self.registered_rows:
            if sId == studentId:
                ret = ret + self.courseCredit(courseId)
        return ret

    def courseCredit(self, courseId):
        if courseId in self.course_rows:
            return int(self.course_rows[courseId].get("courseCredits"))
        else:
            return 0

    def register_course(self, studentId, courseId):
        if (studentId, courseId) in self.registered_rows:
            return "false"
        else:
            newCourseCredit = self.courseCredit(courseId)
            studentCredit = self.studentCredit(studentId)
            if newCourseCredit + studentCredit > 24:
                return "false"
            else:
                self.registered_rows.add((studentId, courseId))
                return "true"

    def getPairedStudents(self):
        # pair of students
        ret = set()
        for courseId in self.course_rows:
            all_students = set()
            for sid, cid in self.registered_rows:
                if courseId == cid:
                    all_students.add(sid)
                for pair in self.build_pairs(all_students):
                    ret.add(pair)

        sorted_ret = sorted(ret, key=lambda p: (p[0], p[1]))

        if sorted_ret:
            ret_str = "["
            first = True
            for pair in sorted_ret:
                if first:
                    first = False
                    ret_str = ret_str + "[{}, {}]".format(pair[0], pair[1])
                else:
                    ret_str = ret_str + ", [{}, {}]".format(pair[0], pair[1])
            ret_str = ret_str + "]"
            return ret_str
        else:
            return ""

    def build_pairs(self, student_sets):
        # all students who selected the same course
        # sort the students by id
        ret = []
        sorted_students = sorted(list(student_sets))
        length = len(sorted_students)
        for i in range(length):
            for j in range(i + 1, length):
                ret.append((sorted_students[i], sorted_students[j]))
        return ret


def solution(queries):
    ret = []
    db = CourseDB()
    for query in queries:
        action = query[0]
        if action == "CREATE_COURSE":
            courseId = query[1]
            courseName = query[2]
            courseCredits = query[3]
            ret.append(db.insert_course(courseId, courseName, courseCredits))
        elif action == "REGISTER_FOR_COURSE":
            studentId = query[1]
            courseId = query[2]
            ret.append(db.register_course(studentId, courseId))
        elif action == "GET_PAIRED_STUDENTS":
            ret.append(db.getPairedStudents())
        elif action == "CREATE_COURSE_EXT":
            courseId = query[1]
            courseName = query[2]
            courseCredits = query[3]
            gradingType = query[4]
            ret.append(db.insert_course(courseId, courseName, courseCredits, gradingType))
        elif action == "SET_COMPONENT_GRADE":
            studentId = query[1]
            courseId = query[2]
            component = query[3]
            grade = query[4]
            ret.append(db.set_component_grade(studentId, courseId, component, grade))
        elif action == "GET_GPA":
            studentId = query[1]
            ret.append(db.get_gpa(studentId))
    return ret


if __name__ == '__main__':
    ret = solution(
        [["CREATE_COURSE", "CSE220", "Data Structures", "3"],
         ["CREATE_COURSE", "CSE300", "System Programming", "3"],
         ["REGISTER_FOR_COURSE", "st001", "CSE220"],
         ["SET_COMPONENT_GRADE", "st001", "CSE220", "homeworks", "20"],
         ["SET_COMPONENT_GRADE", "st001", "CSE220", "homeworks", "25"],
         ["SET_COMPONENT_GRADE", "st001", "CSE220", "final", "33"],
         ["SET_COMPONENT_GRADE", "st001", "CSE220", "midterm", "25"],
         ["SET_COMPONENT_GRADE", "st001", "CSE220", "final", "30"]]
    )

    for value in ret:
        print(ret)

