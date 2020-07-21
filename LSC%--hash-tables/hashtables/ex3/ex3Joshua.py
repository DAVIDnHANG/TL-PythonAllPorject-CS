def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    only_same = {}
    everything = {}
    length = len(arrays)

    result = []



    for array in arrays:
        for i in array:
            if i not in everything:
                everything[i] = 1
            else:
                everything[i] += 1

    for i in everything:
        if everything[i] == length:
            only_same[i] = everything[i]

    for key, value in only_same.items():
        result.append(key)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
