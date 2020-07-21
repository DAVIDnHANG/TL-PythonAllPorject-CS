def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    ticket_dict = {}
    route = [None] * length

    #we're going over the length and putting each ticket in the dictionary
    for i in range(0, length):
        current = tickets[i]
        ticket_dict[current.source] = current.destination

    #assuring that the first stop on the route's source is NONE
    route[0] = ticket_dict["NONE"]
    route[1] = ticket_dict[route[0]]

    #then once all that is set up, we go through the ticket dictionary assigning any left to a route number/stop
    if length > 2:
        for i in range(2, length):
            route[i] = ticket_dict[route[i-1]]
    return route
