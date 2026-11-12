import math
import csv

# Experiment 02: Euler vs RK4

GAMMA = 2.0
LAM = 1.0
INITIAL_PSI = 0.1
TARGET_TIME = 4.0

def derivative(psi):
    return (LAM / GAMMA) * psi * (1 - psi**2)

def exact_solution(t):
    return 1 / math.sqrt(1 + 99 * math.exp(-t))

def euler_step(psi, dt):
    return psi + dt * derivative(psi)

def rk4_step(psi, dt):
    k1 = derivative(psi)
    k2 = derivative(psi + dt * k1 / 2)
    k3 = derivative(psi + dt * k2 / 2)
    k4 = derivative(psi + dt * k3)

    return psi + dt * (k1 + 2*k2 + 2*k3 + k4) / 6

def simulate(method, dt):
    psi = INITIAL_PSI
    steps = round(TARGET_TIME / dt)

    for _ in range(steps):
        psi = method(psi, dt)

    return psi

results = []
exact = exact_solution(TARGET_TIME)

print("Method | dt | Error | Derivative Evaluations")
print("-" * 60)

for dt in [0.2, 0.1, 0.05, 0.01]:
    steps = round(TARGET_TIME / dt)

    for name, method, evaluations in [
        ("Euler", euler_step, 1),
        ("RK4", rk4_step, 4)
    ]:
        numerical = simulate(method, dt)
        error = abs(numerical - exact)
        cost = steps * evaluations

        results.append([name, dt, numerical, exact, error, cost])

        print(
            f"{name:5} | {dt:.2f} | "
            f"{error:.10f} | {cost}"
        )

with open("method_comparison.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "method", "dt", "numerical",
        "exact", "error", "derivative_evaluations"
    ])
    writer.writerows(results)

print("\nResults saved to method_comparison.csv")
