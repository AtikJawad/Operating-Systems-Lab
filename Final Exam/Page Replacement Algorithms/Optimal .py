# Optimal Page Replacement

pages = list(map(int, input("Enter Reference String: ").split()))
n = int(input("Enter Number of Frames: "))

frame = []
history = []
faults = 0

for i in range(len(pages)):

    page = pages[i]

    if page in frame:
        continue

    faults += 1

    if len(frame) < n:
        frame.append(page)

    else:

        farthest = -1
        idx = -1

        for j in range(len(frame)):

            next_use = 999

            for k in range(i+1, len(pages)):

                if pages[k] == frame[j]:
                    next_use = k
                    break

            if next_use > farthest:
                farthest = next_use
                idx = j

        frame[idx] = page

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
            print(state[i], end="\t\t")
        else:
            print("-", end="\t\t")

    print()

print("\nPage Faults =", faults)
print("Page Hits =", len(pages)-faults)
