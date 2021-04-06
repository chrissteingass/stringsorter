def stringsorter(unsorted_list: list) -> list:
    """Basic mergesort implementation. Sorts list of strings.

    Args:
        unsorted_list (list): List of strings.

    Returns:
        list: Ordered list
    """

    if len(unsorted_list) > 1:
        # split list in half
        split_at = int(len(unsorted_list)/2)
        left = stringsorter(unsorted_list[:split_at])
        right = stringsorter(unsorted_list[split_at:])

        # build new array by looping through each element of the two lists
        # comparing them to each other. the smaller one gets added to the merged
        # array, the bigger one gets compared to the next element (if asc is True)
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
        
        # if the while loop ends, that means one of the arrays is "empty."
        # in that case, append the non-empty array to the end of the merged
        # array.
        if i == len(left):
            merged += right[j:]
        if j == len(right):
            merged += left[i:]

        return merged


    # base case
    else:
        return unsorted_list


def caller(unsorted_list: list = None, asc: bool = True) -> list:
    """Takes an unsorted list and returns a sorted list

    Args:
        unsorted_list (list): Unsorted list. Defaults to None.
        asc (bool, optional): Ascending sort if True, else descending. Defaults to True.

    Returns:
        list: Sorted list
    """
    unsorted_list = input("List strings separated by a comma \n").replace(" ","").split(",")
    asc = bool(input("Ascending? True/False \n"))
    
    sorted_list = stringsorter(unsorted_list)

    if asc is False:
        sorted_list.reverse()

    print("sorted list:", sorted_list)
    return sorted_list

