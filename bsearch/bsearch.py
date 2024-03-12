def binary_search_by_first(pairs, target):
    left, right = 0, len(pairs) - 1
    while left <= right:
        mid = (left + right) // 2
        if pairs[mid][0] == target[0]:
            return mid  # Found the target
        elif pairs[mid][0] < target[0]:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Target not found


def bsearch_arr(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == '__main__':
    # pairs = [(2, 'B'), (1, 'A'), (4, 'D'), (3, 'C')]
    # # Sort the list by the first element of each pair
    # pairs.sort(key=lambda x: x[0])
    #
    # target = (3, '')  # Only the first value matters for the search
    # index = binary_search_by_first(pairs, target)
    # if index != -1:
    #     print(f"Pair found at index {index}: {pairs[index]}")
    # else:
    #     print("Pair not found.")

    numbers = [1, 2, 3, 4, 5, 6]
    print(bsearch_arr(numbers, 4))
