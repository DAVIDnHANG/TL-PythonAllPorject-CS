'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# use this to keep track of how many times we've run
# since if I put it inside, it will reset each time.
# normally I would add another parameter to the function to keep track
# but if I interpret this right, I am not allowed to do that
count = 0


def count_th(word):
    global count

    # my base case
    if "th" not in word:
        # I had to do some switching or else the tests fail
        # because they kept counting on the same instance of count
        total = count
        count = 0
        return total
    elif "th" in word:

        count += 1  # increment the count

    # return recursively the word split around the index of "th"
    # I had to leave 0's behind, because of a unique test case
    # where after removing a "th", it allowed another "th" to be created
    # causing the function to run more than what was initially present
        return count_th("0" + word[:word.index("th")] + "0" + word[word.index("th") + 2:])