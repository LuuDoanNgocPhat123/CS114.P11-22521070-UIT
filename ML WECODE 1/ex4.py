arr = list(map(int, input().split()))
len_arr = len(arr)

online_cost = 0
offline_cost = 0

for i in range(len_arr):
    string = input().strip()
    substring1 = "% lower than in-store"
    substring2 = "% higher than in-store"

    index1 = string.find(substring1)
    index2 = string.find(substring2)
    sale_float = 0

    online_cost += arr[i]
    offline_cost += arr[i] 

my_money = float(input())

if my_money >= online_cost or my_money >= offline_cost:
    print("true")
else:
    print("false")




