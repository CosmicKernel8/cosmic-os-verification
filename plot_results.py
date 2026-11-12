import csv
import matplotlib.pyplot as plt

dt_values = []
errors = []

with open("convergence_results.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        dt_values.append(float(row["dt"]))
        errors.append(float(row["error"]))

plt.figure(figsize=(8, 5))

plt.plot(dt_values, errors, marker="o", label="Euler Error")

plt.xlabel("Time Step (dt)")
plt.ylabel("Absolute Error at t=4")
plt.title("Euler Method Convergence Test")

plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("convergence_plot.png", dpi=200)
print("Graph saved to convergence_plot.png")
