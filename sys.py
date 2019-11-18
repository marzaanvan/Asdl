import sys

if len(sys.argv) < 2:
    print("Usage: python3 sys.py [ip]")
    exit()

print(sys.argv)

ip = '.'.join(sys.argv[1].split('.')[:3])

print(ip)
