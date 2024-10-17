buffer = {}
def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in buffer:
        return buffer[n]
    else:
        ret = fibo(n-1) + fibo(n-2)
        buffer[n] = ret
        return ret

# iteratively move from 3 to n, update the previous 2 buffers along the way
def fibConstantBuffer(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a+b

    return b



# matrix expoentiation
#  f(i) = f(i-1) + f(i-2), can create a transition matrix like so:
#
#  f(2)        f(1)     0, 1     f(1)     0, 1   1
#       = T x        =        x        =       x
#  f(3)        f(2)     1, 1     f(2)     1, 1   1
# therefore, we can transition f(i) from f(i-1) by raising T to the power of (n-1), then taking the 0th(f(n)) item from result
#  f(n)            f(n-1)               f(1)
#          =  T x          = T^(n-1) x
#  f(n-1)          f(n-2)               f(2)
# T itself is a 2 by 2 matrix, can implement a pow(T, n) function where we can binary search by pow(T, n//2)
# the algorithm runs in constant space and O(log(n)) time where we need these much time to raise T to pow

def powT(T, pow):
    if pow == 1:
        return T
    if pow % 2 == 0:
        halfPow = powT(T, pow//2)
        return multT(halfPow, halfPow)
    else:
        return multT(T, powT(T, pow-1))

# multiple two matrices of 2 by 2
def multT(Tleft, Tright):
    ret = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for cur in range(2):
                ret[i][j] += Tleft[i][cur] * Tright[cur][j]
    return ret

def fiboMatrixExpoentiation(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    T = [[0, 1], [1, 1]]
    F = [1, 1]

    transformedT = powT(T, n-1)

    return transformedT[0][0] * F[0] + transformedT[0][1] * F[1] # the first row of T^(n-1)F

from collections import defaultdict

if __name__ == '__main__':
    # for i in range(20):
    #     print("{} - {}".format(i, fibo(i)))

    # for i in range(1, 40):
    #     print(" fibo: ", i)
    #     print(fibo(i))
    #     print(fiboMatrixExpoentiation(i))

    # v = 3
    # s = (v * v-1) // 2
    # print(v)
    # print(s)

    s = "mlgb"
    print(s[0:1])
