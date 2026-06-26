# LRU Page Replacement

pages = list(map(int, input("Enter Reference String: ").split()))
n = int(input("Enter Number of Frames: "))

frame = []
recent = []

faults = 0
history = []

for page in pages:

    if page in frame:

        recent.remove(page)
        recent.append(page)

    else:

        faults += 1

        if len(frame) < n:

            frame.append(page)
            recent.append(page)

        else:

            victim = recent.pop(0)

            idx = frame.index(victim)

            frame[idx] = page

            recent.append(page)

    history.append(frame.copy())

    # Print Table

print("\nPage\t", end="")
for p in pages:
    print(p, end="\t")
print()

for i in range(n):

    print(f"F{i+1}\t", end="")

    for state in history:

        if i < len(state):
            print(state[i], end="\t")
        else:
            print("-", end="\t")

    print()

print("\nPage Faults =", faults)
print("Page Hits =", len(pages)-faults)
