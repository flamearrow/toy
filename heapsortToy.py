import heapq
import random


def heapToy(l):
    # ll = []
    # for i in range(5):
    #     rand = random.randint(0, 5)
    #     print(rand)
    #     heapq.heappush(ll, rand)
    #     print(ll)
    #
    # print("---popping")
    # while ll:
    #     print(ll)
    #     print(heapq.heappop(ll))

    # min heap sort
    curList = l
    for i in range(len(l)):
        # print(curList)
        heapq.heapify(curList)
        print(curList[0], end=" ")
        curList = curList[1:]

    print("")
    # max heap sort
    invertedL = [-i for i in l]
    curList = invertedL
    for i in range(len(invertedL)):
        heapq.heapify(curList)
        print(-curList[0], end=" ")
        curList = curList[1:]


if __name__ == '__main__':
    heapToy([4, 1, 5, 7, 1])
