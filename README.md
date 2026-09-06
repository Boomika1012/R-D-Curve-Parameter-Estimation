# R-D Curve Parameter Estimation

## Objective

Find the unknown parameters θ, M, and X for the given parametric curve using the provided xy_data.csv dataset.

## Given Equation

x = t cos(θ) - e^(M|t|) sin(0.3t) sin(θ) + X

y = 42 + t sin(θ) + e^(M|t|) sin(0.3t) cos(θ)

## Parameter Ranges

- 0° < θ < 50°
- -0.05 < M < 0.05
- 0 < X < 100
- 6 < t < 60

## Method

The given points were compared with points generated from the parametric curve.

The L1 distance between the given points and the generated curve was used as the objective function.

Differential Evolution was used to estimate θ, M, and X within the given parameter ranges.

## Result

θ = 30°

M = 0.03

X = 55
