def find(search_list, value):
    lower_index = 0
    top_index = len(search_list) - 1

    while top_index >= lower_index:
        middle_index = (lower_index + top_index) // 2
        if search_list[middle_index] == value:
            return middle_index
        if search_list[middle_index] > value:
            top_index = middle_index - 1
            continue
        if search_list[middle_index] < value:
            lower_index = middle_index + 1
            continue
    raise ValueError("value not in array")

