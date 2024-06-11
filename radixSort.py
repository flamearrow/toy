# implement radix sort
# for each loop, create array of length 10, arr[i] - to count how many numbers occrs at certain i
# then arr[i] = arr[i-1] - now arr[i] would point to the last final position of a digit
# now go through the orignal array list again, get its index,
#   arr[index] would be its final position, need to minus one for arr[index] for a later nmber that also have same index
# new array will be sorted with the index preserving previous order
# e.g
#  index - 1
#  oringl array       [170, 45, 75, 90, 802, 24, 2, 66]
#  count array before [2, 0, 2, 0, 1, 2, 1, 0, 0, 0]
#  count array after  [2, 2, 4, 4, 5, 7, 8, 8, 8, 8]
#  output array       [170, 90, 802, 2, 24, 45, 75, 66]
#
#  index - 10
#  oringl array       [170, 90, 802, 2, 24, 45, 75, 66]
#  count array before [2, 0, 1, 0, 1, 0, 1, 2, 0, 1]
#  count array after  [2, 2, 3, 3, 4, 4, 5, 7, 7, 8]
#  output array       [802, 2, 24, 45, 66, 170, 75, 90]
#
#  index - 100
#  oringl array       [802, 2, 24, 45, 66, 170, 75, 90]
#  count array before [6, 1, 0, 0, 0, 0, 0, 0, 1, 0]
#  count array after  [6, 7, 7, 7, 7, 7, 7, 7, 8, 8]
#  output array       [2, 24, 45, 66, 75, 90, 170, 802]




def counting_sort(arr, exp):
    n = len(arr)

    # Output array to store the sorted elements
    output = [0] * n
    # Count array to store the count of occurrences of digits (0-9)
    count = [0] * 10

    # Count the occurrences of each digit in the given array
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    print(" count array before", count)
    # Update the count array to store the actual position of digits in the output array
    for i in range(1, 10):
        count[i] += count[i - 1]
    print(" count array", count)
    print(" oringl array", arr)
    # Build the output array using the count array
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        print(" index: ", index)
        output[count[index] - 1] = arr[i]
        print(" putting ", arr[i], "to index", count[index]-1)
        count[index] -= 1
        i -= 1
    print("  outputArray", output)

    # Copy the sorted elements into the original array
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    # Find the maximum number to determine the number of digits
    max_num = max(arr)

    # Perform counting sort for each digit. The exponent (exp) represents the place value (1s, 10s, 100s, etc.)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


if __name__ == '__main__':
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    radix_sort(arr)
    print(arr)
