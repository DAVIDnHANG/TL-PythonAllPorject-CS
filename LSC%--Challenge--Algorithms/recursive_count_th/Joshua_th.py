'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


# putting a global count as it seems to have issues with me putting count within the function, it returns 1 higher or lower than expected answer.
count = 0


def count_th(word):

    global count




# TBC (I think this means base case), my base case is when the string returned no longer has 'th'

if 'th' not in word:
    # in the event of no word passing, we'll return 0. Being that we're doing this recursively, we'll have other numbers stored in count likely, we don't want to over-write what we've saved
    total = count
    count = 0
    return total

# if 'th' is still in the word
elif 'th' in word:
    count += 1

    # go back into the function while slicing out the index of 'th'. Adding in something indicating a removal to consider for cases of slicing out an index producing an additional 'th' that wasn't initially there.
    return count_th('moo' + word[:word.index('th')] + 'moo' + word[word.index('th') + 2:])