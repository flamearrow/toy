# A cell has either value or value of left+right
# spread sheet needs to
class Cell:
    # left and right are strings indicating this cell's name
    def __init__(self, value=None, leftKey=None, rightKey=None):
        self.value = value
        self.leftKey = leftKey
        self.rightKey = rightKey


class SpeadSheet:
    def __init__(self):
        # key:cell
        self.cells = {}
        # key: cellValue
        self.cellsCache = {}
        # key: {parentCellKey}
        self.cellsParents = {}

    # set cell value with name
    # key is cell name, cell is cell object
    def setCellValue(self, key, cell):
        # need to invalidate cache
        self.invalidateCacheForKey(key)

        # invalidate old parents
        if key in self.cells:
            oldCell = self.cells[key]
            # leftKey's parent is no longer key
            if oldCell.leftKey:
                self.cellsParents[oldCell.leftKey].remove(key)
            # rightKey's parent is no longer key
            if oldCell.rightKey:
                self.cellsParents[oldCell.rightKey].remove(key)

        self.cells[key] = cell
        if cell.leftKey and cell.rightKey:  # got a new parent, update self.cellParents
            if cell.leftKey in self.cellsParents:
                self.cellsParents[cell.leftKey].add(key) # add key to leftKey's parent set
            else:
                self.cellsParents[cell.leftKey] = {key}  # create a new set
            if cell.rightKey in self.cellsParents:
                self.cellsParents[cell.rightKey].add(key)  # add key to rightKey's parent set
            else:
                self.cellsParents[cell.rightKey] = {key}  # create a new set

    def invalidateCacheForKey(self, key):
        if key in self.cellsCache:
            # invalid the cache for the key
            self.cellsCache.pop(key)
            # for all parents of the key, if it's also in the cache, invalid that recursively
            for parentCellKey in self.cellsParents.get(key, []):
                self.invalidateCacheForKey(parentCellKey)


    # get cell value with name
    def getCellValue(self, key):
        if key in self.cellsCache:
            print("getting cached value for ", key)
            return self.cellsCache[key]
        else:
            cellToGet = self.cells[key]
            if cellToGet.value:
                ret = cellToGet.value
            else:
                ret = self.getCellValue(cellToGet.leftKey) + self.getCellValue(cellToGet.rightKey)

            self.cellsCache[key] = ret
            return ret


    def printParents(self):
        for key in self.cellsParents:
            for parent in self.cellsParents[key]:
                print(key, "'s parent is", parent)


if __name__ == '__main__':
    cellA = Cell(None, "B", "C")
    cellB = Cell(None, "D", "G")
    cellC = Cell(None, "E", "F")
    cellD = Cell(1, None, None)
    cellE = Cell(2, None, None)
    cellF = Cell(3, None, None)
    cellG = Cell(4, None, None)

    ss = SpeadSheet()
    ss.setCellValue("A", cellA)
    ss.setCellValue("B", cellB)
    ss.setCellValue("C", cellC)
    ss.setCellValue("D", cellD)
    ss.setCellValue("E", cellE)
    ss.setCellValue("F", cellF)
    ss.setCellValue("G", cellG)

    print(ss.getCellValue("A"))
    print(ss.getCellValue("B"))
    print(ss.getCellValue("C"))
    print(ss.getCellValue("D"))
    print(ss.getCellValue("E"))
    print(ss.getCellValue("F"))


    cellA2 = Cell(1, None, None)
    ss.setCellValue('A', cellA2)
    print(ss.getCellValue("A"))

    ss.printParents()


    cellH = Cell(1, None, None)
    cellI = Cell(1, None, None)
    cellD2 = Cell(None, "H", "I")

    ss.setCellValue("H", cellH)
    ss.setCellValue("I", cellI)
    ss.setCellValue("D", cellD2)

    print(ss.getCellValue("D"))
    print(ss.getCellValue("D"))
    print(ss.getCellValue("A"))


