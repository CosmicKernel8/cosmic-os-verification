# Experiment 01: Euler Method Convergence

## Objective

Verify the numerical accuracy of Euler's method for a simplified order-parameter transition equation from Cosmic OS.

## Mathematical Model

The simplified equation is:

`gamma * dpsi/dt = lambda * psi * (1 - psi^2)`

Parameters:
- gamma = 2.0
- lambda = 1.0
- Initial condition: psi(0) = 0.1
- Simulation interval: t = 0 to 10

The analytical solution for these parameters is:

`psi(t) = 1 / sqrt(1 + 99 * exp(-t))`

## Method

I implemented Euler's method in Python and compared the numerical results with the analytical solution.

I repeated the simulation using three different time steps: 0.1, 0.05, and 0.01.

## Results

Absolute errors at t = 4:

| Time Step (dt) | Numerical Solution | Analytical Solution | Absolute Error |
|---|---|---|---|
| 0.1 | 0.583159 | 0.596205 | 0.013047 |
| 0.05 | 0.589685 | 0.596205 | 0.006521 |
| 0.01 | 0.594902 | 0.596205 | 0.001303 |

## Findings

Reducing the time step reduced the numerical error.

When the time step decreased from 0.1 to 0.01, the absolute error at t = 4 decreased by approximately a factor of 10.

This result is consistent with the first-order convergence behavior of Euler's method.

## Limitations

This experiment verifies the numerical behavior of a simplified differential equation, not the physical validity of Cosmic OS or its cosmological predictions.

Further work is required to test the full dissipative model and compare predictions with observational data.
