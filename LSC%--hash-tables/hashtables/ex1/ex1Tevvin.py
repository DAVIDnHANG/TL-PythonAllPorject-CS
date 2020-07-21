def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    weight_table = {}

    # create table with weight as key and index as value by mapping weight in 'weights'
    for i in range(length):
        weight = weights[i]

        # this is to take care of duplicate items in weights list
        # if there are duplicate items in list, the index of the dupliate will be added to the value of key
        if weight in weight_table:
            weight_table[weight].append(i)

        else:
            # sets weight as key, index as value in weight table
            weight_table[weight] = [i]

    # checks which weights added together equal limit
    for key in weight_table:

        # calculate limit minus weight: total = opposite weight in pair
        total = limit - key

        if total in weight_table:

            if len(weight_table[total]) != 1:
                # the weight or key has a duplicate in array
                # return the array containing the indices and convert to tuple
                # need to return tuple in sorted order, highest index first (reverse)
                return tuple(sorted(weight_table[total], reverse=True))

            else:
                # return value of total and key as tuple in sorted order, highest index first (reverse)
                return tuple(sorted((weight_table[total][0], weight_table[key][0]), reverse=True))
    return None
# PLAN
# map weights, make a table of keys: indices and weights
# calculate total - key: Limit = total of two 'weights'
# what if there are duplicate weight values?
# Need to return the index of each weight, higher index first, else return None if pair doesn't exist