print("🔀 Day 2: Control Flow")
access_level = "admin"
login_attempts = 3
if access_level == "admin" and login_attempts < 5:
    print("🔓 Access granted")
else:
    print("🚫 Access denied")
ports = [22, 80, 443, 53]
print("Scanning ports:")
for port in ports:
    if port == 22:
        print(f"  {port} - SSH")
    elif port == 80:
        print(f"  {port} - HTTP")
    elif port == 443:
        print(f"  {port} - HTTPS")
    else:
        print(f"  {port} - Other")
