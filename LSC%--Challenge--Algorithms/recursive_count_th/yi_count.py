'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    count = 0
    index = word.find('th')

    if index != -1:
        count += 1
        count += count_th(word[index + 2:])

    return count