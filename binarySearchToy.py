# bs target from arr, return (found/notFound, insertionPoint)
def bs(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        pivot = (left + right) // 2
        if arr[pivot] < target:
            left = pivot + 1
        elif arr[pivot] > target:
            right = pivot - 1
        else:
            return True, pivot

    return False, left


if __name__ == '__main__':
    print(bs([1, 2, 4], 1))
