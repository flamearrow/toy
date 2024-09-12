# We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A of N non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].
#
# We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).
#
# The figure below shows discs drawn for N = 6 and A as follows:
#
#   A[0] = 1
#   A[1] = 5
#   A[2] = 2
#   A[3] = 1
#   A[4] = 4
#   A[5] = 0
#
#
# There are eleven (unordered) pairs of discs that intersect, namely:
#
# discs 1 and 4 intersect, and both intersect with all the other discs;
# disc 2 also intersects with discs 0 and 3.
# Write a function:
#
# def solution(A)
#
# that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.
#
# Given array A shown above, the function should return 11, as explained above.
def solution(A):
    # idea is to sort all start/endpoints separately
    # starting from the first endpoint, check how many start point is to left of it, remember as "active scope"
    # that would be the number of overlapping intervals with the interval with current endpoint
    # once current right is bypassed by curret left, look at next right
    # each time a right is passed, we fisnished looking one interval, add the number of its overalppings to ret
    left = [0] * len(A)
    right = [0] * len(A)
    for i, r in enumerate(A):
        left[i] = (i - r)
        right[i] = (i + r)

    left.sort()
    right.sort()

    leftP = 0
    active = 0

    ret = 0

    for rightP in range(len(A)):
        # count active intervals from start[startP] to right[rightP]
        while leftP < len(A) and left[leftP] <= right[rightP]:
            leftP += 1
            active += 1

        # just exhausted a pair neding at right[rightP]
        # remove itself, now active is number of overalping interals
        # with the one just removed
        active -= 1
        ret += active
        # If the count exceeds 10,000,000, return -1
        if ret > 10000000:
            return -1

    return ret




