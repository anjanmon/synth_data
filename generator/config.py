import enum
import os
from dataclasses import dataclass, field
from typing import List, Optional

import yaml
from dotenv import load_dotenv

load_dotenv()


class Function(enum.Enum):
    SINE = "sine"

    @classmethod
    def from_str(cls, name: str):
        name = name.lower()
        for member in cls:
            if member.value.lower() == name:
                return member
        raise ValueError(f"Invalid generator type: {name}")


@dataclass
class Config:
    name: str
    function: Function
    size: Optional[int] = 100
    start: Optional[int] = 0
    stop: Optional[int] = 1
    add_noise: bool = True
    noise_scale: Optional[float] = 0.1

    def metadata(self):
        pass


@dataclass
class DataGen:
    "Class for keeping track of all the data generators"

    configs: List[Config] = field(default_factory=list)

    @classmethod
    def build(cls, config_path: Optional[str] = None):
        if config_path is None:
            config_path = os.getenv("CONFIG_PATH")
            if not config_path:
                raise RuntimeError(
                    "CONFIG_PATH is not set. Please provide the path explicitly or set the CONFIG_PATH environment variable."
                )
        with open(config_path, "r") as file:
            configs = yaml.safe_load(file)

        return cls(
            configs=[
                Config(**{**cfg, "function": Function.from_str(cfg["function"])})
                for cfg in configs["datasets"]
            ]
        )

    @property
    def num_configs(self):
        return len(self.configs)
