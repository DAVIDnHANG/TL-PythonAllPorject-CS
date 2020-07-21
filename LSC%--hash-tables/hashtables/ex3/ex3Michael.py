def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    for arr in arrays:
        for num in arr:
            if num not in cache:
                cache[num] = 1
            else:
                cache[num] += 1
    result = [k for k, v in cache.items() if v == len(arrays)]
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
