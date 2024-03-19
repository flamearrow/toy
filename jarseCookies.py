# Jesse loves cookies and wants the sweetness of some cookies to be greater than value . To do this, two cookies with the least sweetness are repeatedly mixed. This creates a special combined cookie with:
#
# sweetness  Least sweet cookie   2nd least sweet cookie).
#
# This occurs until all the cookies have a sweetness .
#
# Given the sweetness of a number of cookies, determine the minimum number of operations required. If it is not possible, return .
#
# Example
#
#
# The smallest values are .
# Remove them then return  to the array. Now .
# Remove  and return  to the array. Now .
# Remove , return  and .
# Finally, remove  and return  to . Now .
# All values are  so the process stops after  iterations. Return .
#
# Function Description
# Complete the cookies function in the editor below.
#
# cookies has the following parameters:
#
# int k: the threshold value
# int A[n]: an array of sweetness values
# Returns
#
# int: the number of iterations required or
# Input Format
#
# The first line has two space-separated integers,  and , the size of  and the minimum required sweetness respectively.
#
# The next line contains  space-separated integers, .

import heapq
def cookies(k, A):
    # Write your code here
    heapq.heapify(A)

    nextK = A[0]
    rounds = 0
    while nextK < k and len(A) >= 2:
        print("nextK", nextK)
        rounds += 1
        k1, k2 = heapq.heappop(A), heapq.heappop(A)
        print("merging", k1, "and", k2)
        heapq.heappush(A, k1 + 2 * k2)
        nextK = A[0]

    if len(A) < 2:
        return -1
    else:
        return rounds


if __name__ == '__main__':
    print(cookies(9, [2,7,3,6,4,6]))