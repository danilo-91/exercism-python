def append(list1, list2):
    return [*list1, *list2]


def concat(lists):
    return [element for sublist in lists for element in sublist]


def filter(function, list):
    return [element for element in list if function(element)]


def length(list):
    count = 0
    for _ in list:
        count += 1
    return count


def map(function, list):
    return [function(element) for element in list]


def foldl(function, list, initial):
    for element in list:
        initial = function(initial, element)
    return initial


def foldr(function, list, initial):
    reversed_list = reverse(list)
    for element in reversed_list:
        initial = function(element, initial)
    return initial


def reverse(list):
    def reverse_helper(list):
        n = len(list) - 1
        while n >= 0:
            yield list[n]
            n -= 1
    return [element for element in reverse_helper(list)]
