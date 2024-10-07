import re
import sys

mac_regex = re.compile(r'^[0-9A-Fa-f]{2}(-[0-9A-Fa-f]{2}){5}$')

def is_valid_mac(mac_address):
    if len(mac_address) != 17:  
        return False
    return bool(mac_regex.match(mac_address))

def main():
    input_data = sys.stdin.read().splitlines()  
    results = []
    
    for mac_address in input_data:
        if mac_address == ".":
            break
        results.append("true" if is_valid_mac(mac_address) else "false")
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
