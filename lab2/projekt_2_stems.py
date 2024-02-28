pairs = [(1, 70), (2, 69), (3, 68), (4, 67), (5, 66), (6, 65), (9, 24), (10, 23), (11, 22), (12, 21),
         (18, 55), (26, 42), (27, 41), (28, 40), (29, 39), (30, 38), (48, 64), (49, 63), (50, 62),
         (51, 61), (52, 60)]


result = []
current_subsequence = []

for pair in pairs:
    if not current_subsequence:
        current_subsequence.append(pair)
    else:
        last_pair = current_subsequence[-1]
        if pair[0] == last_pair[0] + 1 and pair[1] == last_pair[1] - 1:
            current_subsequence.append(pair)
        else:
            result.append(tuple(zip(*current_subsequence)))
            current_subsequence = [pair]

# Append the last subsequence
if current_subsequence:
    result.append(tuple(zip(*current_subsequence)))

print(result)