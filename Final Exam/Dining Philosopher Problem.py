import threading
import time

N = 5
forks = [threading.Lock() for i in range(N)]
Eaten = [False]*N

def Philosopher_deadlock(i):
    left_fork = forks[i]
    right_fork = forks[(i+1) % N]

    print(f"\n Philosopher{i} is Thinking... ")
    print(f"\n Philosopher{i} Picked up Left fork ")
    left_fork.acquire()
    time.sleep(1)

    print(f"\n Philosopher{i} WAITING for RIGHT Fork ")
    right_fork.acquire()

    print(f"\n Philosopher{i} is Eating ")
    Eaten[i] = True

    left_fork.release()
    right_fork.release()

def philosopher_NO_Deadlock(i):
    left_fork = forks[i]
    right_fork = forks[(i + 1) % N]

    print(f"\n Philosopher{i} is Thinking... ")
    if i == N-1:
        right_fork.acquire()
        print(f"\n Philosopher{i} Picked up RIGHT fork ")
        left_fork.acquire()
        print(f"\n Philosopher{i} Picked up LEFT fork ")

    else:
        left_fork.acquire()
        print(f"\n Philosopher{i} Picked up LEFT fork ")
        right_fork.acquire()
        print(f"\n Philosopher{i} Picked up RIGHT fork ")

    print(f"\n Philosopher{i} is Eating ")
    Eaten[i] = True
    time.sleep(1)

    left_fork.release()
    right_fork.release()


choice = int(input("1. DeadLock Version \n2. DeadLock Free Version \n Enter Your Choice (1 / 2) : "))

threads = []

if choice == 1:
    print("\nRunning Deadlock Version...")

    for i in range(N):
        thread = threading.Thread(target = Philosopher_deadlock, args=(i,))
        threads.append(thread)
        thread.start()

else:
    print("\nRunning Deadlock FREE Version...")

    for i in range(N):
        thread = threading.Thread(target=philosopher_NO_Deadlock, args=(i,))
        threads.append(thread)
        thread.start()

time.sleep(5)

if all(Eaten):
    print("\n NO DEADLOCK OCCURED 💯")
else:
    print("\n DEADLOCK OCCURED 💀")
