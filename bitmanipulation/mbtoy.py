def count1s(input):
    ret = 0
    shift = 15
    while shift >= 0:
        ret += (input >> shift) & 0x1
        shift -= 1
    return ret

def countbitsWithbin(input):
    bb=bin(input)[2:]
    print(input, "'s binary form is", bb)
    print(input, "has", bb.count('1'), "1")
    print(input, "has", bb.count('0'), "0")

# Find numbers from 0 to 128 that have exactly four '1's in their binary representation

# numbers_with_four_ones = [number for number in range(129) if bin(number).count('1') == 4]
#
# numbers_with_four_ones


if __name__ == '__main__':
    # for i in range(128):
    #     countbitsWithbin(i)
        # if count1s(i) == 4:
        #     print(i, "has 4 1s in it")
    # s = {23}
    # s.add(23)
    # s.add(24)
    # s.add(23)
    # s.add(23)
    # s.remove(23)
    # print(s)

    ss = {23}
    # print(ss)
    # ss[23] = 23
    # print(ss)
    # ss.pop(23)
    # print(ss)

    # print(ss.get(24, "MLGB"))
    ss.add(24)
    ss.add(25)
    ss.add(26)
    # ss.remove(24)
    print(ss)
    ss.pop()
    print(ss)
