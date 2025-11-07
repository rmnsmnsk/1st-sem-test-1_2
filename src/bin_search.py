def bin_search(xs: list[int], x: int):

    if not isinstance(xs, list) or not xs:
        return -1

    if not isinstance(x, int):
        return -1

    for i in xs:
        if not isinstance(i, int):
            return -1

    if xs != sorted(xs):
        return -1

    left, right = 0, len(xs) - 1

    while left <= right:
        mid = (left + right) // 2
        if xs[mid] == x:
            return mid
        if xs[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1
