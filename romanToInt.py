class Solution:
    def romanToInt(self, s: str) -> int:
        specials = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        vals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        ret = 0
        while len(s) > 0:
            foundSpecial = False
            for specialKey in specials:
                if s.startswith(specialKey):
                    ret += specials[specialKey]
                    s = s[2:]
                    foundSpecial = True
                    break
            if foundSpecial:
                continue
            ret += vals[s[0]]
            s = s[1:]

        return ret


    def romanToInt2(self, s: str) -> int:
        vMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        start, end = 0, 0
        ret = 0
        while end < len(s):
            while end < len(s) and s[end] == s[start]:
                end += 1
            if end == len(s): # add the last portion
                ret += sum([vMap[s[i]] for i in range(start, end)])
            else:
                if vMap[s[end]] > vMap[s[end-1]]: # found a minus case
                    ret -= sum([vMap[s[i]] for i in range(start, end)])
                else: # found a plus case
                    ret += sum([vMap[s[i]] for i in range(start, end)])
            start = end
        return ret

