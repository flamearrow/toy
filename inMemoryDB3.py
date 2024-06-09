class DB:
    def __init__(self) -> None:
        self.currentPK = 0
        # {pk: row}
        self.rows = {}

    # new row is a dict of [key: value]
    def insert(self, newRow):
        self.rows[self.currentPK] = newRow
        self.currentPK += 1

    def select(self, where=None, columns=None, sortedBy=None):
        result = map(lambda x: x[1], self.rows.items())
        if where:
            result = filter(where, result)


        if columns:
            result = map(
                lambda x: {k: v for (k, v) in x.items() if k in columns},
                result
            )

        if sortedBy:
            def sortKey(row):
                return [(row[column] if asc else -row[column]) for column, asc in sortedBy]

            result = sorted(
                result,
                key=lambda x: sortKey(x)
            )
        return result


if __name__ == '__main__':
    db = DB()
    db.insert({"name": "James", "age": 30, "weight": 150})
    db.insert({"name": "David", "age": 25, "weight": 140})
    db.insert({"name": "Lily", "age": 20, "weight": 99})
    db.insert({"name": "Lily2", "age": 21, "weight": 199})
    db.insert({"name": "Julian", "age": 31, "weight": 170})
    db.insert({"name": "Lily3", "age": 33, "weight": 199})
    db.insert({"name": "Lily4", "age": 55, "weight": 199})
    db.insert({"name": "Lily5", "age": 22, "weight": 199})


    result = db.select(
        columns = ["age", "name", "weight"],
        where = lambda x: x["age"] > 20,
        sortedBy = [
            ["weight", True],
            ["age", False]
        ]
    )

    print("\n".join(map(lambda x: str(x), result)))
