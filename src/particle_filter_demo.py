"""
Particle filter tracking demonstration.

Tracks a moving target in 1D using a simple particle filter with
Gaussian process noise and noisy position measurements.
"""

import numpy as np
import matplotlib.pyplot as plt


def simulate_motion(n: int = 100) -> np.ndarray:
    """Generate a simple 1D linear motion signal.

    The target moves from position 0 to 10 over n time steps.

    Args:
        n: Number of time steps.

    Returns:
        np.ndarray: Array of shape (n,) with true positions.
    """
    x = np.linspace(0, 10, n)
    return x


def particle_filter(measurements: np.ndarray, num_particles: int = 200) -> np.ndarray:
    """Estimate a 1D trajectory using a basic particle filter.

    The filter assumes:
    - A simple random-walk motion model for particles.
    - Gaussian measurement likelihood.
    - Systematic resampling via weighted random choice each step.

    Args:
        measurements: Noisy position measurements of shape (n,).
        num_particles: Number of particles used in the filter.

    Returns:
        np.ndarray: Estimated positions of shape (n,).
    """
    particles = np.random.uniform(0, 10, num_particles)
    weights = np.ones(num_particles) / num_particles

    estimates = []

    for z in measurements:
        # Predict: propagate particles with process noise.
        particles += np.random.normal(0, 0.1, num_particles)

        # Update: compute importance weights from measurement likelihood.
        weights *= np.exp(-(particles - z) ** 2)
        weights += 1e-300  # Avoid numerical underflow.
        weights /= np.sum(weights)

        # Estimate: weighted average of particles.
        estimate = np.sum(particles * weights)
        estimates.append(estimate)

        # Resample: draw new particles according to weights.
        indices = np.random.choice(range(num_particles), num_particles, p=weights)
        particles = particles[indices]
        weights.fill(1.0 / num_particles)

    return np.array(estimates)


if __name__ == "__main__":
    np.random.seed(42)

    true_signal = simulate_motion()
    measurements = true_signal + np.random.normal(0, 0.5, len(true_signal))

    estimates = particle_filter(measurements)

    plt.plot(true_signal, label="True signal")
    plt.scatter(
        range(len(measurements)),
        measurements,
        alpha=0.5,
        label="Measurements",
    )
    plt.plot(estimates, label="Particle filter estimate")

    plt.legend()
    plt.title("Particle Filter Tracking")

    plt.savefig("../assets/particle_filter_tracking.png")
