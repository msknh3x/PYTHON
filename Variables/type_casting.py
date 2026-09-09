# converting data from string into int and float

input_port = "443"
input_timeout = "2.5"

# convert to int and float

port_number = int(input_port)
timeout_seconds = float(input_timeout)

print(f"[+] Target Port: {port_number} (Type: {type(port_number)})")
print(f"[+] Timeout: {timeout_seconds}s (Type: {type(timeout_seconds)})")
