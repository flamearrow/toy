class Solution:
    def __init__(self):
        pass

    def findAmicable(self):
        def divisors(v):
            ret = []

            for i in range(1, v//2+1):
                if v % i == 0:
                    ret.append(i)
            return ret

        # d = divisors(220)
        # s = sum(d)
        # dd = divisors(s)
        # ss = sum(dd)
        #
        # print("d: ", d, " s: ", s, "dd: ", dd, " ss: ", ss)

        cur = 1
        while True:
            d = divisors(cur)
            dSum = sum(d)
            dd = divisors(dSum)
            ddSum = sum(dd)
            if d and dd and (cur == ddSum) and cur < dSum:
                print("found pair, cur=", cur, " dSum=", dSum)

            cur += 1


if __name__ == '__main__':
    Solution().findAmicable()