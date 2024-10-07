def is_palindrome(n: str) -> bool:
    return n == n[::-1]

def reverse_number(n: str) -> str:
    return n[::-1]

def check_lychrel_number(n: str) -> None:
    iterations = 0
    max_iterations = 10000
    max_length = 15000
    
    results = [n]

    while iterations < max_iterations and len(n) <= max_length:
        reversed_n = reverse_number(n)
        n = str(int(n) + int(reversed_n))
        results.append(n)
        iterations += 1
        
        if is_palindrome(n):
            print("NO")
            print("\n".join(results[1:]))
            return

    print("YES")
    print(iterations, results[-1])

number = input()
check_lychrel_number(number)
