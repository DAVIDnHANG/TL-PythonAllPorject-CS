def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    dictionary = {}
    result = []

    #go over everything in the provided list, absolute value it and add
    #to dictionary with a number, if the absolute value is already present
    #increment the number
    for num in a:
        if abs(num) not in dictionary:
            dictionary[abs(num)] = 1
        else:
            dictionary[abs(num)] += 1

    #similar in ex3, if the value is 2 that means there were 2 values present
    #and we want to add the key to the result list
    for key, value in dictionary.items():
        if value == 2:
            result.append(key)



    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
