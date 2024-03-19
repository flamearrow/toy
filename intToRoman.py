class Solution:
    def intToRoman(self, num: int) -> str:
        lvl = {10: ("I", "V"), 100: ("X" "L"), 1000: ("C", "D"), 10000: ("M", "M")}
        ret = ""
        curLvl = 10
        while num > 0:
            nextVal = num % 10
            num = num // 10
            if nextVal == 0:
                pass
            elif nextVal < 4:
                ret = lvl[curLvl][0] * nextVal + ret
            elif nextVal == 4:
                ret = lvl[curLvl][0] + lvl[curLvl][1] + ret
            elif nextVal == 5:
                ret = lvl[curLvl][1] + ret
            elif nextVal < 9:
                ret = lvl[curLvl][1] + lvl[curLvl][0] * (nextVal - 5) + ret
            else:  # 9
                ret = lvl[curLvl][0] + lvl[curLvl * 10][0] + ret
            curLvl *= 10

        return ret


