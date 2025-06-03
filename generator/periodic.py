from typing import Any, Dict, Optional

import numpy as np
from base import BaseGenerator


class Periodic(BaseGenerator):
    def __init__(self, name: str, params: Optional[Dict[str, Any]] = None) -> None:
        self.name = name
        self.params = params or {}
        self.synth_output = None
        self.size = None

    def synth(self, size: int, start: float = 0, stop: float = 2 * np.pi) -> None:
        self.size = size
        x = np.linspace(start, stop, size)
        y = np.sin(x)
        self.synth_output = np.column_stack((x, y))

    def add_noise(self, scale: float = 0.1) -> None:
        if self.synth_output is None:
            raise ValueError("synth_output is None. Call synth() before add_noise().")
        noise = np.random.normal(0, scale=0.1, size=self.size)
        self.synth_output[:, 1] += noise

    def generate(
        self,
        size: int = 100,
        start: float = 0.0,
        stop: float = 2 * np.pi,
        noise_scale: float = 0.1,
        add_noise: bool = True,
    ) -> Optional[np.ndarray]:
        """
        Generates periodic data with optional noise.

        Args:
            size (int): Number of data points.
            start (float): Start value of the x-range.
            stop (float): Stop value of the x-range.
            noise_scale (float): Standard deviation of the noise to add.
            add_noise (bool): Whether to add noise to the sine values.

        Returns:
            Optional[np.ndarray]: The generated (x, y) dataset.
        """
        self.synth(size=size, start=start, stop=stop)
        if add_noise:
            self.add_noise(scale=noise_scale)
        return self.synth_output
