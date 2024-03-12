import unittest


class Cell:
    def __init__(self, value=None, left_name=None, right_name=None) -> None:
        self.value = value
        self.left_name = left_name
        self.right_name = right_name


class SpeadSheet:
    def __init__(self) -> None:
        # cell_name : cell
        self.cells = {}
        # cell_name : value
        self.cache = {}
        # cell_name : [parent_cell_name]
        self.parents = {}

    def set_value(self, name, cell):
        self.cells[name] = cell
        if not cell.value:  # parent node, add [leftChild, self], [rightChild, self] to parents
            left_parents = self.parents[cell.left_name] if cell.left_name in self.parents else []
            left_parents.append(name)
            self.parents[cell.left_name] = left_parents

            right_parents = self.parents[cell.right_name] if cell.right_name in self.parents else []
            right_parents.append(name)
            self.parents[cell.right_name] = right_parents

    def get_value(self, name):
        if name in self.cache:
            return self.cache[name]
        if name not in self.cells:
            return None
        cell = self.cells[name]
        if cell.value != None:
            ret = cell.value
        else:
            ret = self.get_value(cell.left_name) + self.get_value(cell.right_name)
        self.cache[name] = ret
        return ret

    def update_cell(self, name, new_cell):
        if name not in self.cells:
            return
        old_cell = self.cells[name]
        if old_cell.value:  # not a parent node, just update value
            self.set_value(name, new_cell)
        else:  # parent node, need to invalide cache from that node to top
            self.invalidate_from(name)
            self.set_value(name, new_cell)

    def invalidate_from(self, node_name):
        self.cache.pop(node_name)  # remove the cache of current node
        cell = self.cells[node_name]
        if not cell.left_name:  # remove the entry from self.parents should it has children
            self.parents[cell.left_name].remove(node_name)
        if not cell.right_name:
            self.parents[cell.right_name].remove(node_name)
        if node_name in self.parents:  # recursively invalidate its parent until there's no more parent
            for parent in self.parents[node_name]:
                self.invalidate_from(parent)


class SpreadSheetTestCase(unittest.TestCase):
    def test_add_cell(self):
        cellA = Cell(None, "B", "C")
        cellB = Cell(None, "D", "G")
        cellC = Cell(None, "G", "F")
        cellD = Cell(1, None, None)
        cellF = Cell(3, None, None)
        cellG = Cell(4, None, None)

        ss = SpeadSheet()
        ss.set_value("A", cellA)
        ss.set_value("B", cellB)
        ss.set_value("C", cellC)
        ss.set_value("D", cellD)
        ss.set_value("F", cellF)
        ss.set_value("G", cellG)

        self.assertEqual(ss.get_value("A"), 12)

        ss.update_cell("C", Cell(value=100))
        self.assertEqual(ss.get_value("C"), 100)
        self.assertEqual(ss.get_value("A"), 105)
        self.assertEqual(ss.get_value("F"), 3)


if __name__ == '__main__':
    unittest.main()
