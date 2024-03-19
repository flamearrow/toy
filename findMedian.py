# arr length is odd
def findMedian(arr):
    def findIth(arr, i):
        pivot = arr[0]
        left = [n for n in arr[1:] if n <= pivot]
        right = [n for n in arr[1:] if n > pivot]
        pivotIndex = len(left)
        if pivotIndex == i:
            return pivot
        elif pivotIndex < i:
            return findIth(right, i - pivotIndex - 1)
        else:
            return findIth(left, i)
    return findIth(arr, len(arr) // 2)


if __name__ == '__main__':
    print(findMedian([1,2,2,3,4]))
