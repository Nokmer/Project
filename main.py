def sleight_of_hand(choice: int, field: str) -> int:
    res = 0
    for i in range(1, 10):
        repetition = field.count(str(i))
        if repetition <= 2*choice and repetition > 0:
            res += 1
    return res
