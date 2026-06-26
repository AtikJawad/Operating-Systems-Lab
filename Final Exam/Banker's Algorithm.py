# Banker's Algorithm

n = int(input("Enter number of processes: "))
m = int(input("Enter number of resources: "))

alloc = []
print("\nEnter Allocation Matrix:")
for i in range(n):
    alloc.append(list(map(int, input().split())))

mx = []
print("\nEnter Maximum Matrix:")
for i in range(n):
    mx.append(list(map(int, input().split())))

avail = list(map(int, input("\nEnter Available Resources: ").split()))

# Need Matrix
need = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        need[i][j] = mx[i][j] - alloc[i][j]

finish = [0]*n
safe = []

while len(safe) < n:

    found = False

    for i in range(n):

        if finish[i] == 0:

            possible = True

            for j in range(m):
                if need[i][j] > avail[j]:
                    possible = False
                    break

            if possible:

                safe.append(i)
                finish[i] = 1

                for j in range(m):
                    avail[j] += alloc[i][j]

                found = True

    if not found:
        break

# Output
print("\nNeed Matrix:")
for row in need:
    print(row)

if len(safe) == n:

    print("\nSystem is SAFE")

    print("Safe Sequence:", end=" ")
    for i in safe:
        print("P"+str(i), end=" ")
    print()

else:
    print("\nSystem is UNSAFE")
