
import math

# Cosmic OS: Order Parameter Transition
# gamma * dpsi/dt = lambda * psi * (1 - psi**2)

gamma = 2.0
lam = 1.0
psi = 0.1
dt = 0.1

print("Time | Psi")
print("-" * 20)

for step in range(101):
    t = step * dt

    if step % 10 == 0:
        print(f"{t:4.1f} | {psi:.6f}")

    # Euler numerical integration
    dpsi_dt = (lam / gamma) * psi * (1 - psi**2)
    psi = psi + dpsi_dt * dt
