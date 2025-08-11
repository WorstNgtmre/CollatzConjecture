## collatz_conjecture.py

import matplotlib.pyplot as plt

def evenfunction(n: int) -> int:
    return n // 2
def oddfunction(n: int) -> int:
    return 3 * n + 1

def collatz(n: int) -> list:
    steps = 0
    log = [n]
    while n != 1:
        if n % 2 == 0:
            n = evenfunction(n)
        else:
            n = oddfunction(n)
        steps += 1
        log.append(n)

    highest_num = max(log)
    print(f"Highest number reached in the sequence: {highest_num}") 
    print(f"Number of steps: {steps}")
    return log    

def plot_graph(log: list) -> None:
    plt.plot(log, marker='o')
    plt.title("Collatz Conjecture Sequence")
    plt.xlabel("Step")
    plt.ylabel("Value")
    plt.grid()
    plt.show()

#Main program loop
while True:
    try:
        n = int(input("Enter a positive integer (or 0 to exit): "))
        if n == 0:
            break
        elif n < 1:
            input("Please enter a positive integer: ")
            continue

        plot_graph(collatz(n))

    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")