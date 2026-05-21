n = int(input("Number of processes: "))

process = []
burst = []

for i in range(n):
    process.append(input("Process name: "))
    burst.append(int(input("Burst time: ")))

def fcfs():
    print("\nFCFS Scheduling")

    waiting = [0] * n

    for i in range(1, n):
        waiting[i] = waiting[i - 1] + burst[i - 1]

    for i in range(n):
        print(process[i], "Waiting:", waiting[i])

def sjf():
    print("\nSJF Scheduling")

    data = []

    for i in range(n):
        data.append([process[i], burst[i]])

    for i in range(n):
        for j in range(i + 1, n):
            if data[i][1] > data[j][1]:
                data[i], data[j] = data[j], data[i]

    waiting = [0] * n
    time = 0

    for i in range(n):
        print(data[i][0], "Waiting:", time)
        time += data[i][1]

def round_robin():
    print("\nRound Robin Scheduling")

    quantum = int(input("Time quantum: "))

    remaining = burst.copy()
    time = 0

    while True:
        done = True

        for i in range(n):
            if remaining[i] > 0:
                done = False  

                if remaining[i] > quantum:
                    print(process[i], "runs", quantum)
                    remaining[i] -= quantum
                    time += quantum
                else:
                    print(process[i], "runs", remaining[i])
                    time += remaining[i]
                    remaining[i] = 0
        if done:
            break

fcfs()
sjf()
round_robin()
