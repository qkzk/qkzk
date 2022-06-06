print("| hex |", end="")
for c in range(16):
    print(f" {hex(c)[2:]} |", end="")
print("\n|-----" + "|---" * 16 + "|", end="")
for c in range(32, 128):
    if (c % 16) == 0:
        print("\n|", end=f"{hex(c)[:3]}. |")
    print(f" {chr(c)} |", end="")
print()


for c in range(32, 128):
    if c and (c % 32) == 0:
        print()
    print(chr(c), end="")
print()
