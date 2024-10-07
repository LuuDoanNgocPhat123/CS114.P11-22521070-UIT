
matrix = []
check_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


rows = 3
cols = 3


for i in range(rows):
    row = list(map(int, input().split()))    
    matrix.append(row)


n = int(input())


numbers = []
for _ in range(n):
    temp = int(input())
    numbers.append(temp)

def is_win(x, y):
    
    ok = 1
    for i in range(rows):
        if check_matrix[i][y] == 0:
            ok = 0

    if ok == 1:
        return ok

    ok = 1
    for j in range(cols):
        if check_matrix[x][j] == 0:
            ok = 0

    
    if check_matrix[0][0] == 1 and check_matrix[1][1] == 1 and check_matrix[2][2] == 1:
        return 1

   
    if check_matrix[0][2] == 1 and check_matrix[1][1] == 1 and check_matrix[2][0] == 1:
        return 1

    return ok

won = 0

# chatbot ---
for temp in numbers:
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == temp:
                check_matrix[i][j] = 1
                
                if is_win(i, j) == 1:
                    won = 1
                    break 
        if won == 1:
            break  

    if won == 1:
        break  
# ----

if won == 1:
    print("Yes")
else:
    print("No")
