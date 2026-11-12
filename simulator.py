import math

gamma = 2.0
lam = 1.0
psi = 0.1
dt = 0.1

def exact_solution(t):
    return 1 / math.sqrt(1 + 99 * math.exp(-t))

print("Time | Numerical | Exact | Error")
print("-" * 45)

for step in range(101):
    t = step * dt

    if step % 10 == 0:
        exact = exact_solution(t)
        error = abs(psi - exact)

        print(
            f"{t:4.1f} | {psi:.6f} | "
            f"{exact:.6f} | {error:.6f}"
        )

    dpsi_dt = (lam / gamma) * psi * (1 - psi**2)
    psi += dpsi_dt * dt

