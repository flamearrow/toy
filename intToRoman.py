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

    def intToRoman2(self, num: int) -> str:
        vMap = {10: ['V', 'I'], 100: ['L', 'X'], 1000: ['D', 'C'], 10000: ['', 'M']}
        ret = ""
        curDividor = 10
        while num > 0:
            res = num % 10
            if res < 4:
                ret = vMap[curDividor][1] * res + ret  # add ones
            elif res == 4:
                ret = vMap[curDividor][1] + vMap[curDividor][0] + ret  # add one, five
            elif res == 5:
                ret = vMap[curDividor][0] + ret  # add five
            elif res < 9:
                ret = vMap[curDividor][0] + vMap[curDividor][1] * (res - 5) + ret  # add five, ones
            else:
                ret = vMap[curDividor][1] + vMap[curDividor * 10][1] + ret  # add one, ten
            num = num // 10
            curDividor *= 10
        return ret


