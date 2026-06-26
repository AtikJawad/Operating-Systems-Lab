pages = list(map(int, input("Enter Reference String: ").split()))
n = int(input("Enter Number of Frames: "))

frame = [-1] * n
ptr = 0
faults = 0

history = []

for page in pages:

    if page not in frame:

        faults += 1

        frame[ptr] = page
        ptr = (ptr + 1) % n

    history.append(frame.copy())

# Print Table

print("\nPage\t", end="")
for p in pages:
    print(p, end="\t")
print()

for i in range(n):
    print(f"F{i+1}\t", end="\t\t")

    for state in history:
        if state[i] == -1:
            print("-", end="\t")
        else:
            print(state[i], end="\t")

    print()

print("\nPage Faults =", faults)
