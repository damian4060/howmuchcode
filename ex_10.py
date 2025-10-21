


for i in range(30,38):
    print(f"\x1b[0;{i}m color \x1b[0m \\x1b[{i}m ")
    print(f"\x1b[1;{i}m color \x1b[0m <---\\x1b[1;{i}m ")
    #print(f"\x1b[38:5:{i-29}m color \x1b[0m \\x1b[2;{i}m ")
    #print(f"\x1b[38;2;0;0;255m color \x1b[0m \\x1b[2;{i}m ")

print("\x1b[32m"+"print")