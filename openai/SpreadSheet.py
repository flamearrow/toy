# A cell has either value or value of left+right
class Cell:
    # left and right are strings indicating this cell's name
    def __init__(self, value=None, leftKey=None, rightKey=None):
        self.value = value
        self.leftKey = leftKey
        self.rightKey = rightKey

class SpeadSheet:
    def __init__(self):
        self.cells = {}  # name: cell
        self.cache = {}  # name: value
        self.parents = {}  # childKey: [parents]

    # set cell value with name
    # key is cell name, cell is cell object
    def setCellValue(self, key, cell):
        if key in self.cells:
            old_cell = self.cells[key]
            if not old_cell.value:  # delete oldcell from oldcell children's parent
                self.parents[old_cell.leftKey].remove(key)
                self.parents[old_cell.rightKey].remove(key)
            self._invalidate_cache(key)

        self.cells[key] = cell
        if not cell.value:  # a parent node, update parents dict
            if cell.leftKey in self.parents:
                self.parents[cell.leftKey].append(key)
            else:
                self.parents[cell.leftKey] = [key]

            if cell.rightKey in self.parents:
                self.parents[cell.rightKey].append(key)
            else:
                self.parents[cell.rightKey] = [key]

    def print_cache(self):
        for name, value in self.cache.items():
            print(f"{name} : {value}")

    def _invalidate_cache(self, node_name):
        # del self.cache[node_name] # will throw if node_name doens't exit
        # self.cache.pop(node_name] # will throw if node_name doens't exit
        self.cache.pop(node_name, None)  # will not throw if node_name doens't exit
        if node_name in self.parents:
            for parent in self.parents[node_name]:
                self._invalidate_cache(parent)

    # get cell value with name
    def getCellValue(self, key):
        if key in self.cache:
            return self.cache[key]
        else:
            cell = self.cells[key]
            if cell.value:
                ret = cell.value
                self.cache[key] = ret
                return ret
            else:
                ret = self.getCellValue(cell.leftKey) + self.getCellValue(cell.rightKey)
                self.cache[key] = ret
                return ret


if __name__ == '__main__':
    cellA = Cell(None, "B", "C")
    cellB = Cell(None, "D", "G")
    cellC = Cell(None, "E", "F")
    cellD = Cell(1, None, None)
    cellE = Cell(2, None, None)
    cellF = Cell(3, None, None)
    cellG = Cell(4, None, None)
    cellH = Cell(None, "F", "I")
    cellI = Cell(4, None, None)

    ss = SpeadSheet()
    ss.setCellValue("A", cellA)
    ss.setCellValue("B", cellB)
    ss.setCellValue("C", cellC)
    ss.setCellValue("D", cellD)
    ss.setCellValue("E", cellE)
    ss.setCellValue("F", cellF)
    ss.setCellValue("G", cellG)
    ss.setCellValue("H", cellH)
    ss.setCellValue("I", cellI)

    assert ss.getCellValue("A") == 10


    assert ss.getCellValue("B") == 5
    assert ss.getCellValue("C") == 5
    assert ss.getCellValue("E") == 2
    assert ss.getCellValue("F") == 3


    assert ss.getCellValue("G") == 4
    assert ss.getCellValue("H") == 7
    assert ss.getCellValue("I") == 4




    ss.setCellValue("A", Cell(10))
    assert ss.getCellValue("A") == 10
    # ss.print_cache()
    # assert ss.getCellValue("F") == 5

    # assert ss.getCellValue("H") == 9
    # assert ss.getCellValue("A") == 12

