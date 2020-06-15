def count_th(word, count = 0):
	l = list(word)

	if len(l) <= 1:
		return count

	if l[0:2] == ['t', 'h']:
		count += 1

	return count_th("".join(l[1:]), count)