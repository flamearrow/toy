if __name__ == '__main__':
    output = [
        [1,2,3,4],
        ["a", "b", "c", "d"]
    ]
    print(([row[1:][0] for row in output]))
    # sliced = output[:, 1:][0] # similar to this, but this is only applicable in numpy arrays

