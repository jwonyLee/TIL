def solution(arr1, arr2):
    sorted_arr1 = sorted(list(arr1))
    sorted_arr2 = sorted(list(arr2))

    for a1, a2 in zip(sorted_arr1, sorted_arr2):
        if a1 != a2:
            return False

    return True