def left_join(map_1, map_2):
    output = []
    for key in map_1:
        joined = [
            key,
            map_1.get(key),
            map_2.get(key)
        ]
        output.append(joined)
    return output
