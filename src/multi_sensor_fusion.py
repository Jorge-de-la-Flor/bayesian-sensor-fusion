"""
Multi-sensor fusion demonstration.

Simulates two sensors with different noise levels measuring the same
underlying 1D signal and fuses their outputs.
"""

import numpy as np
import matplotlib.pyplot as plt


def generate_signal(n: int = 200) -> tuple[np.ndarray, np.ndarray]:
    """Generate a 1D sinusoidal signal.

    Args:
        n: Number of time samples.

    Returns:
        tuple[np.ndarray, np.ndarray]: Time vector t and signal values
        sin(t), both of length n.
    """
    t = np.linspace(0, 10, n)
    signal = np.sin(t)
    return t, signal


def noisy_sensor(signal: np.ndarray, std: float) -> np.ndarray:
    """Simulate a noisy sensor measuring a 1D signal.

    Args:
        signal: Clean 1D signal samples.
        std: Standard deviation of the additive Gaussian noise.

    Returns:
        np.ndarray: Noisy measurements with the same shape as signal.
    """
    noise = np.random.normal(0, std, len(signal))
    return signal + noise


def fuse(sensor_a: np.ndarray, sensor_b: np.ndarray) -> np.ndarray:
    """Fuse two sensor measurements by simple averaging.

    Args:
        sensor_a: First sensor measurements.
        sensor_b: Second sensor measurements.

    Returns:
        np.ndarray: Element-wise average of the two sensor signals.
    """
    return (sensor_a + sensor_b) / 2


if __name__ == "__main__":
    np.random.seed(42)

    t, true_signal = generate_signal()

    sensor1 = noisy_sensor(true_signal, 0.2)
    sensor2 = noisy_sensor(true_signal, 0.5)

    fused = fuse(sensor1, sensor2)

    plt.plot(t, true_signal, label="True signal")
    plt.plot(t, sensor1, alpha=0.5, label="Sensor 1")
    plt.plot(t, sensor2, alpha=0.5, label="Sensor 2")
    plt.plot(t, fused, label="Fused estimate")

    plt.legend()
    plt.title("Multi-Sensor Fusion")

    plt.savefig("../assets/multi_sensor_fusion.png")
