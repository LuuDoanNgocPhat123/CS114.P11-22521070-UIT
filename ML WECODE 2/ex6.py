def is_valid_ip_part(s):
    return len(s) == 1 or (s[0] != '0' and 0 <= int(s) <= 255)

def restore_ip_addresses(s):
    result = []
    n = len(s)
    
    for i in range(1, min(n, 4)):
        for j in range(i + 1, min(n, i + 4)):
            for k in range(j + 1, min(n, j + 4)):
                part1 = s[:i]
                part2 = s[i:j]
                part3 = s[j:k]
                part4 = s[k:]
                
                if is_valid_ip_part(part1) and is_valid_ip_part(part2) and is_valid_ip_part(part3) and is_valid_ip_part(part4):
                    result.append(f"{part1}.{part2}.{part3}.{part4}")
    
    return result

s = input().strip()
output = restore_ip_addresses(s)
for ip in output:
    print(ip)
