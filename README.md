# Cosmic OS Verification

**From speculative ideas to reproducible experiments.**

## 1. Project Overview

Cosmic OS began as a personal exploration of relationships between information, entropy, and physical systems.

During its development, I recognized an important limitation: generating mathematical models and Python code with AI does not automatically establish that the models are correct.

I therefore created this repository to take a more systematic approach: isolate a small mathematical model, implement it in Python, compare its numerical output with an analytical solution, and document the results.

## 2. First Experiment: Numerical Convergence

The first experiment examines a simplified order-parameter transition equation:

`gamma * dpsi/dt = lambda * psi * (1 - psi^2)`

Using Euler's method, I simulated the equation with three different time steps and compared the numerical results against an analytical solution.

### Results

| Time Step | Absolute Error at t=4 |
|---|---|
| 0.10 | 0.01304677 |
| 0.05 | 0.00652087 |
| 0.01 | 0.00130324 |

The numerical error decreased as the time step became smaller, consistent with the expected first-order convergence behavior of Euler's method.

![Euler Convergence Test](convergence_plot.png)

## 3. Project Structure

- `simulator.py` — Numerical simulation and analytical comparison
- `convergence_test.py` — Automated convergence experiment
- `plot_results.py` — Visualization of numerical errors
- `convergence_results.csv` — Generated experiment data
- `convergence_plot.png` — Experiment visualization
- `results/experiment.md` — Experiment documentation

## 4. How to Run

Requirements:
- Python 3
- Matplotlib

Install the plotting dependency:

`python -m pip install matplotlib`

Run the experiments:

```bash
python simulator.py
python convergence_test.py
python plot_results.py
```

## 5. Limitations

This project verifies the numerical behavior of a simplified differential equation. It does not establish the physical validity of the broader Cosmic OS framework.

The current experiment uses a known analytical solution and a basic numerical method. It is intended as an initial step toward more rigorous testing.

## 6. Future Improvements

- Add automated correctness tests
- Compare Euler's method with higher-order numerical methods
- Explore parameter sensitivity
- Investigate whether more complex models produce testable predictions

## 7. Development Approach

AI tools assisted with code generation, debugging, and documentation.

My goal is to move beyond accepting AI-generated outputs and toward independently testing, understanding, and improving them.
