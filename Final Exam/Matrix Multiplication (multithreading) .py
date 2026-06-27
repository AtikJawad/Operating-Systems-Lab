import threading
import random
import time

size = int(input("Enter Matrix Size: "))

A = [[random.randint(1, 10) for j in range(size)] for i in range(size)]
B = [[random.randint(1, 10) for j in range(size)] for i in range(size)]

C = [[0] * size for _ in range(size)]

def multiply_row(row):

    for j in range(size):

        total = 0

        for k in range(size):
            total += A[row][k] * B[k][j]

        C[row][j] = total

start = time.time()

threads = []

for i in range(size):

    thread = threading.Thread(target=multiply_row, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end = time.time()

print("\nMultiplication Completed!")
print("Execution Time:", round(end - start, 4), "seconds")

# Print matrices only if small
if size <= 10:

    print("\nMatrix A:")
    for row in A:
        print(row)

    print("\nMatrix B:")
    for row in B:
        print(row)

    print("\nResult Matrix C:")
    for row in C:
        print(row)

else:

    print("\nMatrix too large to display.")

    print("\nFirst 5 rows and 5 columns of Result Matrix:")

    for i in range(min(5, size)):
        print(C[i][:5])
