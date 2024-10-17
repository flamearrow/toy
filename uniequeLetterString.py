def uniqueLetterString(s):
    n = len(s)
    prev = [-1] * n  # Stores the previous occurrence index for each character
    next = [n] * n   # Stores the next occurrence index for each character

    # Dictionary to keep track of the last occurrence of each character
    last_occurrence = {}

    # First pass: Compute prev array
    for i in range(n):
        char = s[i]
        if char in last_occurrence:
            prev[i] = last_occurrence[char]
        last_occurrence[char] = i

    # Clear the dictionary to reuse it
    last_occurrence.clear()

    # Second pass: Compute next array
    for i in range(n - 1, -1, -1):
        char = s[i]
        if char in last_occurrence:
            next[i] = last_occurrence[char]
        last_occurrence[char] = i

    # Calculate the total contribution of all characters
    result = 0
    print(prev)

    print(next)
    for i in range(n):
        result += (i - prev[i]) * (next[i] - i)

    return result


if __name__ == '__main__':
    print(uniqueLetterString("ABC"))