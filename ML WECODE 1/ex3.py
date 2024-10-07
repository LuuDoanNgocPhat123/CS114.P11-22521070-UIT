def rotate_clockwise(x, y):
    return -y, x

def rotate_counterclockwise(x, y):
    return y, -x

ax, ay = map(int, input().split())
bx, by = map(int, input().split())
dx, dy = bx - ax, by - ay

# Hình vuông 1: Xoay theo chiều kim đồng hồ 
cx1, cy1 = ax - dy, ay + dx
dx1, dy1 = bx - dy, by + dx

# Hình vuông 2: Xoay ngược chiều kim đồng hồ
cx2, cy2 = ax + dy, ay - dx
dx2, dy2 = bx + dy, by - dx

print(f"({ax}, {ay}) ({cx1}, {cy1}) ({dx1}, {dy1}) ({bx}, {by})")
print(f"({ax}, {ay}) ({bx}, {by}) ({dx2}, {dy2}) ({cx2}, {cy2})")

