"""
2D Kalman filter tracking example.

Simulates tracking of a moving object in two dimensions using noisy
position measurements.
"""

import numpy as np
import matplotlib.pyplot as plt


def simulate_motion(n: int = 100) -> np.ndarray:
    """Generate a simple 2D linear trajectory.

    Generates n points along the line y = 0.5 * x, with x uniformly
    spaced from 0 to 10.
    
    Args:
        n: Number of samples in the trajectory.

    Returns:
        np.ndarray: Array of shape (n, 2) with columns [x, y].
    """
    x = np.linspace(0, 10, n)
    y = 0.5 * x

    return np.vstack((x, y)).T


def add_noise(signal: np.ndarray, std: float = 0.5) -> np.ndarray:
    """Add Gaussian noise to a 2D trajectory.

    Args:
        signal: Input trajectory of shape (n, 2).
        std: Standard deviation of the Gaussian noise.

    Returns:
        np.ndarray: Noisy trajectory of the same shape as signal.
    """
    noise = np.random.normal(0, std, signal.shape)
    return signal + noise


def kalman_filter(measurements: np.ndarray) -> np.ndarray:
    """Apply a simple 2D Kalman filter for position estimation.

    Uses an identity state transition and observation model to filter
    noisy 2D position measurements.

    Args:
        measurements: Array of shape (n, 2) with noisy position data.

    Returns:
        np.ndarray: Filtered position estimates of shape (n, 2).
    """
    x = np.array([0.0, 0.0])
    P = np.eye(2)

    Q = np.eye(2) * 0.01
    R = np.eye(2) * 0.5

    estimates = []

    for z in measurements:
        # Prediction
        P = P + Q
        K = P @ np.linalg.inv(P + R)

        # Update
        x = x + K @ (z - x)
        P = (np.eye(2) - K) @ P

        estimates.append(x.copy())

    return np.array(estimates)


if __name__ == "__main__":
    np.random.seed(42)

    true_path = simulate_motion()
    measurements = add_noise(true_path)

    estimates = kalman_filter(measurements)

    plt.plot(true_path[:, 0], true_path[:, 1], label="True path")
    plt.scatter(measurements[:, 0], measurements[:, 1],
                alpha=0.5, label="Measurements")
    plt.plot(estimates[:, 0], estimates[:, 1], label="Kalman estimate")

    plt.legend()
    plt.title("2D Kalman Filter Tracking")

    plt.savefig("../assets/kalman_2d_tracking.png")
