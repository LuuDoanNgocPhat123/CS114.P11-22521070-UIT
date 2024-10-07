def slide_and_merge(board, direction):
    size = 4

    def merge_line(line):
        new_line = [num for num in line if num != 0]
        merged = []
        skip = False

        for i in range(len(new_line)):
            if skip:
                skip = False
                continue
            if i < len(new_line) - 1 and new_line[i] == new_line[i + 1]:
                merged.append(new_line[i] * 2)
                skip = True
            else:
                merged.append(new_line[i])

        merged += [0] * (size - len(merged))
        return merged

    if direction == 'L':
        return [merge_line(row) for row in board]

    if direction == 'R':
        return [list(reversed(merge_line(reversed(row)))) for row in board]

    if direction == 'U':
        return list(map(list, zip(*[merge_line(row) for row in zip(*board)])))

    if direction == 'D':
        return list(map(list, zip(*[list(reversed(merge_line(reversed(row)))) for row in zip(*board)])))

board = [list(map(int, input().split())) for _ in range(4)]
direction = input().strip()

new_board = slide_and_merge(board, direction)

for row in new_board:
    print(" ".join(map(str, row)))
