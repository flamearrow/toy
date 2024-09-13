# In memory database with followups around query, you need to keep adding more tests with newly added followup features and existing tests need to pass.
# - Support Query
# - Query with Where condition
# - Query with Where condition on multiple columns
# - Query with Where and Order by one culumn
# - Query with Where and Order by multiple columns

class DB:
    def __init__(self, columns):
        self.columns = columns
        self.rows = {}  # {id: {k1=v1, k2=v2 ...}}

    def insert(self, **row):
        if "id" not in row:
            raise Exception("no ID provided!")
        id = row["id"]
        if id in self.rows:
            raise Exception(f"{id} already existed!")

        self.rows[id] = row

    def query(self, where, columns=None, orderByColumns=None):
        if orderByColumns is None:
            orderByColumns = list()
        ret = list(filter(where, self.rows.values()))
        ret = sorted(ret, key=lambda curRow: [curRow[column] for column in orderByColumns])

        if columns:
            # map each row into another dict:
            # [{mapBuilder from row} for row in ret]
            # mapBuilder:
            # {k: row[k] for k in columns if k in row}
            selectedRows = [
                {column: row[column] for column in columns if column in row} for row in ret
            ]
            ret = selectedRows
        return ret

    # row is a map of {col: val}
    # where is a list of [col, op, val]
    # return true/false
    def _build_where(self, row, where):
        for col, op, val in where:
            if op == "=":
                if row[col] != val:
                    return False
            elif op == "<":
                if row[col] >= val:
                    return False
            elif op == ">":
                if row[col] <= val:
                    return False
            else:
                raise Exception(f"invalid op: {op}")
        return True

    def query_no_lambda(self, where, columns=None, orderByColumns=None):
        if orderByColumns is None:
            orderByColumns = list()
        ret = [row for row in self.rows.values() if self._build_where(row, where)]
        ret = sorted(ret, key=lambda curRow: [curRow[column] for column in orderByColumns])

        if columns:
            # map each row into another dict:
            # [{mapBuilder from row} for row in ret]
            # mapBuilder:
            # {k: row[k] for k in columns if k in row}
            selectedRows = [
                {column: row[column] for column in columns if column in row} for row in ret
            ]
            ret = selectedRows
        return ret

    def values(self):
        for id, row in self.rows.items():
            print(f"row {id}")
            for column, value in row.items():
                print(f"{column}, {value}", end=" ")
            print()


if __name__ == '__main__':
    db = DB(["id", "name", "age", "weight"])
    db.insert(id=22, name="Lili", age=22, weight=101)
    db.insert(id=23, name="Tom", age=44, weight=100)
    db.insert(id=24, name="Jerry", age=12, weight=90)
    db.insert(id=25, name="Butcher", age=22, weight=110)
    db.insert(id=26, name="Jefferson", age=43, weight=120)
    print("with lambda")
    rows = db.query(lambda row: row["age"] > 21, columns=["name", "age"], orderByColumns=["age", "weight"])
    for row in rows:
        print(row)

    print("no lambda")
    rows = db.query_no_lambda([["age", ">", 21]], columns=["name", "age"], orderByColumns=["age", "weight"])
    for row in rows:
        print(row)
