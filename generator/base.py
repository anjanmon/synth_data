from abc import ABC, abstractmethod
from typing import Any, Dict, Optional
import numpy as np

class BaseGenerator(ABC):
    def __init__(self, name: str, params: Optional[Dict[str, Any]] = None):
        pass

    @abstractmethod
    def synth(self, size: int) -> None:
        pass

    def add_noise(self) -> None:
        pass

    @abstractmethod
    def generate(self, size: int) -> Optional[np.ndarray]:
        pass
