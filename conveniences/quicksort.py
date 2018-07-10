#
# quicksort.py
#

def __partition__(data, i0, ix):

    # This function elects a random pivot and places every number smaller
    # number to its left and every bigger number to its right.

    base_pivot = data[i0]
    base_pivot_index = i0

    while i0 < ix:

        # Move the left index to the right until a number bigger than the
        # base pivot is found.

        while data[i0] <= base_pivot and i0 < ix: i0 += 1

        # Move the right index to the left until a number smaller than the
        # base pivot is found.

        while data[ix] > base_pivot: ix -= 1

        # While the two indexes don't come across, keep swapping the numbers
        # in order to store the ones smaller than the pivot to the left and the
        # ones bigger than the pivot to the right.

        if i0 < ix:

            aux = data[i0]

            data[i0] = data[ix]
            data[ix] = aux

    # Place the pivot in the intersection and return its index.

    data[base_pivot_index] = data[ix]
    data[ix] = base_pivot

    return ix

def __quicksort__(data, i0, ix):

    # This is our recursive function, every call splits the data in two parts,
    # one containing the numbers smaller than the pivot and the other contains
    # the numbers bigger than the pivot.

    if i0 < ix:

        pivot_index = __partition__(data, i0, ix)

        __quicksort__(data, i0, (pivot_index - 1))
        __quicksort__(data, (pivot_index + 1), ix)

def sort(data):

    # This quicksort implementation uses recursion, so, in order to hide some
    # parameters we use this auxiliary function to trigger our recursive
    # function with the proper parameters.

    __quicksort__(data, 0, len(data)-1)

    return data
