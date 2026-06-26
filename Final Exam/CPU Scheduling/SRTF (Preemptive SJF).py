# SRTF (Preemptive SJF)

n = int(input("Enter number of processes: "))

p = ["P"+str(i+1) for i in range(n)]
at = list(map(int, input("Enter AT: ").split()))
bt = list(map(int, input("Enter BT: ").split()))

remt = bt.copy()      # Remaining Time

ct = [0]*n
tat = [0]*n
wt = [0]*n
done = [0]*n

time = 0
completed = 0

# Gantt Chart
print("\nSRTF Gantt Chart:")
print("0", end="")

while completed < n:

    idx = -1
    mn = 999

    for i in range(n):
        if at[i] <= time and done[i] == 0:

            if remt[i] < mn:
                mn = remt[i]
                idx = i

            elif remt[i] == mn:
                if at[i] < at[idx]:
                    idx = i

    if idx == -1:
        time += 1
        continue

    remt[idx] -= 1
    time += 1

    print(" ->", p[idx], "->", time, end="")

    if remt[idx] == 0:
        done[idx] = 1
        ct[idx] = time
        completed += 1

print()

# Calculate TAT and WT
for i in range(n):
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]

# Output Table
print("\nProcess\tAT\tBT\tCT\tTAT\tWT")

for i in range(n):
    print(f"{p[i]}\t\t{at[i]}\t{bt[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")

print("\nAverage TAT =", sum(tat)/n)
print("Average WT  =", sum(wt)/n)