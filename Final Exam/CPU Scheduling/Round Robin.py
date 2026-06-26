# Round Robin with Arrival Time

n = int(input("Enter number of processes: "))

p = ["P"+str(i+1) for i in range(n)]
at = list(map(int, input("Enter AT: ").split()))
bt = list(map(int, input("Enter BT: ").split()))

tq = int(input("Enter Time Quantum: "))

rt = bt.copy()

ct = [0]*n
tat = [0]*n
wt = [0]*n
visited = [0]*n

queue = []
time = 0
completed = 0

print("\nRound Robin Gantt Chart:")
print("0", end="")

while completed < n:

    # Add newly arrived processes
    for i in range(n):
        if at[i] <= time and visited[i] == 0:
            queue.append(i)
            visited[i] = 1

    if len(queue) == 0:
        time += 1
        continue

    idx = queue.pop(0)

    if rt[idx] > tq:

        rt[idx] -= tq
        time += tq

        print(" ->", p[idx], "->", time, end="")

        # Add newly arrived processes during execution
        for i in range(n):
            if at[i] <= time and visited[i] == 0:
                queue.append(i)
                visited[i] = 1

        queue.append(idx)

    else:

        time += rt[idx]

        print(" ->", p[idx], "->", time, end="")

        rt[idx] = 0
        ct[idx] = time
        completed += 1

        # Add newly arrived processes during execution
        for i in range(n):
            if at[i] <= time and visited[i] == 0:
                queue.append(i)
                visited[i] = 1

print()

# Calculate TAT and WT
for i in range(n):
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]

print("\nProcess\tAT\tBT\tCT\tTAT\tWT")

for i in range(n):
    print(f"{p[i]}\t\t{at[i]}\t{bt[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")

print("\nAverage TAT =", sum(tat)/n)
print("Average WT  =", sum(wt)/n)