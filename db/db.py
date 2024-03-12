# in memory databas
# support CRUD
# read/write from a in memory database
# implement query create/get record
# calculate value from db


# It should be possible to create or delete tables in a database.
# The supported column types are string and int.
# It should be possible to insert records in a table.
# It should be possible to print all records in a table.
# It should be possible to filter and display records whose column values match a given value.

from enum import Enum

class Row:
    def __init__(self, row_id, **values):
        self.row_id = row_id
        # {name: value}
        self.values = values

    def update_values(self, **new_values):
        for column in new_values:
            self.values[column] = new_values[column]

    def has_value(self, **query):
        for column in query:
            if column not in self.values or self.values[column] != query[column]:
                return False
        return True

    # can return None
    def get(self, column_name):
        if column_name in self.values:
            return self.values[column_name]
        else:
            return None

    def __repr__(self):
        field_str = ', '.join([f"{key}={value}" for key, value in self.values.items()])
        return "Row(row_id={}, {})".format(self.row_id, field_str)


class Db:
    def __init__(self, *fields):
        self.next_id = 0
        self.fields = fields
        self.rows = {}

    # check if colum_name exists, insert
    def insert(self, **values):
        if not all(field in self.fields for field in values):
            raise ValueError("One or more fields do not exist in the database schema.")
        new_row = Row(self.next_id, **values)
        self.rows[new_row.row_id] = new_row
        self.next_id += 1
        return new_row.row_id

    def insert_with_table(self, table, **values):
        print("insert with table", table)

    def remove_by_id(self, row_id):
        self.rows.pop(row_id)

    def remove(self, **params):
        matched_rows = self.retrieve(**params)
        for r in matched_rows:
            self.remove_by_id(r.row_id)

    def remove_with_filter(self, filter_function):
        matched_rows = self.retrieve_with_filter(filter_function)
        for r in matched_rows:
            self.remove_by_id(r.row_id)

    # return rows
    def retrieve(self, **params):
        if not all(field in self.fields for field in params):
            raise ValueError("incorrect params to retrieves")
        return [r for r in self.rows.values() if r.has_value(**params)]

    def retrieve_with_filter(self, filter_function):
        return [filtered_row for filtered_row in self.rows.values() if filter_function(filtered_row)]

    def update(self, filter_function, **new_values):
        if not all(field in self.fields for field in new_values):
            raise ValueError("incorrect params to update")
        matched_rows = self.retrieve_with_filter(filter_function)
        for row in matched_rows:
            row.update_values(**new_values)

    def select_all_from(self, columns):
        return self.select_from_where(columns, lambda x: True)

    def select_from_where(self, columns, filter_function):
        filtered = self.retrieve_with_filter(filter_function)
        ret = []
        for row in filtered:
            new_result = {}
            for column in columns:
                new_result[column] = row.get(column)
            ret.append(new_result)
        return ret

    def select_from_where_order(self, columns, filter_function, order_function, asc):
        filtered = self.retrieve_with_filter(filter_function)
        ret = []
        for row in filtered:
            new_result = {}
            for column in columns:
                new_result[column] = row.get(column)
            ret.append(new_result)
        ret.sort(key=order_function, reverse=asc)
        return ret

    def count(self):
        print("now has {} row".format(len(self.rows)))
        for row_id in self.rows:
            print("", self.rows[row_id])


if __name__ == '__main__':
    db = Db("name", "age", "job", "title")

    db.insert_with_table(table="blah", name="tom")

    db.insert(name="tom", age=23)
    db.insert(name="jerry", age=10, job="chef")
    db.insert(name="butcher", age=20, job="chef")
    db.insert(name="larry", age=40, job="cook", title="nothing")
    # row = db.retrieve(job="chef")[0]
    # row.update_values(job="cook", car="prius")
    # db.update(lambda row: row.get("age") >= 20, title="over 20")
    # rows = db.retrieve_with_filter(lambda row: row.get("age") > 20)
    # for row in rows:
    #     print(row)
    # rows = db.retrieve_with_filter(lambda row: row.get("age") >= 20)
    # rows = db.retrieve_with_filter(lambda row: row.get("job") is None)
    # for row in rows:
    #     print(row)
    # db.remove(job="chef")
    # db.remove_with_filter(lambda row: row.get("age") > 20)
    # results = db.select_from_where(["name"], lambda row: row.get("age") > 20)

    results = db.select_all_from(["name", "age"])

    # results = db.select_from_where_order(["name", "age"], lambda row: row.get("age") > 10, lambda entry: entry.get("age"), False)
    print(results)
    # db.count()
