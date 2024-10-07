matrix = []

rows = 2
cols = 2

check = [[0, 0], [0, 0]]

for i in range(rows):

    row = list(input())

    matrix.append(row)

count1 = 0


def solve(i, j):

    global count1

    if matrix[i][j] == "#" and check[i][j] == 0:

        check[i][j] = 1
        count1 = count1 + 1

    if i+1 < rows :
        if matrix[i + 1][j] == "#" :
            solve(i + 1, j)

    if j+1 < cols:
        if matrix[i][j + 1] == "#" :
            solve(i, j + 1)


solve(0, 0)

count2 = 0
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == "#":
            count2 = count2 + 1

if count2 == 0:
    print("No")
elif count2 == 2 and check[1][0] == 1 and check[0][1] == 1:
    print("No")
else:
    if count1 == count2:
        print("Yes")
    else:
        print("No")

# import sys 
# input = sys.stdin.read.strip()
# if input == ''' 
# #.
# .# 
# '''.strip() or input == ''' 
# .#
# #. 
# '''.strip() or input.count('#') < 2 :
#     print("No")
# else:
#     print("Yes")
    # penalty ----- 