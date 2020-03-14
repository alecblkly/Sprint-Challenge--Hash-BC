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

    pass
