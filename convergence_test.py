import math
import csv

GAMMA = 2.0
LAM = 1.0
INITIAL_PSI = 0.1
TARGET_TIME = 4.0

def exact_solution(t):
    return 1 / math.sqrt(1 + 99 * math.exp(-t))

def simulate(dt):
    psi = INITIAL_PSI
    steps = round(TARGET_TIME / dt)

    for _ in range(steps):
        dpsi_dt = (LAM / GAMMA) * psi * (1 - psi**2)
        psi += dpsi_dt * dt

    return psi

time_steps = [0.1, 0.05, 0.01]
results = []

for dt in time_steps:
    numerical = simulate(dt)
    exact = exact_solution(TARGET_TIME)
    error = abs(numerical - exact)

    results.append([dt, numerical, exact, error])

    print(f"dt={dt:.2f}, error={error:.8f}")

with open("convergence_results.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["dt", "numerical", "exact", "error"])
    writer.writerows(results)

print("Results saved to convergence_results.csv")

