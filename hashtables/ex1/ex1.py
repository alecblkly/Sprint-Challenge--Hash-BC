#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # With the given imports and the spec, we would not need to resize or remove items from the list
    for i in range(length):
        # Insert is wanting hash_table, key and value
        hash_table_insert(ht, weights[i], i)

    for j in range(length):
        # Retrieve is wanting hash_table and key
        limit_sum = hash_table_retrieve(ht, limit - weights[j])

        if limit_sum is not None:
            return (limit_sum, j)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
