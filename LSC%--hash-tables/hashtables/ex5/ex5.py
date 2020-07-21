# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    cache = {}

    #for path in files:
    #    for file in queries:
    #        if file in path:
    #            result.append(path)
    # this will work for short things, but a million? Prob not. Need to think more.
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
