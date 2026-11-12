# Experiment 02: Euler vs RK4

## Objective

Compare the numerical accuracy and computational cost of Euler's method and the fourth-order Runge-Kutta method (RK4).

## Method

Both algorithms were applied to the same simplified differential equation used in Experiment 01.

The numerical solutions were compared against the analytical solution at t = 4.

Computational cost was measured using the number of derivative evaluations, not execution time.

## Results

| Method | Time Step | Derivative Evaluations | Absolute Error |
|---|---|---|---|
| Euler | 0.20 | 20 | 0.0260704649 |
| RK4 | 0.20 | 80 | 0.0000004623 |
| Euler | 0.10 | 40 | 0.0130467699 |
| RK4 | 0.10 | 160 | 0.0000000295 |
| Euler | 0.05 | 80 | 0.0065208658 |
| RK4 | 0.05 | 320 | 0.0000000019 |
| Euler | 0.01 | 400 | 0.0013032433 |
| RK4 | 0.01 | 1600 | Less than 0.00000000005 (based on rounded output) |

## Key Finding

At a budget of 80 derivative evaluations:

- Euler (dt = 0.05) produced an error of approximately 0.00652.
- RK4 (dt = 0.20) produced an error of approximately 0.000000462.

Under these conditions, RK4 achieved approximately 14,100 times lower absolute error with the same number of derivative evaluations.

## Limitations

This result applies to the tested equation, parameters, and time interval.

Derivative evaluation counts do not represent complete runtime or memory costs.

The experiment does not validate the broader physical hypotheses of Cosmic OS.
