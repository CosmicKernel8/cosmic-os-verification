
import csv
import matplotlib.pyplot as plt

data = {"Euler": [], "RK4": []}

with open("method_comparison.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        method = row["method"]
        dt = float(row["dt"])
        error = float(row["error"])

        if error > 0:
            data[method].append((dt, error))

for method, values in data.items():
    values.sort()
    x = [v[0] for v in values]
    y = [v[1] for v in values]
    plt.plot(x, y, marker="o", label=method)

plt.yscale("log")
plt.xlabel("Time Step (dt)")
plt.ylabel("Absolute Error (log scale)")
plt.title("Euler vs RK4: Numerical Error")
plt.legend()
plt.grid(True, which="both", alpha=0.3)
plt.tight_layout()

plt.savefig("method_comparison_plot.png", dpi=200)
plt.show()

print("Graph saved: method_comparison_plot.png")
