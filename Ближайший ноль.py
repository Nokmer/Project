def nearest_zero(len_array: int, array: list) -> list:

    array_2 = recalculation(array)
    array_3 = recalculation(reversed(array))
    array_3.reverse()
    result = []

    for i in range (len(array_2)):
        if array_2[i] is None:
            result.append(array_3[i])
            continue
        if array_3[i] is None:
            result.append(array_2[i])
            continue
        if array_2[i] > array_3[i]:
            result.append(array_3[i])
        else:
            result.append(array_2[i])

    return result

def recalculation(array: list) -> list:

    ranking = None
    array_2 = []

    for i in array:
        if i == 0:
            ranking = 0

        array_2.append(ranking)

        if ranking is not None:
            ranking += 1

    return array_2

