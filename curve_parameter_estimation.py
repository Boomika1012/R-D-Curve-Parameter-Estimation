import numpy as np
import pandas as pd
from scipy.optimize import differential_evolution
from scipy.spatial import cKDTree

data = pd.read_csv("xy_data.csv")
x_data = data["x"].to_numpy()
y_data = data["y"].to_numpy()
actual_points = np.column_stack((x_data, y_data))

def generate_curve(theta, M, X, n=3000):
    t = np.linspace(6, 60, n)
    theta = np.radians(theta)
    x = (
        t * np.cos(theta)
        - np.exp(M * np.abs(t))
        * np.sin(0.3 * t)
        * np.sin(theta)
        + X
    )
    y = (
        42
        + t * np.sin(theta)
        + np.exp(M * np.abs(t))
        * np.sin(0.3 * t)
        * np.cos(theta)
    )
    return np.column_stack((x, y))

def objective(params):
    theta, M, X = params
    predicted_points = generate_curve(theta, M, X)
    tree = cKDTree(predicted_points)
    distances, _ = tree.query(actual_points)
    return np.sum(distances)

bounds = [
    (0, 50),       # theta
    (-0.05, 0.05), # M
    (0, 100)       # X
]

result = differential_evolution(
    objective,
    bounds,
    seed=42,
    tol=1e-8,
    polish=True
)

theta, M, X = result.x
print("\nOptimal Parameters")
print(f"theta = {round(theta)} degrees")
print(f"M     = {M:.2f}")
print(f"X     = {round(X)}")