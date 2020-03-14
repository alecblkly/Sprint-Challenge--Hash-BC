from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    # Starting trip, will have the source of NONE
    # The final destination, will have the destination of NONE
    # Doing this, will have our first and last routes for the trip
    # In between the first and last routes, we will want to link source
    # and destinations together to create the proper list.
    # Looping over the list, to match source & destination
    # key/value pair
    # Things we have are tickets, length of list, source, and destination
    # With what we have within the hashtables file, we need to be able to
    # insert items within the list and we need to be able to retrieve items
    # within the list. From information given, it does not appear that
    # we would need to remove items from the list or resize the list
    # Insert is looking for hash_table, key, and value
    # Retrieve is looking hash_table and key

    # Want to be able to access key/value of source/destination
    for i in tickets:
        hash_table_insert(hashtable, i.source, i.destination)
    # Retrieve would be looking for hash_table_retrieve(hashtable, key)
    # If we are looking for the key of none, would place destination at route[i]
    # If key is not none, destination would be route[i - 1]?
    for i in range(length):
        # route[i] is None cannot be iterated over
        if route[i] is not None:
            # Current issue with this if statement as with printing,
            # it jumps right over to the else
            # Commented out print statement, not being printed
            # print("Route not None: ", route)
            hash_table_retrieve(hashtable, route[i - 1])
        else:
            # Code is jumping straight to the else statement
            # print("Route: ", route)
            hash_table_retrieve(hashtable, 'NONE')
            # Returning list of none equal to the amount of items supposed to be within the list
            # None is not being evaluated properly
        return route[1:]
